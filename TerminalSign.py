from Sign import Sign

class TerminalSign(Sign):
	def __init__(self):
		super(TerminalSign, self).__init__()
		print "TerminalSign init"

	def update(self):
		print self.data
		self.dirty = False


