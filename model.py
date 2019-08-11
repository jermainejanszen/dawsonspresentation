'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view, sql, json
from datetime import datetime

import controller as Controller

# Initialise our views, all arguments are defaults
page_view = view.View()
db = sql.SQLDatabase()
db.database_setup()

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    return page_view("index")
