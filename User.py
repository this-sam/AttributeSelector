#User contains a events and a Survey so that they can be easily related
#to their data

class User:
	
	global Event
	from Event import Event
	
	EVENT_TYPES = ['tim', 'stt', 'bkb', 'bka', 'snd']
	USERNAME_MAPPINGS = {'A':'B', 'B':'A', 'C':'D', 'D':'C'}
	
	def __init__(self, eventString, survey):
		"""Initialize user class
		
		Keyword arguments:
		fname -- the name of the text file containing the users events
		survey -- a survey object containing the user responses to the survey
		
		"""
		
		#TOO MUCH MEMORY WTF!
		self.events, self.lookupTables = self.__loadEventsFromFile(eventString)
		self.eventString = eventString
		self.survey = survey
		self.username = survey.username
		self.partner = self.__findPartner()
		self.classification = self.__findClassification()


#===============================================
#--------------Private Functions----------------
	def __loadEventsFromFile(self, eventString):
		"""Create an array of events from the user's message file.
	
		Keyword arguments:
		fname -- the name of the text file containing the users events
		
		Return values:
		events -- array containing each event, in chronological order
		lookupTable -- assoc array of 'event type' => array.  Each array contains
		indexes into events array to rapidly retrieve all events of that type
		"""
		
		events = []
		lookupTables ={}

		#load events into array
		for line in eventString:
			events.append(Event(line))
		
		#prepare lookupTables with defined event types
		for type in User.EVENT_TYPES:
			lookupTables[type] = []
		
		#create the arrays in the lookupTable
		for i in range(len(events)):
			lookupTables[events[i].type].append(i)
			
		return events, lookupTables
			
	def __findPartner(self):
		classification, sep, suffix = self.username.partition('_')
		return User.USERNAME_MAPPINGS[classification]+sep+suffix
		
	def __findClassification(self):
		classification, sep, suffix = self.username.partition('_')
		return classification
			
