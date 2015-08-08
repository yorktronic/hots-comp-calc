# Heroes of the Storm Team Comp Calculator #

Python script that recommends characters to choose when forming a 5-man team for quick matches and team league. 

## How it Works ##

Takes in a .csv of a team's top 5 preferred characters (i.e., each team member picks the five characters he enjoys to play most), and then creates a team based on VirginHeroes' Guide to Team Creation. While his post could be considered dated, my friends and I believe the theory behind team creation is still solid. 

Using VirginHeroes' theory, combined with up-to-date data from Heroes Fire on the tier of a hero along with their role, this calculator aims to use optimization / data science techniques to recommend a decent team that combines ideal composition, player preference, and picking top tier heroes whenever possible. 

We start out by picking the "core" members of any 5-man team: Tank, Healer, and Assassin. The assassin can be ranged or melee, but currently the calculator will prefer a ranged assassin unless a melee one is specified or a ranged assassin isn't available in the player preference csv. Using a combination of player preference and hero tier, a Tank, Healer, and Assassin combo will be formed from the CSV and this 3-hero group will serve as the core of the team.

Next, the calculator will ensure that the team has adequate laning capability. If the assassin that was selected as part of the core team has good laning capability, then the next character will be selected mostly by player preference, tier of hero, and the attributes of the core assassin (more to come on this). Converseley, if the core assassin hero does not have adequate laning capability, then the next character selection will prioritize laning capability above all other factors, likely picking a top-tier hero such as Sylvanas, Nazeebo, or someone else who rocks at laning.

The final hero will be selected based on the attributes of the previous heroes (more to come on this, also).

## Required Things / Libraries ##
* python
* pandas
* sqlite3
* knowing how to create a csv file (you can use Excel, Google Sheets, Open Office, whatever apple product to do this and export to csv) with the following columns <a href="https://docs.google.com/spreadsheets/d/1bUMx7QqzBAutBXNB0wlhzaAO2esWF6Th8iTeDUbPaOw/edit#gid=0" target="_blank">(click here to view a sample on Google Sheets)</a>:
	* `player` - player names for you and your team members
	* `hero1`
	* `hero2`
	* `...`
	* `hero5` - the heroes that the players on your team prefer, ranked 1-5

## Upcoming ##
* Actually writing the algorithm
* Figuring out if I can use Blizzard's API or access HeroesFire data somehow to make sure the output is using the latest information
* Posting some team comps that it created
* Adding "ideal" hero pairings based on the "Top Teammates" numbers on HeroesFire


