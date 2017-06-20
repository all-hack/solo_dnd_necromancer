
# for fucking colors
from pygments import highlight 
from pygments.lexers import PythonLexer
# from pygments.formatters import Terminal256Formatter not very nice colors
from pygments.formatters import TerminalFormatter
from pprint import pformat
def pprint_color(obj):
    print (highlight(pformat(obj), PythonLexer(), TerminalFormatter()))
#

import digitalocean
from wisp import Wisp
from party import Party
from guild import Guild




# pp = pprint.PrettyPrinter(indent=4)
# manager = digitalocean.Manager(token="48f44a588d0dd1f1652a47a057e40aecc889164009d52e448a92ac1876741919")
# my_droplets = manager.get_all_droplets()
# print(my_droplets)

guild = Guild(0)
party = guild.spawn_party(0, "green_secret")
# wisp = Wisp.spawn(party)
party.spawn_wisp()
party.spawn_wisp()
party.spawn_wisp()
wisp = party.wisps_list[0]


# print (inspect.getmembers(wisp))
print ("\nguild:")
pprint_color(vars(guild))
guild.parties_printNames()


print ("\nparty:")
print (party.guild.name)
# pprint_color(vars(party))
party.wisps_printNames()


print ("\nwisp:")
print (wisp.party.name)
pprint_color(vars(wisp))


print ()




























