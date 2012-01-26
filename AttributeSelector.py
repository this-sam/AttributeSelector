#==========================================================
#TODO:
#	-- Make a globals class so that I can globally set debug, parameters
#	-- Lots of other things that i won't forget because i need to do them
#  -- Look into measuring where in the sentence the word is located that is edited
#      --> statistical analysis on sentences... from twitter, etc.?  db of
#			  messenger convos?





class AttributeSelector:
	
	global pprint
	import os, pprint
	
	global Survey, User, Chat, Settings
	from Survey import Survey
	from Settings import Settings
	from User import User
	from Chat import Chat
	
	def __init__(self):
		"""Initialize AttributeSelector Class
		
		More to come...
		
		"""
		#log errors
		self.errors = []
		
		#get input files
		#store files in dictionary --> USERNAME =>
		self.surveyFiles, self.userFiles = self.__getFiles()
		
		self.chats = self.__makeChats()
		
		if Settings.DEBUG:
			self.__debug()

#===============================================
#--------------Public  Functions----------------

		def printFeatures(self):
			featureVectors = []			
			for chat in self.chats:
				chat.userA.selectFeatures()
				featureVectors.append(chat.userA.getFeatureVector())
				chat.userB.selectFeatures()
				featureVectors.append(chat.userB.getFeatureVector())
				
				
#===============================================
#--------------Private Functions----------------
	def __getFiles(self):
		"""Load message and survey files into separate arrays
		
		Return values:
			surveys -- a list of survey files
			userChats -- a list of conversations had by users
		"""
		surveyFiles = []
		userFiles = []
		
		#walk the file directory
		for dirpath, dirnames, filenames in AttributeSelector.os.walk(Settings.ROOT_DIR):
			for f in filenames:
				file = AttributeSelector.os.path.join(dirpath, f)
				
				#trim file name and search string
				file = file[len(Settings.ROOT_DIR):]
				fname = file[6:]

				#only add the correct files to the list
				if(fname[0:1] == "U"):
					userFiles.append(file)
				elif(fname[0:1] =="s"):
					surveyFiles.append(file)
					
		return surveyFiles, userFiles
	

	def __makeChats(self):
		"""Create conversations by loading users from survey and message files
		
		creates an array of chats
		"""
		surveys = []
		users = {}
		chats = []
		
		for surveyFile in self.surveyFiles:
			survey = open(Settings.ROOT_DIR + surveyFile, 'r')
			date = surveyFile.split('/')[0]
			
			#create a new Survey and user for each line in the survey file
			#add the users to a temporary array so that they can be added into chats
			tmpUsers = {}
			for line in survey:
				surveys.append(Survey(line))
				userFile = surveys[-1].getUserFilename()
				userFName = Settings.ROOT_DIR+date+'/'+userFile
				userEventString = open(userFName, 'r').read()
				user = User(userEventString, surveys[-1])
				tmpUsers[user.index] = user
				
			#pair users and create chats	
			for username, user in tmpUsers.iteritems():
				if ((user.classification == 'A') or (user.classification == 'C')):
					chats.append(Chat(user, tmpUsers[user.partnerIndex]))
		
		return chats			


	def __debug(self):
		print "Dumping Object AttributeSelector"
		pprint.pprint(self.surveyFiles)
		pprint.pprint(self.userFiles)
		pprint.pprint(self.errors)


	

if __name__ == '__main__':
	selector = AttributeSelector()
	 
	 
	 
