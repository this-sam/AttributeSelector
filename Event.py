#===============================================================================
#
# Event.py by Sam Brown
#
# Many types of events are contained during a conversation.  The Event class
# handles categorization of the event as well as extracting certain metrics or
# features.
#
#===============================================================================


class Event:
	
	global Settings, datetime, string
	from Settings import Settings
	from datetime import datetime

	
	def __init__(self, rawString):
		"""Load raw string of event, calculate all attributes based on raw string."""
		self.rawString = rawString
		splitString = self.rawString.split(',', 5)
		
		#INITIALIZE EVENT VARIABLES:	#+ --> feature implemented
		self.type = ""					#+ what type of event (list in Settings.py)
		self.username = ""				#+ username of person who caused event
		self.text = ""					#+ text in text box during event
		self.timestamp = ""				#+ timestamp of when event took place
		
		self.timestampAsDatetime = -1	#+ save the timestamp as a python datetime object
		
		self.isEmpty = False			#+ is there text?
		self.length = -1				#+ total length of text
		self.numChars = -1				#+ total characters in text box during event
		self.numWords = -1				#+ total number of "words" (sep by spaces)
		self.avgWordLen = -1			#+ average length of words (no punctuation)
		
		#begin to set event attributes
		self.username = splitString[0].strip()
		self.timestamp = splitString[1].strip()
		self.type = splitString[2].strip()
		self.text = splitString[3].strip()
		
		self.timestampAsDatetime = self.convertTimestamp(self.timestamp)
		
		#calculate anything dependent on dividing by text length
		self.length = len(self.text)
		self.isEmpty = (self.length==0)
		if (self.isEmpty == False):
			self.numChars = self.getNumChars()
			self.numWords = self.getNumWords()
			if self.numWords != 0:
				self.avgWordLen = self.numChars/self.numWords
			else:
				self.avgWordLen = 0
			
		
		if Settings.DEBUG:
			self.__debug()


#---------------------------------------------
# Getter functions
	
	def getAvgWordLength(self):
		"""Calculate average word length in event."""
		s = self.text
		s = s.lower()
		ct = s.count('x')
		numWords = getNumWords()
		avgWordLength = ct/numWords
		return avgWordLength

	def getNumChars(self):
		"""Calculate number of characters in event."""
		strippedText = self.text.replace(" ", "")
		return len(strippedText)
		
	def getNumWords(self):
		"""Calculate number of words in event text."""
		s = self.text
		s = s.lower()
		numWords = 0
		for substr in s.split(" "): #REPLACE WITH REGEX FOR PUNCTUATION AND SPACES
			ct = substr.count('x')
			if ct > 0:
				numWords += 1
		return numWords
	
	def convertTimestamp(self, timestamp):
		"""Convert a timestamp from the message into a python timestamp."""
		splitTimestamp = timestamp.split(" ")
		date = splitTimestamp[0]
		time = splitTimestamp[1]
		
		splitDate = date.split("-")
		year, month, day = int(splitDate[0]), int(splitDate[1]), int(splitDate[2])
		
		splitTime = time.split(":")
		hours, minutes = int(splitTime[0]), int(splitTime[1])
		seconds, miliseconds = int(splitTime[2].split(".")[0]), int(splitTime[2].split(".")[1])
		
		convertedTimestamp = datetime(year, month, day, hours, minutes, seconds, miliseconds*1000)
		return convertedTimestamp
	
	
	def __debug(self):
		"""Print all variables contained in Event."""
		print "Dumping Object Event"
		print self.rawString
		print "USER:\n\t"+self.username
		print "TYPE:\n\t"+self.type
		print "TEXT:\n\t"+self.text
		print "TIME:\n\t",self.timestampAsDatetime
		print "BOOLEANS:"
		print "\tisEmpty:", self.isEmpty
		print "CALCULATED:"
		print "\tnumChars:", self.numChars
		print "\tnumWords:", self.numWords
		print "\tavgWordLen:", self.avgWordLen
		
if __name__ == '__main__':
	#testing an event string
	string = "A_01_4_02, 2011-09-29 21:37:28.291, snd, xxx x xxxxx xxx xxxxxxxx"
	event = Event(string)
	
	

