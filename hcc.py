###############################
#
# Python script that recommends characters to choose when forming a 5-man team for quick matches and team league
#
###############################

# Import required libraries
import pandas as pd
import sqlite3 as lite
import collections
import requests
from StringIO import StringIO

# Get the latest player preferences and hero details from google docs
player_pref_data = (requests.get('https://docs.google.com/spreadsheets/d/1I3moDVJVrIU2xOimb1nFDWmGWh3fJNHjKmOxHxif4r8/pub?gid=0&single=true&output=csv')).content

hero_details_data = (requests.get('https://docs.google.com/spreadsheets/d/1I3moDVJVrIU2xOimb1nFDWmGWh3fJNHjKmOxHxif4r8/pub?gid=427084345&single=true&output=csv')).content

priorities_data = (requests.get('https://docs.google.com/spreadsheets/d/1I3moDVJVrIU2xOimb1nFDWmGWh3fJNHjKmOxHxif4r8/pub?gid=1668494311&single=true&output=csv')).content

# Convert from requests object to CSV then to dataframe
hero_details = pd.read_csv(StringIO(hero_details_data), header=0)
player_pref = pd.read_csv(StringIO(player_pref_data), header=0)
priorities = pd.read_csv(StringIO(priorities_data), header=0)

#format for accessing data by index: player_pref.loc['ty', 'hero1']
 
sql_hero = "INSERT INTO hero_details (hero_name, tier, role, melee_ranged, core_role, lane, ww1, ww2, ww3) VALUES (?,?,?,?,?,?,?,?,?)"
sql_player = "INSERT INTO player_pref (player_name, hero1, hero2, hero3, hero4, hero5) VALUES (?,?,?,?,?,?)"
sql_priorities = "INSERT INTO priorities (hero_name, ty, wisnu, kat, mark, flick) VALUES (?,?,?,?,?,?)"

def createDatabase():
	con = lite.connect('./db/hcc.db')
	cur = con.cursor()
	with con: 
		cur.execute("DROP TABLE IF EXISTS player_pref")
		cur.execute("DROP TABLE IF EXISTS hero_details")
		cur.execute("DROP TABLE IF EXISTS priorities")
		cur.execute("CREATE TABLE player_pref (player_name TEXT PRIMARY KEY, hero1 TEXT, hero2 TEXT, hero3 TEXT, hero4 TEXT, hero5 TEXT)")
		cur.execute("CREATE TABLE hero_details (hero_name TEXT PRIMARY KEY, tier INT, role TEXT, melee_ranged TEXT, core_role TEXT, lane INT, ww1 TEXT, ww2 TEXT, ww3 TEXT)")
		cur.execute("CREATE TABLE priorities (hero_name TEXT, ty INT, wisnu INT, kat INT, mark INT, flick INT)")

def populateTables():
	con = lite.connect('./db/hcc.db')
	cur = con.cursor()
	with con:
		
		# Populate the hero_details table in the sql database hcc.db
		for idx, hero in hero_details.iterrows():
			cur.execute(sql_hero, (hero['hero_name'], hero['tier'], hero['role'], hero['melee_ranged'], hero['core_role'], hero['lane'], hero['ww1'], hero['ww2'], hero['ww3']))

		# Populate the player_pref table in the sql database hcc.db
		for idx, player in player_pref.iterrows():
			cur.execute(sql_player, (player['player_name'], player['hero1'], player['hero2'], player['hero3'], player['hero4'], player['hero5']))

		for idx, hero in priorities.iterrows():
			cur.execute(sql_priorities, (hero['hero_name'], hero['ty'], hero['wisnu'], hero['kat'], hero['mark'], hero['flick']))

# Now the database should be populated with what is on our google doc, and we can actually start pulling what we need out of it

def calcTeam():
	con = lite.connect('./db/hcc.db')
	cur = con.cursor()
	
	return pd.read_sql_query("select hero_details.hero_name, tier, role from hero_details join priorities on (hero_details.hero_name = priorities.hero_name) where tier in (1,2) and role in ('assassin', 'warrior', 'support') and (ty = 1 or wisnu = 1 or kat = 1 or mark = 1 or flick = 1)", con)










# Build the core of the team (Healer, Tank, Assassin)
#hero1 = player_pref['hero1'].tolist()
