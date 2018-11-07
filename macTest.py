#!/usr/bin/env python3

import subprocess
avad = input('Wanted Interface: \n>>> ')
ally = input('Wanted MAC Address: \n>>> ')
print('[+] Changing MAC address for '+ avad +' to ' + ally)
subprocess.call('ifconfig '+ avad +' down', shell = True)
subprocess.call('ifconfig '+ avad +' hw ether ' + ally, shell = True)
subprocess.call('ifconfig '+ avad +' up', shell = True)

# Alright Ill try to explain what is going on better.


# Basically, if you want to change the mac (technically spoof but I dont want to confuse you any more than I have to) address, you type 3 commands into the console.

# We do this to shut down the interface so that we can edit it:
# ifconfig (This says that you want to change something to do with the networks) wlan0 (this is the nam eof the interface that im using, the wifi card) down (this turns it off so that we can edit it.)

# Then we do this to actually change it:
# ifconfig (Again) wlan0 (Again, specifying which interface we want to change) hw (Too complex and doesnt matter, just ignore it) ether (Same story as with hw) "new mac" (Whatever you want your new mac address to be)

# Finally we want to turn the interface back on, doing the same thing as shutting it down, but using "up" instead of "down"
# ifconfig wlan0 up


# You can see where in the subprocess.call lines we are putting in these commands but instead of wlan0 and the new mac address, its variables that substitute user input


# Basically this scripts just runs 3 commands, while asking which interface and what new mac you want. That way you dont have to type each of those commands on their own.
# You dont really have to understand any of that in order to reconize the security risk. All you really have to know is that the user is *putting in their own inputs* which gets *directly inserted* into the *commands getting send to the terminal*.
# And basically you can do anything in the terminal, which is why its always the hacker's first goal when breaking into a system, to get into command prompt or the terminal. From there they can do anything, including browsing files.