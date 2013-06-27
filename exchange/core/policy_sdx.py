__author__ = 'arpit'

import rule_sdx as rule
import logging as log
import utility

log.basicConfig(filename='sdx.log', level=log.DEBUG)


class policy():
    def __init__(self, player_ip='', player_port=0, player_prio=0, policy_type=None, policy_raw=''
                 , rule_id=0, rule=rule.rule()):
        self.player_ip = player_ip
        self.player_port = player_port
        self.player_prio = player_prio
        self.policy_type = policy_type
        self.policy_raw = policy_raw
        self.rule_id = rule_id
        self.rule = rule
        log.info('policy object created')


class policy_offload():
    def __init__(self, name='offload', participants={}):
        # we will have provider,customer hashtable /dictionary for creating rules from this object
        self.name = name
        self.participants = participants

    def rule_gen(self,rule_obj):
        log.info('Rule text: %s', rule_obj.raw)
        rules=[]
        part={}
        text = rule_obj.raw
        print text
        n_comb=len(text.split('{'))-1
        requester = text.split(':')[1].split(',')[0]
        log.info('need to resolve %s rules for offloading request from %s',n_comb,requester)
        for i in range(0,n_comb):
            log.info('%s',i)
            provider=text.split('{')[i+1].split(':')[0]
            customers=text.split('{')[i+1].split(':')[1].split('}')[0]
            part[provider]=customers

            clist=customers.split(',')
            n_cust=len(clist)
            print n_cust
            print part
            ruleo=rule.rule()
            ruleo.owner=utility.player_to_mac(requester)
            ruleo.match_dl_dst=utility.player_to_mac(requester)
            ruleo.match_nw_dst=utility.player_to_nw(provider)
            print customers
            for cust in clist:
                print cust
                ## Need to take care of having multiple src macs here
                ruleo.match_dl_src=utility.player_to_mac(cust)
            ruleo.action_dl_src=utility.player_to_mac(requester)
            ruleo.action_dl_dst=utility.player_to_mac(provider)
            rules.append(ruleo)
            print ruleo.action_dl_dst
        self.participants = part
        print self.participants

        return rules


        ## We will create classes for other policy types when required