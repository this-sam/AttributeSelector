#User contains a HalfConvo and a Survey so that they can be easily related
#to their data

class User:
	
	def __init__(self, fname, survey):
		"""Initialize user class
		
		Keyword arguments:
		fname -- the name of the text file containing the users events
		survey -- a survey object containing the user responses to the survey
		
		"""
		
		self.__loadEventsFromFile(fname)
		self.survey = survey
   
	def loadEventsFromFile(fname):
		"""Create an array of events from the user's message file.
	
		Keyword arguments:
		fname -- the name of the text file containing the users events
		
		"""
		return true
		