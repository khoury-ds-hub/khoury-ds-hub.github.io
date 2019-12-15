import os 

REPO_NAME = "khoury-ds-hub.github.io" #Used for FREEZER_BASE_URL
DEBUG = True 


# Assumes the app is located in the same directory where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path): 
	'''Returns the parent of a directory.'''
	return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files 
# to the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Gihub user page), 
# we need to set the BASE_url to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME) 
FREEZER_REMOVE_EXTRA_FILES = False # IMPORTANT: If this is True, all app files
								   # will be delted when you run the freezer

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'


# More comments: 
#	L17: Tell Frozen-Flask to build the static content to the project root instead of 
#		 the default build/ directory.  
#	L20: We also need to explicitly set FREEZER_BASE_URL since GH Pages hosts
#		 your repo pages on http://username.github.com/your-reponame 
#	L21: Don't delete all your app files! 
#	L25-26: Tell FlatPages to look for .md files in the project/pages/ directory 