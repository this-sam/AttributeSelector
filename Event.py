#Many types of events are contained during a conversation.  This class makes it
#easier to determine which type of event, etc.

class Event:
	def __init__(self, rawString):
		self.type = "bkb"
		self.rawString = rawString