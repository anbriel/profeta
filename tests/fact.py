#!/usr/local/bin/python2.6
#
#

import sys
sys.path.append ("../lib")

import time

from profeta.variable  import *
from profeta.attitude  import *
from profeta.inference  import *
from profeta.action  import *
from profeta.lib  import *
from profeta.main import *


# ------------------------------------------------------------------------------
# {{{ The Beliefs
# ------------------------------------------------------------------------------

class fact(Reactor):
    pass

# ------------------------------------------------------------------------------
# }}}


# ------------------------------------------------------------------------------
# {{{ The Actions
# ------------------------------------------------------------------------------
class show(Action):

    def execute(self):
        print self[0]

# ------------------------------------------------------------------------------
# }}}

class KB(Sensor):

    def sense(self):
        print "KB is:", PROFETA.kb()
        e = raw_input ("Enter Number: ")
        return fact(e, 1)



def factorial():
    +fact(0, "X") >> [ show("X") ]
    +fact("N", "X") >> [ "Y = int(N) * int(X)", "N = int(N) - 1", +fact("N", "Y") ]





if __name__ == "__main__":

    PROFETA.start()
    PROFETA.add_sensor(KB())

    factorial()

    PROFETA.run()

