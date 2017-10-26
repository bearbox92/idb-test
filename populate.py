from six.moves import urllib
import json
import ssl
import time
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items


baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()

def scrapeHeroes():
#24 heroes
	for h in range(1, 25):
		tempurl = baseurl + '/hero/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		Hero_id = data['id']
		name = data['name']
		description = data['description']

		abilities_list = data['abilties']

		b = false

		name_str = ''
		ulti = ''
		for i in abilties_list:
			if i['is_ultimate']:
				ulti = i['name']
			else:
				if not b:
					name_str += i['name'] 
					b = true
				else:
					name_str += ', '
					name_str += i['name'] 
		



		#Need to insert these into the Database
		


#def getPlay  erInfo():

	#all the url, info to create each json

def scrapeAchievements():

	for h in range(1, 75):
		tempurl = baseurl + '/achievement/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		name = data['name']
		description = data['description']

	#all the url, info to create each json

def scrapeEvents():

	for h in range(1, 4):
		tempurl = baseurl + '/event/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		name = data['name']
		start = data['start_date']
		end = data['end_date']

	#all the url, info to create each json

def scrapeSkinsItems():

	for h in range(1, 1887):
		tempurl = baseurl + '/reward/' + str(h)

		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		reward_type = data['type']['name']
		if  reward_type == 'skin':
			skin = reward_type
		else:
			item = reward_type



def scrapeTopPlayers():
	battletags = ['SPREE-2984', 'HaventMetYou-2451', 'Hydration-1570', 'zombs-1642', 'Seraphic-21298', 'Jchuk99-1390', 'SumAwsomeKid-1356', 'YLLES-3238', 'SKRRSKRR-1878', 'NotE-1996']
	#top 10 players to start with
	for h in range(0, 10):
		tempurl = "https://owapi.net/api/v3/u/" + battletags[h] + "/blob"
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		name = battletags[h]
		win_rate = data['us']['stats']['competitive']['overall_stats']['win_rate']
		tier = data['us']['stats']['competitive']['overall_stats']['tier']
		level = data['us']['stats']['competitive']['overall_stats']['level']
		skill_rank = data['us']['stats']['competitive']['overall_stats']['comprank']

		# print(name)
		# print(win_rate)
		# print(tier)
		# print(level)
		# print(skill_rank)
		# print("--------")
	    # parse json here
	    #print(thejson.read())
		time.sleep(5)

	#all the url, info to create each json


def main():
	#scrapeHeroes()
	#scrapeAchievements()
	#scrapeEvents()
	#scrapeSkinsItems()
	scrapeTopPlayers()

if __name__ == "__main__": main()
