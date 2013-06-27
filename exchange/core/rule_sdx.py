__author__ = 'arpit'

import logging as log
log.basicConfig(filename='sdx.log',level=log.DEBUG)

class flow():
    def __init__(self, in_port='*',vlan='*',dl_src='*',dl_dst='*',dl_type='*',
                 nw_src='*',nw_dst='*',nw_proto='*',tp_src='*',tp_dst='*'):
        self.in_port=in_port
        self.vlan=vlan
        self.dl_src=dl_src
        self.dl_dst=dl_dst
        self.dl_type=dl_type
        self.nw_src=nw_src
        self.nw_dst=nw_dst
        self.nw_proto=nw_proto
        self.tp_src=tp_src
        self.tp_dst=tp_dst
        log.info('Flow vector object created')

class action(flow):
    aflow=flow()

    def __init__(self,flow=flow()):

        #self.flow=flow
        log.info('match object created')


class match(flow):
    mflow=flow()

    def __init__(self,flow=flow()):
        #self.flow=flow
        log.info('action object created')


class rule(match,action):
    rid=1,
    ofsid=0
    priority=0
    raw=''
    #match=match()
    #action=action()
    owner=''
    classifier=''
    compseq=''
    # match parameters
    match_in_port='*'
    match_vlan='*'
    match_dl_src='*'
    match_dl_dst='*'
    match_dl_type='*'
    match_nw_src='*'
    match_nw_dst='*'
    match_nw_proto='*'
    match_tp_src='*'
    match_tp_dst='*'

    # action parameters
    action_in_port='*'
    action_vlan='*'
    action_dl_src='*'
    action_dl_dst='*'
    action_dl_type='*'
    action_nw_src='*'
    action_nw_dst='*'
    action_nw_proto='*'
    action_tp_src='*'
    action_tp_dst='*'


    def __init__(self):

        """match_rid=rid
        self.match=match
        self.action=action
        self.ofsid=ofsid
        self.priority=priority
        self.raw=raw
        self.owner=owner
        self.classifier=classifier
        self.compseq=compseq"""
        log.info('policy object created')

    def debug_display_rule(self):
        log.info('Rule id: %d', self.rid)