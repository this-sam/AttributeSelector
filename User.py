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
		#=======================================================
		#INITIALIZE USER VARIABLES:	#+ --> feature implemented
		self.username = ""				#+
		self.classification = ""		#+
		self.orientation = ""			#-	(S/G)
		self.gender = ""					#-
		self.numMessages = -1			#+
		
		#load events
		self.events, self.eventLookupTables = self.__loadEventsFromFile(eventString)
		self.eventString = eventString
		
		#load user information, survey
		self.survey = survey
		self.username = survey.username
		self.index = self.username[0:-3]
		self.partnerIndex = self.__getPartnerIndex()
		self.classification = self.__getClassification()
		self.orientation = self.__getOrientation()
		self.gender = self.__getGender()
		
		#load messages from events
		self.messages, self.messageLookupTables = self.__loadMessagesFromEvents()
		
		#=============================
		#Begin setting user variables:
		self.allFeatures = ['username', 'index', 'orientation', 'gender', 'numMessages', 'numEvents',\
								  'avgCompositionTime',\
							     'avgCompositionDelay', 'avgTotalEvents', 'avgSendDelay', 'avgDeletions',\
							     'avgDeletedChars','avgMessageLength','avgMessageWords','avgMessageChars',\
							     'avgCharsPerMin','avgWordsPerMin', 'ratioSent']
		
		self.lastFeatureSet = self.allFeatures
		
		self.numMessages = len(self.messages)
		self.numEvents = len(self.events)
		
		self.avgCompositionTime = self.__averageMessageAttribute("compositionTime")
		#print "avgCompTime", self.__averageMessageAttribute("compositionTime")
		self.avgCompositionDelay = self.__averageMessageAttribute("compositionDelay")
		#print "avgCompDelay", self.avgCompositionDelay
		self.avgTotalEvents = self.__averageMessageAttribute("totalEvents")
		#print "avgTotalEvents/Msg", self.avgTotalEvents
		self.avgSendDelay = self.__averageMessageAttribute("sendDelay")
		#print "avgSendDelay", self.avgSendDelay
		
		self.avgDeletions = self.__averageMessageAttribute("totalDeletions")
		#print "avgtotalDeletions", self.avgDeletions
		self.avgDeletedChars = self.__averageMessageAttribute("totalDeletedChars")
		#print "avgtotalDeletedChars", self.avgDeletedChars
		self.avgMessageLength = self.__averageMessageAttribute("finalLength")
		#print "avgfinalLength", self.avgMessageLength
		self.avgMessageWords = self.__averageMessageAttribute("totalWords")
		#print "avgtotalWords", self.avgMessageWords
		self.avgMessageChars = self.__averageMessageAttribute("totalChars")
		#print "avgtotalChars", self.avgMessageChars
		
		self.avgCharsPerMin = self.__averageMessageAttribute("charsPerMin")
		#print "charspermin: ", self.avgCharsPerMin
		self.avgWordsPerMin = self.__averageMessageAttribute("wordsPerMin")
		#print "wordspermin: ", self.avgWordsPerMin
		
		self.ratioSent = len(self.messageLookupTables['sent'])/float(len(self.messageLookupTables['unsent']))
		#print "ratiosent:", self.ratioSent
		
		#=============== 
		#SELECT FEATURES 
		self.featureVector = self.selectFeatures(self.allFeatures)
		
		if Settings.DEBUG:
			self.__debug()
		

#===============================================
#-------------------Getters---------------------
	def selectFeatures(self, features):
		"""for each feature in the features (list of strings which represent variable names
		within the class), select the variable and add it to a the feature vector."""
		featureVector = []
		for feature in features:
			#check types:
			if not hasattr(self, feature):
				raise Exception("User does not have feature "+feature)

			if type(vars(self)[feature]) == datetime.timedelta:
				seconds, microseconds = vars(self)[feature].seconds, vars(self)[feature].microseconds
				seconds += microseconds/1000000.
				featureVector.append(seconds)
			else:
				featureVector.append(vars(self)[feature])
				
		self.lastFeatureSet = features
		return featureVector

	def getFeatureSet(self):
		return self.lastFeatureSet
		
		
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
			
		#if it's an int, turn it into a float so we don't lose accuracy when we average
		if (type(total) is int):
			total = float(total)
			
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
				
				#now this event was the last message sent
				lastSnd = event.timestampAsDatetime
			
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

	def __getPartnerIndex(self):
		classification, sep, suffix = self.username.partition('_')
		return (Settings.USERNAME_MAPPINGS[classification]+sep+suffix)[0:-3]
		
	def __getClassification(self):
		classification, sep, suffix = self.username.partition('_')
		return classification
	
	def __getOrientation(self):
		return Settings.ORIENTATION_MAPPINGS[self.classification]
		
	def __getGender(self):
		return Settings.GENDER_MAPPINGS[self.classification]
			
	def __debug(self):
		print "Dumping Object User"
		print self.username
