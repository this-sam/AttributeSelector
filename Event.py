#Many types of events are contained during a conversation.  This class makes it
#easier to determine which type of event, etc.

class Event:
	
	global Settings
	from Settings import Settings
	
	def __init__(self, rawString):
		self.type = "bkb"
		self.rawString = rawString
		splitString = self.rawString.split(',', 5)
		
		
		#event attributes
		self.username = splitString[0].strip()
		self.timestamp = splitString[1].strip()
		self.type = splitString[2].strip()
		self.text = splitString[3].strip()
		
		if Settings.DEBUG:
			self.__debug()


#---------------------------------------------
#Getter functions!
#getters will either calculate a value, or return the calculated
#value if the field has already been calculated.
#
# TODO: Define them as variables to access
	
	def getAvgWordLength(self):
		s = self.text
		s = string.lower(s)
		ct = s.count('x')
		numWords = getNumWords()
		avgWordLength = ct/numWords
		
		
	def getEmoticons(self):
		pass
	
	def getLength(self):
		pass

	def getNumWords(self):
		#remove punctuation
		#split
		#divide ct by number of words
		pass
	
	def getPunctuation(self):
		pass
	
	def getSentenceType(self):
		#exclamation, question, response, incomplete? ==> research
		pass
	
			
	
	
	def __debug(self):
		print "Dumping Object Event"
		print self.rawString