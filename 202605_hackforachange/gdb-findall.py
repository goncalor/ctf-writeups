class FindAll(gdb.Command):
	def __init__(self):
		super(FindAll, self).__init__("findall", gdb.COMMAND_USER, gdb.COMPLETE_EXPRESSION)
	
	def invoke(self, arg, from_tty):
		# arg = int(gdb.parse_and_eval('(unsigned long long)('+arg+')'))
		lines = gdb.execute("info proc mappings", from_tty, True).split('\n')
		header = ''
		foundStart = False
		for line in lines:
			if foundStart and '0x' in line:
				fields = line.split()
				start = int(fields[0], 16)
				end   = int(fields[1], 16)

				cmd = f"find {start}, {end}, {arg}"
				print(cmd)
				lines = gdb.execute(cmd, from_tty, True)
				print(lines)
			elif 'Start Addr' in line and 'End Addr' in line:
				foundStart = True
				header = line

FindAll()
