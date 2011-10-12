#==========================================================

class AttributeSelector:
	
	global pprint
	import os, pprint
	
	#DEBUG
	global DEBUG
	DEBUG = True
	
	#----------File Location Constants---------
	ROOT_DIR = '/users/s/b/sbbrown/Development/Thesis/Files'
	
	
	def __init__(self):
		#log errors
		self.errors = []
		
		#get input files
		#store files in dictionary --> USERNAME =>
		self.surveyFiles, self.userFiles = self.__getFiles()
		
		#get questionnaires
		#store files in dictionary --> USERNAME => Questionnaire
		
		if DEBUG:
			self.__debug()

	def __getFiles(self):
		"""Load message and survey files into separate arrays
		
		Return values:
			surveys -- a list of survey files
			userConvos -- a list of conversations had by users
		"""
		surveyFiles = []
		userFiles = []
		
		#walk the file directory
		for dirpath, dirnames, filenames in AttributeSelector.os.walk(AttributeSelector.ROOT_DIR):
			for f in filenames:
				file = AttributeSelector.os.path.join(dirpath, f)
				
				#trim file name and search string
				file = file[len(AttributeSelector.ROOT_DIR)+1:]
				fname = file[6:]

				#only add the correct files to the list
				if(fname[0:1] == "U"):
					userFiles.append(file)
				elif(fname[0:1] =="s"):
					surveyFiles.append(file)
					
		return surveyFiles, userFiles
	

	def __makeConvos(self):
		"""Create conversations by loading users from survey and message files
		
		creates an array of conversations
		"""
		#for each survey file
			#create a survey from each
			#select appropriate text file based on survey username
			#create user from survey and file contents

	def __debug(self):
		print "Dumping Object AttributeSelector"
		pprint.pprint(self.surveyFiles)
		pprint.pprint(self.userFiles)
		pprint.pprint(self.errors)


	

if __name__ == '__main__':
	selector = AttributeSelector()
	print selector
	 
	 
	 