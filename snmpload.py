# Command line application
import socket
import sys

from pysnmp.hlapi import *

from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI

net = Mininet(SingleSwitchTopo(2))

def mininet_start_nodes(net):
    validated = false
    net.start()
    pingResults = net.pingAll()
    if(pingResults.find('100% dropped') & pingResults.find('100.0')):
        validated = true 
    if(validated):
        return net.values()
    return 0


def mininet_snmp_load(host, community, objectID):
    g = getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget(('demo.snmplabs.com', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

    next(g)

nodes = mininet_start_nodes(net)
if(nodes):
    for node in nodes:
        print PyEval_GetFuncName(node)





net.stop()