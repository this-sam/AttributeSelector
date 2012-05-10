#===============================================================================
#
# Survey.py by Sam Brown
#
# Contains all of a user's responses to the post-study questionnaire.  
#
#===============================================================================


#Survey contains the list of a user's particular responses to the survey

class Survey:
	
	global pprint
	import pprint
	
	global Settings
	from Settings import Settings
	
	def __init__(self, surveyString):
		"""Initialize Survey class
			
		Keyword arguments:
		surveyString -- a line from the survey file, from which the survey inftializes all values
		
		"""
		#=======================================================
		#INITIALIZE SURVEY VARIABLES:	#+ --> feature implemented
		self.username = ""
		self.userAge = 0
		self.responses = []
		
		self.__fillOutSurvey(surveyString)
		
		if Settings.DEBUG:
			self.__debug()
	
#===============================================
#--------------Public  Functions----------------		
	def getUserFilename(self):
		"""Appends text to username to produce the name of that user's log file."""
		#turn username into filename
		return self.username+".txt"	
	
	
#===============================================
#--------------Private Functions----------------	
	def __fillOutSurvey(self, surveyString):
		"""Sets the responses to each survey question."""
		splitSurvey = surveyString.split(';')
		responses = []
		for response in splitSurvey:
			responses.append(response.strip()[1:-1])
		
		#username is the first entry, but remove the [] after
		self.username = responses[0][1:-1]
		responses.remove(responses[0])

		#now the responses can be stored as integers
		for i in range(len(responses)):
			responses[i] = int(responses[i])
			
		self.userAge = responses.pop()
		self.responses = responses		
		
	def __debug(self):
		"""Outputs all variables contained in the Survey object."""
		print "Dumping Object Survey"
		pprint.pprint(self.username)
		pprint.pprint(self.userAge)
		pprint.pprint(self.responses)