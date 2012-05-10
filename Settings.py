#===============================================================================
#
# Settings.py by Sam Brown
#
# Contains all globally required settings for the AttributeSelector in one convenient
# place.  Modify these to set for all objects.
#
#===============================================================================

class Settings:
    #========================DEBUG=============================
	 DEBUG = False 
	 
	 #-----------Visualization---------------
	 VISUALIZE = False
	 VIS_SPEED = .07
	 
	 #----------File Location Constants----------
     #Home Ubuntu
	 ROOT_DIR = '/home/sam/Development/ConversationGenerator/Files/'

	 #----------Event Constants-----------
	 EVENT_TYPES = ['tim', 'stt', 'bkb', 'bka', 'snd', 'deb', 'dea']
	 EMOTICON_TYPES = [':)', ': )', ':-)']

	 #----------Message Constants-----------
	 MESSAGE_TYPES = ['snd', 'del']
	 
	 #----------Username Constants-----------
	 USERNAME_MAPPINGS = {'A':'B', 'B':'A', 'C':'D', 'D':'C'}
	 #check these two!!!
	 ORIENTATION_MAPPINGS = {'A':'S', 'B':'S', 'C':'G', 'D':'G'}
	 GENDER_MAPPINGS = {'A':'M', 'B':'F', 'C':'M', 'D':'F'}

	 #----------Time Constants-----------
	 YEAR = 2012