#Survey contains the list of a user's particular responses to the survey

global DEBUG
DEBUG = False

class Survey:
	
	global pprint
	import pprint
	
	def __init__(self, surveyString):
		"""Initialize Survey class
			
		Keyword arguments:
		surveyString -- a line from the survey file, from which the survey inftializes all values
		
		"""
		self.__fillOutSurvey(surveyString)
		
		if DEBUG:
			self.__debug()
	
	
	def __fillOutSurvey(self, surveyString):
		splitSurvey = surveyString.split(';')
		responses = []
		for response in splitSurvey:
			responses.append(response.strip()[1:-1])
		
		#username is the first entry, but remove the [] after
		self.userName = responses[0][1:-1]
		responses.remove(responses[0])
		print self.userName
		self.userAge = responses.pop()
		self.responses = responses
	
	def getUserFilename(self):
		#turn username into filename
		splitUName = self.userName.split('_')
		return "User "+splitUName[0]+splitUName[2]+splitUName[3]+".txt"
		
		
	def __debug(self):
		print "Dumping Object Survey"
		pprint.pprint(self.userName)
		pprint.pprint(self.userAge)
		pprint.pprint(self.responses)
			
		