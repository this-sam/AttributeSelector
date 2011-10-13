#Chat is initialized by passing in the two Users who make up the chat
#The users contain their half of the conversation, from which the chat builds
#a time-sorted reconstruction of the chat (message by message)

class Chat:
	#Chat should know what type (MM, MF, FF) it is and be able to perform calcul-
	#ations on the male/female specific data
	import time
	def __init__(self, userA, userB):
		self.userA, self.userB = userA, userB
		
		self.visualize()
			
			
	def visualize(self, speed=.05):
		##DELETE ME THIS IS ONLY TO WATCH
		A = self.userA.eventString.split('[end]')
		B = self.userB.eventString.split('[end]')
		for i in range(min(len(A), len(B))):
			print A[i].strip()
			print B[i].strip()
			Chat.time.sleep(speed)