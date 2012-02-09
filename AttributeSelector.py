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
		print self.surveyFiles
		
		self.chats = self.__makeChats()
		self.featureVectors = self.getFeatureVectors()
		
		#make sure we loaded files
		if len(self.chats) > 0:
			self.featureSet = self.chats[0].userA.getFeatureSet()
			self.printToCSV(self.featureVectors, self.featureSet)
		else:
			print "No chat files could be found."
		
		if Settings.DEBUG:
			self.__debug()

#===============================================
#--------------Public  Functions----------------

	def getFeatureVectors(self):
		featureVectors = []			
		for chat in self.chats:
			featureVectors.append(chat.userA.featureVector)
			featureVectors.append(chat.userB.featureVector)
		return featureVectors
	

	def printToCSV(self, featureVectors, featureSet, withHeader=True, overwrite=True):
		if overwrite:
			f = open("Features.csv", 'w')
		else:
			f = open("Features.csv", 'a')
		
		if withHeader:
			for heading in featureSet:
				f.write(heading+",")
			f.write("\r\n")
		
		for vector in featureVectors:
			row = ""
			for element in vector:
				row+=str(element)+","
			f.write(row+"\r\n")
		f.close()
		
			
			
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
	 
	 
	 
