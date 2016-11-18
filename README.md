
# Create a default network available in mininet
sudo mn

hosts -> h1, h2
links -> (h1,s1), (h2,s1)

switch -> s1
controller -> c0

# Check all interfaces are correct
h1 ifconfig
h2 ifconfig
s1 ifconfig

pingall ## will ping all the hosts

h1 and h2 are shared hosts within the mininet environment

