global DEBUG
DEBUG = False
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
	
	global Survey, User, Chat
	from Survey import Survey
	from User import User
	from Chat import Chat
	
	#----------File Location Constants---------
	ROOT_DIR = '/users/s/b/sbbrown/Development/Thesis/Files/'
	
	
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
		
		if DEBUG:
			self.__debug()

#===============================================
#--------------Public  Functions----------------

	#!!!!!MOVE TO CHAT CLASS!!!!!!
	def printConvo(self, user):
		pass





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
		for dirpath, dirnames, filenames in AttributeSelector.os.walk(AttributeSelector.ROOT_DIR):
			for f in filenames:
				file = AttributeSelector.os.path.join(dirpath, f)
				
				#trim file name and search string
				file = file[len(AttributeSelector.ROOT_DIR):]
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
			survey = open(AttributeSelector.ROOT_DIR + surveyFile, 'r')
			date = surveyFile.split('/')[0]
			
			#create a new Survey and user for each line in the survey file
			#add the users to a temporary array so that they can be added into chats
			tmpUsers = {}
			for line in survey:
				surveys.append(Survey(line))
				userFile = surveys[-1].getUserFilename()
				userFName = AttributeSelector.ROOT_DIR+date+'/'+userFile
				userEventString = open(userFName, 'r').read()
				user = User(userEventString, surveys[-1])
				tmpUsers[user.username] = user
				print tmpUsers
				
			#pair users and create chats	
			for username, user in tmpUsers.iteritems():
				if ((user.classification == 'A') or (user.classification == 'C')):
					chats.append(Chat(user, tmpUsers[user.partner]))


	def __debug(self):
		print "Dumping Object AttributeSelector"
		pprint.pprint(self.surveyFiles)
		pprint.pprint(self.userFiles)
		pprint.pprint(self.errors)


	

if __name__ == '__main__':
	selector = AttributeSelector()
	 
	 
	 