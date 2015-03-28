class Sign(object):

	def __init__(self):
		self.data = "pxlpong init..."
		self.dirty = False

		print "Sign init"

	def set(self, text):
		self.data = text
		self.dirty = True

