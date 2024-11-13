#! python
# FUNCTION: automaticaly update all existing pip-managed python extentions
#  Written for Python 3.6.5 (latest)  *** YOU HAVE BEEN WARNED! ***
import subprocess
import json

def banner():
	print( r'╔═══════════════════════════════════════════════════════════════════════════════════════════════╗' )
	print( r'║     ____  _      _          ___         __              __  __          __      __            ║' )
	print( r'║    / __ \(_)___ ( )_____   /   | __  __/ /_____        / / / /___  ____/ /___ _/ /____  _____ ║' )
	print( r'║   / /_/ / / __ \|// ___/  / /| |/ / / / __/ __ \______/ / / / __ \/ __  / __ `/ __/ _ \/ ___/ ║' )
	print( r'║  / ____/ / /_/ / (__  )  / ___ / /_/ / /_/ /_/ /_____/ /_/ / /_/ / /_/ / /_/ / /_/  __/ /     ║' )
	print( r'║ /_/   /_/ .___/ /____/  /_/  |_\__,_/\__/\____/      \____/ .___/\__,_/\__,_/\__/\___/_/      ║' )
	print( r'║        /_/                                               /_/                                  ║' )
	print( r'╚═══════════════════════════════════════════════════════════════════════════════════════════════╝' )
	print()

# Pip Wrappers
def update_pip():
	pipres = subprocess.run( ['python', '-m', 'pip', 'install', '--upgrade', 'pip'] )
	
def update( *packages ):
	pipres = subprocess.run( ['pip', 'install', '--upgrade', *packages] )

def outdated():
	pipres = subprocess.run( ['pip', 'list', '--format=json', '--outdated'], stdout=subprocess.PIPE )
	ppacks = json.loads( pipres.stdout )
	if len( ppacks ) > 0:
		# Filter to names only
		return [ pack["name"] for pack in ppacks ]
	else:
		return None

# !!! THIS IS NOT A LIBRARY !!!
#   Force te code to run as an independent program or not at all
if __name__ != "__main__":
	exit(1)
	
# Displey Banner
banner()

# Get list of outdated modules (1st time)
wip = outdated()

if wip is None:
	print( "Pip packages all up-to-date." )
else:
	# Update Pip if nessesary
	if "pip" in wip:
		update_pip()
		
		# Get list of outdated modules (2nd time)
		wip = outdated()

	# Run Updates
	if wip is not None:
		update( *wip )

# Wait for User Acknowledge
print()
input( "Press Enter to continue..." )

# #############################################################################
# _________ .__                                   .____                      
# \_   ___ \|  |__ _____    ____    ____   ____   |    |    ____   ____   /\ 
# /    \  \/|  |  \\__  \  /    \  / ___\_/ __ \  |    |   /  _ \ / ___\  \/ 
# \     \___|   Y  \/ __ \|   |  \/ /_/  >  ___/  |    |__(  <_> ) /_/  > /\ 
#  \______  /___|  (____  /___|  /\___  / \___  > |_______ \____/\___  /  \/ 
#         \/     \/     \/     \//_____/      \/          \/    /_____/      
#
# 2018-04-26:
#   Maurolepis Dreki: (16:43 UTC)
#      Engineered possable Long-Term Solution to Pip package management;
#        the problem with Pip is that there's no way to automaticaly mass-update all installed packages.
#      This solution is an improvement on a shell-script hack I've use before and lost,
#        may this improved verson not meet the same fate...
#
# 2018-07-23:
#   Maurolepis Dreki: (14:11 UTC)
#     Fixed the update_pip() routine -- the subprocess command was identical to update()'s when
#       it's sole purpose is to update pip
#
# 2024-05-21:
#  Maurolepis Dreki:
#    Fix: Updated Python string literals for header
