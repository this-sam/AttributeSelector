#settings file: contains all global settings

class Settings:
	 #========================DEBUG=============================
	 DEBUG = False 
	 
	 #-----------Visualization---------------
	 VISUALIZE = False
	 VIS_SPEED = .07
	 
	 #----------File Location Constants----------
	 ROOT_DIR = '/users/s/b/sbbrown/Development/Thesis/Files/'
	 #ROOT_DIR = '/Users/cscrew/Thesis/Files/'
	 
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
	 
	 #----------Feature Vectors----------?
	 #USER_FEATURES_STATIC = ['gender','orientation']
	 #USER_FEATURES_TOTALLED = ['numMessages', 'numEvents']
	 #USER_FEATURES_AVERAGED = []
	 #USER_FEATURES_CUSTOM = []
	 USER_CLASS_QUESTION = 7	#pick a survery question number for now (mapped like array: question 1 = index 0)