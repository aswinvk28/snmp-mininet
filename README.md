
# MININET TOPOLOGY SETUP

> topology.py
> snmpload.py

# Create a default network available in mininet
sudo mn

## Network Information

hosts -> h1, h2

Hosts are connected through switches
------------------------------------

links -> (h1, s1), (h2, s1)

switch -> s1
controller -> c0

# Check all interfaces are correct

These are the command to check if the interfaces are correct (linux commands).

> h1 ifconfig
> h2 ifconfig
> s1 ifconfig

> pingall ## will send a ping request on all the hosts

h1 and h2 are shared hosts within the mininet environment

