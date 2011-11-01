#User contains a events and a Survey so that they can be easily related
#to their data

class User:
	
	global Event, Settings
	from Event import Event
	from Settings import Settings
	
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
		self.index = self.username[0:-3]
		self.partnerIndex = self.__findPartnerIndex()
		self.classification = self.__findClassification()
		
		if Settings.DEBUG:
			self.__debug()
		
		


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
		
		lines = eventString.split('[end]')

		#load events into array
		for line in lines:
			if (len(line) > 34):
				events.append(Event(line.strip()))
		
		#prepare lookupTables with defined event types
		for type in Settings.EVENT_TYPES:
			lookupTables[type] = []
		
		#create the arrays in the lookupTable
		for i in range(len(events)):
			lookupTables[events[i].type].append(i)
			
		return events, lookupTables
			
	def __findPartnerIndex(self):
		classification, sep, suffix = self.username.partition('_')
		return (Settings.USERNAME_MAPPINGS[classification]+sep+suffix)[0:-3]
		
	def __findClassification(self):
		classification, sep, suffix = self.username.partition('_')
		return classification
			
	def __debug(self):
		print "Dumping Object User"
		print self.username