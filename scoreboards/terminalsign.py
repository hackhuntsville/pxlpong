from betabrite import Sign

class TerminalSign(Sign):
	def __init__(self):
		super(TerminalSign, self).__init__()
		print "TerminalSign init"

	def update(self):
		print self.data
		self.dirty = False

if __name__ == "__main__":

	sign = TerminalSign()
	sign.update()
	sign.set("Test String")
	sign.update()

