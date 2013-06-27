__author__ = 'arpit'


# focus on unit testing in this module before integration
import rule_sdx as rule
import logging as log
log.basicConfig(filename='seqcomp.log',level=log.DEBUG)


PREFIXES_A = ["100.0.0.0/24", "110.0.0.0/24", "120.0.0.0/24"]
PREFIXES_B=[]
PREFIXES_C=[]

flow_params=['in_port','vlan','dl_src','dl_dst','dl_type','nw_src','nw_dst','nw_proto','tp_src','tp_dst']

def flow_to_vec(r,param1):
    # I know there must be a better way of doing it
    fv=[]
    if param1=='match':
        fv.append(r.match_in_port)
        fv.append(r.match_vlan)
        fv.append(r.match_dl_src)
        fv.append(r.match_dl_dst)
        fv.append(r.match_dl_type)
        fv.append(r.match_nw_src)
        fv.append(r.match_nw_dst)
        fv.append(r.match_nw_proto)
        fv.append(r.match_tp_src)
        fv.append(r.match_tp_dst)

    if param1=='action':
        fv.append(r.action_in_port)
        fv.append(r.action_vlan)
        fv.append(r.action_dl_src)
        fv.append(r.action_dl_dst)
        fv.append(r.action_dl_type)
        fv.append(r.action_nw_src)
        fv.append(r.action_nw_dst)
        fv.append(r.action_nw_proto)
        fv.append(r.action_tp_src)
        fv.append(r.action_tp_dst)

    return fv

def sequential_comp(r1,r2):
    r=rule.rule()
    # Create action Vectors, to make things easier !!
    action_fv1=flow_to_vec(r1,'action')
    action_fv2=flow_to_vec(r2,'action')
    match_fv1=flow_to_vec(r1,'match')
    match_fv2=flow_to_vec(r2,'match')

    # Find if they overlap, there should be atleast one field from action of r1 overlap with predicate of r2
    overlap=0
    conflict=[]
    for ind in range(0,len(match_fv1)):
        #print action_fv1[ind]
        #print match_fv2[ind]
        if action_fv1[ind]=='*':
            continue
        elif action_fv1[ind]==match_fv2[ind]:
            overlap+=1
            conflict.append(ind)
    print conflict
    print overlap
    if overlap>0:
        log.info('Overlap detected in sequential composition, need to create a new rule')
    else:
        log.info('No Overlap, no new rule required')

    log.info('Composing two rules')

    return r

def main():


    r1=rule.rule()
    r1.match_dl_dst='b'
    r1.match_dl_src='c'
    r1.match_nw_dst=PREFIXES_A
    r1.action_dl_dst='a'
    r1.action_dl_src='b'


    r2=rule.rule()
    r2.match_dl_dst='a'
    r2.match_dl_src='b'
    r2.match_nw_dst="100.0.0.0/24"
    r2.action_dl_dst='a2'

    r = sequential_comp(r1,r2)

    print r

    """print r1.action.flow.dl_src

    f1=rule.flow()
    f1.dl_src='c'
    f1.dl_dst='b'
    f1.nw_dst=PREFIXES_A
    f2=rule.flow()
    f2.dl_src='b'
    f2.dl_dst='a'
    r1=rule.rule()
    r1.action.flow=f2
    r1.match.flow=f1
    print r1.action.flow.dl_dst

    f3=rule.flow()
    f3.dl_dst='a'
    f3.nw_dst="100.0.0.0/24"
    f4=rule.flow()
    f4.dl_dst='a2'
    r2=rule.rule()
    r2.action.flow=f4
    r2.match.flow=f3
    print r2.action.flow.dl_dst


    r = sequential_comp(r1,r2)

    print r"""



if __name__=="__main__":
    main()