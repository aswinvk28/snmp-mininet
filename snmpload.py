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
    validated = False
    net.start()
    pingResults = net.pingAll()
    if(pingResults.find('100% dropped') & pingResults.find('100.0')):
        validated = True
    if(validated):
        return net.values()
    return 0


def mininet_snmp_load(host, community, objectID):
    g = getCmd(SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', objectID, 0)))

nodes = mininet_start_nodes(net)
if(nodes):
    for node in nodes:
        mininet_snmp_load(node, community='public', objectID='sysDesc')





net.stop()
sys.exit(0)