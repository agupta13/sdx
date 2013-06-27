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

    def set_aflow(self,param1, param2):
        if param1=='in_port':
            flow.in_port = param2
        elif param1=='vlan':
            flow.vlan = param2
        elif param1=='dl_src':
            flow.dl_src = param2
        elif param1=='dl_dst':
            flow.dl_dst = param2
        elif param1=='dl_type':
            flow.dl_type = param2
        elif param1=='nw_src':
            flow.nw_src = param2
        elif param1=='nw_dst':
            flow.nw_dst = param2
        elif param1=='nw_proto':
            flow.nw_proto = param2
        elif param1=='tp_src':
            flow.tp_src = param2
        elif param1=='tp_dst':
            flow.tp_dst = param2

    def get_aflow(self,param1):
        if param1=='in_port':
            return flow.in_port
        elif param1=='vlan':
            return flow.vlan
        elif param1=='dl_src':
            return flow.dl_src
        elif param1=='dl_dst':
            return flow.dl_dst
        elif param1=='dl_type':
            return flow.dl_type
        elif param1=='nw_src':
            return flow.nw_src
        elif param1=='nw_dst':
            return flow.nw_dst
        elif param1=='nw_proto':
            return flow.nw_proto
        elif param1=='tp_src':
            return flow.tp_src
        elif param1=='tp_dst':
            return flow.tp_dst

class match(flow):
    mflow=flow()

    def __init__(self,flow=flow()):
        #self.flow=flow
        log.info('action object created')

    def set_mflow(self,param1, param2):
        if param1=='in_port':
            flow.in_port = param2
        elif param1=='vlan':
            flow.vlan = param2
        elif param1=='dl_src':
            flow.dl_src = param2
        elif param1=='dl_dst':
            flow.dl_dst = param2
        elif param1=='dl_type':
            flow.dl_type = param2
        elif param1=='nw_src':
            flow.nw_src = param2
        elif param1=='nw_dst':
            flow.nw_dst = param2
        elif param1=='nw_proto':
            flow.nw_proto = param2
        elif param1=='tp_src':
            flow.tp_src = param2
        elif param1=='tp_dst':
            flow.tp_dst = param2

    def get_mflow(self,param1):
        if param1=='in_port':
            return flow.in_port
        elif param1=='vlan':
            return flow.vlan
        elif param1=='dl_src':
            return flow.dl_src
        elif param1=='dl_dst':
            return flow.dl_dst
        elif param1=='dl_type':
            return flow.dl_type
        elif param1=='nw_src':
            return flow.nw_src
        elif param1=='nw_dst':
            return flow.nw_dst
        elif param1=='nw_proto':
            return flow.nw_proto
        elif param1=='tp_src':
            return flow.tp_src
        elif param1=='tp_dst':
            return flow.tp_dst

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

    def __init__(self):

        """self.rid=rid
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