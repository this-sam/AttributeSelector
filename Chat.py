#===============================================================================
#
# Chat.py by Sam Brown
# Chat is initialized by passing in the two Users who make up the chat
# The users contain their half of the conversation. The chat object is primarily
# used to contain these pairs of Users.
#
#===============================================================================

class Chat(object):
	"""Contains two User objects who are paired into one conversation."""
	import time
	
	global Settings
	from Settings import Settings
	
	def __init__(self, userA, userB):
		"""Load both users into the Chat and visualize the convo if set to do so."""
		#grab partners, and set their partner usernames correctly
		self.userA, self.userB = userA, userB
		self.userA.partner = self.userB.username
		self.userB.partner = self.userA.username
		
		if Settings.VISUALIZE:
			self.visualize(Settings.VIS_SPEED)
		
		if Settings.DEBUG:
			self.__debug()
			
			
	def visualize(self, speed=.01):
		"""Perform a fake visualization of the two halves of the convo in parallel.
		   This is 'fake' because the timestamps are not synced."""
		A = self.userA.eventString.split('[end]')
		B = self.userB.eventString.split('[end]')
		for i in range(min(len(A), len(B))):
			print A[i].strip()
			print B[i].strip()
			Chat.time.sleep(speed)
	
	def __debug(self):
		"""Print all variables contained in Chat."""
		print "Dumping Object Chat"
		print self.userA.username +' + '+ self.userB.username