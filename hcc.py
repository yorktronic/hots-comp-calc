###############################
#
# Python script that recommends characters to choose when forming a 5-man team for quick matches and team league
#
###############################

# Import required libraries
import pandas
import sqlite3 as lite
import collections
import requests



# Get the latest player preferences and hero details from google docs
hero_details_csv = requests.get('https://docs.google.com/spreadsheets/d/1I3moDVJVrIU2xOimb1nFDWmGWh3fJNHjKmOxHxif4r8/pub?output=csv')
player_pref_csf = requests.get('https://docs.google.com/spreadsheets/d/1I3moDVJVrIU2xOimb1nFDWmGWh3fJNHjKmOxHxif4r8/pub?output=csv')

# Convert from CSV to dataframe
from StringIO import StringIO
hero_details = pd.read_csv(StringIO(hero_details_csv), index_col = 0)



player_pref = pd.read_csv('./player_pref.csv')


# Create the SQL database
def createDatabase():
	con = lite.connect('./db/hcc.db')
	cur = con.cursor()
	with con: 
		cur.execute('CREATE TABLE player_pref ')

