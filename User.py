#User contains a events and a Survey so that they can be easily related
#to their data

class User:
	
	def __init__(self, eventString, survey):
		"""Initialize user class
		
		Keyword arguments:
		fname -- the name of the text file containing the users events
		survey -- a survey object containing the user responses to the survey
		
		"""
		
		self.__loadEventsFromFile(eventString)
		self.survey = survey
   
	def __loadEventsFromFile(self, eventString):
		"""Create an array of events from the user's message file.
	
		Keyword arguments:
		fname -- the name of the text file containing the users events
		
		"""
		for line in eventString.split('\n'):
			print line
		
		return True
		