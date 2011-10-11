#==========================================================

class AttributeSelector:
	
	import os
	
	#----------File Location Constants---------
	ROOT_DIR = '~/Development/Thesis/Files'
	
	def __init__(self):
		#log errors
		self.errors = []
		
		#get input files
		#store files in dictionary --> USERNAME =>
		self.files = []
		
		#get questionnaires
		#store files in dictionary --> USERNAME => Questionnaire
		
		pass

	def __get_files(self):
		try:
			AttributeSelector.os.chdir(AttributeSelector.ROOT_DIR)
		except:
			self.errors.append("Unable to access file root.")
		else:
			#NEED TO DO THIS RECURSIVELY THROUGH DIRECTORIES
			self.files = AttributeSelector.os.listdir('.')


if __name__ == '__main__':
    selector = AttributeSelector()