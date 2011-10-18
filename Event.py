#Many types of events are contained during a conversation.  This class makes it
#easier to determine which type of event, etc.

class Event:
	
	global Settings
	from Settings import Settings
	
	def __init__(self, rawString):
		self.type = "bkb"
		self.rawString = rawString
		splitString = self.rawString.split(',', 5)
		
		self.username = splitString[0].strip()
		self.timestamp = splitString[1].strip()
		self.type = splitString[2].strip()
		self.text = splitString[3].strip()
		
		if Settings.DEBUG:
			self.__debug()
		
	
	def __debug(self):
		print "Dumping Object Event"
		print self.rawString