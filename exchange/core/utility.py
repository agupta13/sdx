__author__ = 'arpit'
import rule_sdx as rule
p2m={'asB':'08:00:27:8b:5e:11','asA':'08:00:27:b3:39:3a','asC':'08:00:27:6a:fd:10'}
m2p={'08:00:27:8b:5e:11':'asB','08:00:27:b3:39:3a':'asA','08:00:27:6a:fd:10':'asC'}

PREFIXES_A = ["100.0.0.0/24", "110.0.0.0/24", "120.0.0.0/24"]
PREFIXES_B=[]
PREFIXES_C=[]

p2n={'asB':PREFIXES_B,'asA':PREFIXES_A,'asC':PREFIXES_A}


def player_to_mac(player):
    return p2m[player]

def mac_to_player(mac):
    return m2p[mac]

def player_to_nw(player):
    return p2n[player]

