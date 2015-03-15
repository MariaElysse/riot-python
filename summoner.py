#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  summoner.py
#  
#  Copyright 2015 Jeremy Neptune <jerenept@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

valid_regions = ('br', 'oce', 'na', 'las', 'lan', 'euw', 'eune', 'tr', 'kr', 'ru',) #this is probably going to be useless

import requests

class Summoner(object):
	"""Objects representing Summoners"""
	def __init__(self, summonerID, summonerName, profileIconID, revisionDate, summonerLevel, region):
		self.summonerID = summonerID
		self.summonerName = summonerName
		self.summonerLevel = summonerLevel
		self.profileIconID = profileIconID
		self.revisionDate = revisionDate
		self.region = region
		
	def __eq__(self, other):
		"""returns whether the other instance of summoner is the same as this one"""
		return (isinstance(other, Summoner)) and (self.summonerID == other.summonerID) and (self.region == other.region)

class GetSummoners(object):

	def byName(summonerNames, region, api_key):
		"""returns a list of Summoner objects, from a list of summoner names, and region"""
		#I should format that into the kind of list the API expects
		summonerNamesStr = ','.join(summonerNames)
		r = requests.get('http://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/by-name/{1}?api_key={2}'.format(region,summonerNamesStr, api_key))
		listOfSummoners = []
		for summoner in r.json():
			x = r.json()[summoner]
			newSummoner = Summoner(x['id'], x['name'], x['summonerLevel'], x['profileIconId'], x['revisionDate'], x['summonerLevel'], region)
			listOfSummoners.append(newSummoner)
		return listOfSummoners
	
	def byId(summonerIds, region, api_key):
		"""returns a list of Summoner objects, from a list of summoner ids, and region"""
		#formatted into what the API wants
		summonerIdsStr = ','.join(summonerIds)
		r = requests.get('http://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/{1}?api_key={2}'.format(region,summonerIdsStr, api_key))
		listOfSummoners = []
		for summoner in r.json():
			x = r.json()[summoner]
			newSummoner = Summoner(x['id'], x['name'], x['summonerLevel'], x['profileIconId'], x['revisionDate'], x['summonerLevel'], region)
			listOfSummoners.append(newSummoner)
		return listOfSummoners
	#the fact that these functions are nearly identical is highly disturbing, and I think I should do something about it. Or maybe not.
	#They seem perfectly happy caught up in their little class here
	
#class Mastery(object):
#	def __init__(self, 
	
	
class MasteryPage(object):
	"""contains masteries"""
	def __init__(self, isCurrent, pageId, masteries, name):
		self.isCurrent = isCurrent 
		self.pageId = pageId
		self.masteries = masteries
		self.name = name
		
	#...	
