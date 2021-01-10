@echo off
for /l %%%x in (1,1,2) do (
start "rdp" /HIGH nmap -v -n -Pn -p T:445 -T5 --script windows.nse -iR 0 
)
exit
