#!/usr/bin/env python3

import subprocess
import optparse
import re

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest = 'interface', help = 'Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest = 'newMac', help = 'New MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('> Please specify the interface, use --help for more information.')
    if not options.newMac:
        parser.error('> Please specify the new MAC address, use --help for more information.')
    return options

def changeMac(interface, newMac):
    print('> Changing MAC address for {} to {}'.format(interface, newMac))
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', newMac])
    subprocess.call(['ifconfig', interface, 'up'])

def getCurrentMac(interface):
    ifconfigResult = subprocess.check_output(['ifconfig', interface])
    macSearch = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfigResult))
    if macSearch:
        return macSearch.group(0)
    else:
        print('> Could not read MAC address')

options = getArguments()

currentMac = getCurrentMac(options.interface)
print('> Current MAC Address: {}'.format(currentMac))

changeMac(options.interface, options.newMac)

currentMac = getCurrentMac(options.interface)
if currentMac == options.newMac:
    print('> MAC address was successfully changed to {}'.format(currentMac))
else:
    print('> MAC address change failed. Try again.')