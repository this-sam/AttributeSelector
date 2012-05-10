#===============================================================================
# AttributeSelector by Sam Brown
#
# AttributeSelector is the "driver" class for the feature selection software written
# for my thesis.  Location of chat files and other settings may be changed in
# Settings.py.  To use this class, simply edit the settings file and then run
# AttributeSelector.py
#
#===============================================================================

class AttributeSelector:
	"""Parses through chat log files and survey results to create feature vectors."""
	global re, pprint
	import os, pprint, re
	
	global Survey, User, Chat, Settings
	from Survey import Survey
	from Settings import Settings
	from User import User
	from Chat import Chat
	
	def __init__(self):
		"""Load files, parse files into objects, print features to a csv file."""
		
		#get input files
		#store files in dictionary --> USERNAME =>
		self.surveyFiles, self.userFiles = self.__getFiles()
		print self.surveyFiles, self.userFiles
		
		self.chats = self.__makeChats()
		
		#make sure we loaded files
		if len(self.chats) > 0:
			#Write Message Feature File
			self.featureVectors = self.getMessageFeatureVectors()
			self.featureSet = self.chats[0].userA.messages[0].getFeatureSet()
			self.printToCSV(self.featureVectors, self.featureSet, "MessageFeatures.csv")
			
			#Write User Feature File
			self.featureVectors = self.getUserFeatureVectors()
			self.featureSet =  self.chats[0].userA.getFeatureSet()
			self.printToCSV(self.featureVectors, self.featureSet, "UserFeatures.csv")
		else:
			print "No chat files could be found."
		
		if Settings.DEBUG:
			self.__debug()

#===============================================
#--------------Public  Functions----------------

	def getUserFeatureVectors(self):
		"""Retrieve a list of feature vectors from all Users contained in Chats."""
		featureVectors = []			
		for chat in self.chats:
			featureVectors.append(chat.userA.featureVector)
			featureVectors.append(chat.userB.featureVector)
		return featureVectors
	
	def getMessageFeatureVectors(self):
		"""Retrieve a list of feature vectors from all Messages contained in Chats."""
		for chat in self.chats:
			for message in chat.userA.messages+chat.userB.messages:
				featureVectors.append(message.featureVector)
		return featureVectors

	def printToCSV(self, featureVectors, featureSet, fileName = "Features.csv", withHeader=True, overwrite=True):
		"""Output feature vectors to a .csv file."""
		if overwrite:
			f = open(fileName, 'w')
		else:
			f = open(fileName, 'a')
		
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
				
				if (re.search("[A-D]_[0-9_]*.txt",file) != None):
					#trim file name and search string
					file = file[len(Settings.ROOT_DIR):]
					userFiles.append(file)
				elif (re.search(".csv",file) != None):
					surveyFiles.append(file)
					
		return surveyFiles, userFiles
	

	def __makeChats(self):
		"""Create conversations by loading users from survey and message files
		
		creates an array of chats
		"""
		surveys = []
		users = {}
		chats = []
		
		#loop through any number of survey files in order to 
		for surveyFile in self.surveyFiles:
			survey = open(surveyFile, 'r')
			date = surveyFile.split('/')[0]
			
			#create a new Survey and user for each line in the survey file
			#add the users to a temporary array so that they can be added into chats
			tmpUsers = {}
			for line in survey:
				#find users based on survey results			
				surveys.append(Survey(line))
				userFile = surveys[-1].getUserFilename()
				userFName = Settings.ROOT_DIR+userFile
				
				#handle uncertain filenames
				try:
					userEventString = open(userFName, 'r').read()
					user = User(userEventString, surveys[-1])
					tmpUsers[user.index] = user
				except IOError:
					print "Expected file "+userFile+" was not found."
				
			#pair users and create chats	
			for username, user in tmpUsers.iteritems():
				if ((user.classification == 'A') or (user.classification == 'C')):
					#handle unpaired users
					try:
						chats.append(Chat(user, tmpUsers[user.partnerIndex]))
					except Exception:
						print "User "+user.username+" could not find their partner."
		return chats			


	def __debug(self):
		"""Print all variables contained in Attribute Selector."""
		print "Dumping Object AttributeSelector"
		pprint.pprint(self.surveyFiles)
		pprint.pprint(self.userFiles)

#make this object runnable
if __name__ == '__main__':
	selector = AttributeSelector()
	 
	 
	 
