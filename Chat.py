#Chat is initialized by passing in the two Users who make up the chat
#The users contain their half of the conversation, from which the chat builds
#a time-sorted reconstruction of the chat (message by message)

class Chat:
	#Chat should know what type (MM, MF, FF) it is and be able to perform calcul-
	#ations on the male/female specific data
	import time
	
	global Settings
	from Settings import Settings
	
	def __init__(self, userA, userB):
		#grab partners, and set their partner usernames correctly
		self.userA, self.userB = userA, userB
		self.userA.partner = self.userB.username
		self.userB.partner = self.userA.username
		
		if Settings.VISUALIZE:
			self.visualize(Settings.VIS_SPEED)
		
		if Settings.DEBUG:
			self.__debug()
			
			
	def visualize(self, speed=.01):
		A = self.userA.eventString.split('[end]')
		B = self.userB.eventString.split('[end]')
		for i in range(min(len(A), len(B))):
			print A[i].strip()
			print B[i].strip()
			Chat.time.sleep(speed)
	
	def __debug(self):
		print "Dumping Object Chat"
		print self.userA.username +' + '+ self.userB.username