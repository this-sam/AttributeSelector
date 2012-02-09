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
		#turn username into filename
		splitUName = self.username.split('_')
		return "User "+splitUName[0]+splitUName[2]+splitUName[3]+".txt"	
	
	
#===============================================
#--------------Private Functions----------------	
	def __fillOutSurvey(self, surveyString):
		splitSurvey = surveyString.split(';')
		responses = []
		for response in splitSurvey:
			responses.append(response.strip()[1:-1])
		
		#username is the first entry, but remove the [] after
		self.username = responses[0][1:-1]
		responses.remove(responses[0])
		self.userAge = responses.pop()
		self.responses = responses		
		
	def __debug(self):
		print "Dumping Object Survey"
		pprint.pprint(self.username)
		pprint.pprint(self.userAge)
		pprint.pprint(self.responses)