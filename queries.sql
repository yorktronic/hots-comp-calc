# Get the player_naem and hero_name from player_pref that have are hero1,2, have a tier of 1 or 2 and a role of assassin, tank, or melee
select hero_details.hero_name, tier, role
	from hero_details join priorities on (hero_details.hero_name = priorities.hero_name)
		where tier in (1,2) 
			and role in ('assassin', 'warrior', 'support') 
				and (ty in (1,2) or wisnu in (1,2) or kat in (1,2) or mark in (1,2) or flick in (1,2))


# Query 2
select player_name, hero_details.hero_name, tier, role 
	from player_pref join hero_details on (hero1 = hero_details.hero_name)
		where hero1 in (
			select hero_details.hero_name
				from hero_details join priorities on (hero_details.hero_name = priorities.hero_name)
					where tier in (1,2) 
						and role in ('assassin', 'warrior', 'support') 
							and (ty = 1 or wisnu = 1 or kat = 1 or mark = 1 or flick = 1))

#Query 3
select hero_details.hero_name, tier, role
	from hero_details join priorities on (hero_details.hero_name = priorities.hero_name)
		where tier in (1,2) 
			and role in ('specialist') 
				and (ty in (1,2) or wisnu in (1,2) or kat in (1,2) or mark in (1,2) or flick in (1,2))