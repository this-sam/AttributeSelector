#User contains a events and a Survey so that they can be easily related
#to their data

class User:
	
	global Event, Settings, Message, datetime, time
	from Event import Event
	from Settings import Settings
	from Message import Message
	import datetime
	import time
	
	def __init__(self, eventString, survey):
		"""Initialize user class
		
		Keyword arguments:
		fname -- the name of the text file containing the users events
		survey -- a survey object containing the user responses to the survey
		
		"""
		
		#INITIALIZE USER VARIABLES:	#+ --> feature implemented
		self.username = ""				#+
		self.classification = ""		#+
		self.orientation = ""			#-	(S/G)
		self.numMessages = -1			#+
		
		#load events
		self.events, self.eventLookupTables = self.__loadEventsFromFile(eventString)
		self.eventString = eventString
		
		#load user information, survey
		self.survey = survey
		self.username = survey.username
		self.index = self.username[0:-3]
		self.partnerIndex = self.__findPartnerIndex()
		self.classification = self.__findClassification()
		
		#load messages from events
		self.messages, self.messageLookupTables = self.__loadMessagesFromEvents()
		
		#Begin setting user variables:
		self.numMessages = len(self.messages)
		self.numEvents = len(self.events)
		
		self.avgCharsPerMin = self.__averageMessageAttribute("charsPerMin")
		self.avgWordsPerMin = self.__averageMessageAttribute("wordsPerMin")
		self.avgCompositionTime = self.__averageMessageAttribute("compositionTime")
		self.avgCompositionDelay = self.__averageMessageAttribute("compositionDelay")
		self.avgTotalEventsPerMessage = self.__averageMessageAttribute("totalEvents")
		#self.avgSendDelay = self.__averageMessageAttribute("sendDelay")
		
		self.ratioSent = None
		
		
		#===============
		#SELECT FEATURES 
		self.featureVector = self.selectFeatures
		
		if Settings.DEBUG:
			self.__debug()
		
		
	def selectFeatures():
		self.featureVector = []
	
	def getFeatureVector():
		return self.featureVector

#===============================================
#--------------Private Functions----------------
	def __averageMessageAttribute(self, attributeName):
		"""average a variable contained in messages by passing that variables
		name as a string ;)"""
		
		#just make sure it exists first
		if not attributeName in vars(self.messages[0]):
			exceptionString = "Attribute "+attributeName+" not found in object message."
			raise Exception(exceptionString)
			
		#and make sure we can do this stuff to it!
		if not type(vars(self.messages[0])[attributeName]) in [int, str, float, datetime.timedelta]:
			exceptionString = "Attribute "+attributeName+" cannot be averaged because it is of type "+str(type(vars(self.messages[0])[attributeName]))+"."
			raise Exception(exceptionString)
		
		#initialize total to whatever data type is stored in the message attribute
		total = vars(self.messages[0])[attributeName]
		
		#total all of that attribute
		for i in range(1, len(self.messages),1):
			total += vars(self.messages[i])[attributeName]

		#return the average, make sure it's a float for precision
		#correct for absent attributes (I don't know when this would happen but better safe than sorry)
		return total/len(self.messages)

	def __loadEventsFromFile(self, eventString):
		"""Create an array of events from the user's convo file.
	
		Keyword arguments:
		eventString -- string of file
		
		Return values:
		events -- array containing each event, in chronological order
		eventLookupTable -- assoc array of 'event type' => array.  Each array contains
		indexes into events array to rapidly retrieve all events of that type
		"""
		
		events = []
		eventLookupTables ={}
		
		lines = eventString.split('[end]')

		#load events into array
		for line in lines:
			if (len(line) > 34):
				events.append(Event(line.strip()))
		
		#prepare eventLookupTables with defined event types
		for type in Settings.EVENT_TYPES:
			eventLookupTables[type] = []
		
		#create the arrays in the lookupTable
		for i in range(len(events)):
			eventLookupTables[events[i].type].append(i)
			
		return events, eventLookupTables
	
	def __loadMessagesFromEvents(self):
		"""Create an array of events from the user's event array.
	
		Keyword arguments:
		nope.
		
		Return values:
		messages -- array containing each event, in chronological order
		messageLookupTables -- assoc array of 'event type' => array.  Each array contains
		indexes into messages array to rapidly retrieve all messages of that type (sent/unsent)
		"""
		messages = []
		messageLookupTables = {}
		messageLookupTables['sent'] = []
		messageLookupTables['unsent'] = []
		
		lastSnd = self.events[0].timestampAsDatetime;
		messageEvents = []
		messageDone = False
			
		#remove:
		print self.username
		
		for event in self.events:			
			#if the event is a send, the current message has no more events
			#or if the text box wasn't empty, and now is, samesies
			if (event.type == "snd" or event.isEmpty == True) and messageDone == False:
				lastSnd = event.timestampAsDatetime
				messageEvents.append(event)
				
				if Settings.DEBUG:
					print event.rawString
					
				thisMessage = Message(messageEvents)
				thisMessage.setTimeLastSent(lastSnd)
				messages.append(thisMessage)
				
				#log this message in the lookup table
				if event.type == "snd":
					messageLookupTables['sent'].append(len(messages)-1)
				else:
					messageLookupTables['unsent'].append(len(messages)-1)

				del messageEvents
				messageEvents = []
				messageDone = True
				
				if Settings.DEBUG:
					print "|||[ ",messages[-1].numEvents," events  ]|||"
					print "-----------------------------"
					time.sleep(.1)
			
			#not sure why this is necessary, but it makes it work.  manually set message
			#done to false for each empty event to make sure non-empty event is added
			elif event.isEmpty:
				messageDone = True
				
			#if the text box isn't empty, but it was empty, a new message is beginning
			elif (event.isEmpty == False and messageDone == True):
				messageDone = False
				if Settings.DEBUG:
					print self.username
					print "-----------------------------"
				
			#if the message isn't done, add the event to it
			if messageDone == False:
				messageEvents.append(event)
				
				if Settings.DEBUG:
					print event.rawString
				
			
		return messages, messageLookupTables

	def __findPartnerIndex(self):
		classification, sep, suffix = self.username.partition('_')
		return (Settings.USERNAME_MAPPINGS[classification]+sep+suffix)[0:-3]
		
	def __findClassification(self):
		classification, sep, suffix = self.username.partition('_')
		return classification
			
	def __debug(self):
		print "Dumping Object User"
		print self.username
