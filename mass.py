import os,sys
file = open(sys.argv[1]).read().splitlines()
for line in file:
	line = line.split(':')
	try:
		os.system('python3 zer0dump.py ' + line[0])
		pass
	except KeyboardInterrupt:
		pass
