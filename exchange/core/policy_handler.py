import threading, sys
import params_sdx
import logging as log
from itertools import count
import rule_sdx as rule
import policy_sdx as policy
import utility


log.basicConfig(filename='sdx.log',level=log.DEBUG)
iid = count()

def rule_gen(policy_obj):
    # use ur parsing logic to make the appropriate rule object
    ruleo = rule.rule()
    ruleo.rid=next(iid)
    ruleo.raw=policy_obj.policy_raw
    log.info('To parse the rule text: %s',ruleo.raw)
    policy_type = ruleo.raw.split(':')[0]
    if policy_type=="sdx_offload":
        policy_obj.sdx_policy_type = policy.policy_offload()
        rules = policy.policy_offload.rule_gen(policy_obj.sdx_policy_type,ruleo)
    elif policy_type=="sdx_autoOpenPeering":
        log.info('Retrieved Auto Open Peering policy')
    # We will have more options in future

    return rules


def check_rule(rule):
    ofsid=0
    status =True
    rule.ofsid = ofsid
    # logic to check if the rule already pushed to the switch
    return status


def assign_priority(rule):
    priority=1
    rule.priority=priority
    return True

def composition_seq(r):
    seq= 'out_'+utility.mac_to_player(r.match_dl_src)+'<< in_'+utility.mac_to_player(r.match_dl_dst)+'<< out_'+\
        utility.mac_to_player(r.action_dl_src)+'<< in_'+utility.mac_to_player(r.action_dl_dst)
    r.comseq=seq
    return seq

def rule_classifier(r):
    print r.match_dl_src
    print r.owner
    if r.match_dl_src==r.owner:
        classifier='out_'+utility.mac_to_player(r.owner)
        r.priority=100
        r.classifier=classifier
    elif r.match_dl_dst==r.owner:
        classifier='in_'+utility.mac_to_player(r.owner)
        r.priority=200
        r.classifier=classifier
    else:
        classifier='drop'
    return classifier

def add_rule(r):
    ## FOR LATER: make sure to assign highest priority to latest rule added in the table entry, currently not implemented
    t=r.classifier.split('_')
    m=t[1]
    if t[0]=='in':
        ind=0
    else:
        ind=1
    params_sdx.RT[m][ind].append(r)

def rule_compose(r):
    newrules=[]
    seq=r.compseq.split(r.classifier)[1]
    a=seq.split('<< ')
    newrules.append(r)
    for ind in range(0,len(a)-1):
        cand=a[ind+1]
        member=cand.split('_')[1]
        if cand.split('_')[0]=='in':
            index=0
        else:
            index=1
        rules=params_sdx.RT[member][index]
        for ruleo in rules:
            #seq_comp(r,rule)
            print ruleo.debug_display_rule()
            print 'reached end of rule_compose'
    log.info('Rule composer called')

class PQ_scheduler(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        log.info('Scheduler Thread Started')
        while 1:
            if params_sdx.PQ.qsize>0:
                log.info('Policy to process for scheduler')

                # grab the rule from the Policy Queue and generate corresponding rule object
                policy_obj = params_sdx.PQ.get()
                rules = rule_gen(policy_obj)
                compseq={}
                rule_class={}
                for r in rules:
                    # classify this rule
                    rule_class[r]=rule_classifier(r)
                    #p=rule.rule()
                    #p.match_dl_dst='test'
                    log.info('match.dst: %s',r.match_dl_dst)
                    if rule_class[r]=='drop':
                        log.info('Drop this rule as it lacks port authorization')
                        break
                    # Add it to rule table
                    add_rule(r)
                    # Determine composition sequence
                    compseq[r]=composition_seq(r)
                    print compseq[r]
                    # Now time to compose this rule
                    #rule_compose(r)


                # check if rule exists in the database already and filter rules that need to be discarded


                # send this rule object to a pox controller which will translate this rule object to OFS rule
                # Also it has list of rules to discard from the switch
                # final step to integrate with the POX controller


