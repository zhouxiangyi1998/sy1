"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )
        Host7 = self.addHost( 'h7' )
        Host8 = self.addHost( 'h8' )
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
	Switch5 = self.addSwitch( 's5' )
        Switch6 = self.addSwitch( 's6' )
	Switch7 = self.addSwitch( 's7' )

        # Add links
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch2, Switch4 )
        self.addLink( Switch2, Switch5 )
        self.addLink( Switch3, Switch6 )
        self.addLink( Switch3, Switch7 )
        self.addLink( Switch4, Host1 )
        self.addLink( Switch4, Host2 )
        self.addLink( Switch5, Host3 )
        self.addLink( Switch5, Host4 )
        self.addLink( Switch6, Host5 )
        self.addLink( Switch6, Host6 )
        self.addLink( Switch7, Host7 )
	self.addLink( Switch7, Host8 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
