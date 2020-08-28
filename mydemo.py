#!/usr/bin/env python3
# super simple discovery demo

import discoverhue


found = discoverhue.find_bridges()
for bridge in found:
    print('    Bridge ID {br} at {ip}'.format(br=bridge, ip=found[bridge]))
    print('        {ip}api/username/lights - for json'.format(ip=found[bridge]))

