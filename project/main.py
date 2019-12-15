# This just imports app, pages, and freezer, and views so that they can be 
# accessed without circular imports  

'''Entry point to all things to avoid circular imports.'''
from app import app, freezer, pages 
from views import * 