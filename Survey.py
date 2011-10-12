#Survey contains the list of a user's particular responses to the survey

class Survey:
	
	def __init__(self, surveyString):
		"""Initialize Survey class
			
		Keyword arguments:
		surveyString -- a line from the survey file, from which the survey inftializes all values
		
		"""
		self.__fillOutSurvey(surveyString)
	
	def __fillOutSurvey(self, surveyString):
		pass