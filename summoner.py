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

#TODO: create worker function to create a number of summoner objects at once.
#TODO: modify summoner class to allow this.
#TODO: Complete Summoner class.

import requests
import api_key
import statics
import datetime

API_KEY = api_key.API_KEY
DEFAULT_REGION = statics.DEFAULT_REGION #seemed sensible

class Summoner(object):
	"""
	Objects representing Summoners
	Required Parameters:
		.
	
	Optional Parameters:
		region (Defaults to DEFAULT_REGION, which itself defaults to "NA")
	"""
	
	def __init__(self, summonerId, summonerName, profileIconId, revisionDate, summonerLevel, region):
		"""
		Class takes all data provided by the Riot API and stores it in the Summoner object.
		
		"""
		self.revisionDate = datetime.datetime.fromtimestamp(revisionDate/1000) 
		#convert from milliseconds to seconds
		self.summonerId = summonerId
		self.summonerName = summonerName
		self.profileIconId = profileIconId
		self.summonerLevel = summonerLevel
		self.region = region 
		self.matchlist = []
		
		r = requests.get('https://{0}.api.pvp.net/api/lol/{0}/v2.2/matchlist/by-summoner/{1}?api_key={2}'.format(region, summonerId, API_KEY))
		r.raise_for_status()
		
		matchlist = r.json()
		#todo: get basic match data, and add a list of those objects to the summoner object
	def __eq__(self, other):
		"""returns whether the other instance of summoner is the same as this one"""
		return (isinstance(other, Summoner)) and (self.summonerId == other.summonerId) and (self.region == other.region)
		
	def __str__(self):
		return "Summoner \"{0}\", Region: {1}".format(self.summonerName, self.region)
	
	def getSummoners(summonerData, region = DEFAULT_REGION, byId = False):
		"""
		Takes a list, which can be either summoner names or IDs (but not both), 
		as string or integer, and returns a list of Summoner objects.
		Indicate whether it's a list of Names or IDs with the byId parameter,
		which is set to False is they are summoner names (default), and True is they are summoner IDs.
		
		As such, running the function with just one arg will assume both that it's a list of summoner names and the region is DEFAULT_REGION.
		"""
		str_summonerData = ""
		summonersList = []
		
		if ((type(summonerData) == str) or (type(summonerData) == int)):
			str_summonerData = str(summonerData)
		elif type(summonerData) == list:	
			for x in summonerData:
				str_summonerData += str(x) + ','
		else:
			raise RuntimeError("Invalid summoner data provided to function getSummoners")
		
		if byId:
			r = requests.get('https://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/{1}?api_key={2}'.format(region, str_summonerData, API_KEY))
		else:	
			r = requests.get('https://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/by-name/{1}?api_key={2}'.format(region, str_summonerData, API_KEY))
		r.raise_for_status()
		#trying to by DRY, but maybe this isn't the time?
		for summoner in r.json():
			singleSummoner = r.json()[summoner]
			summonersList.append(Summoner(singleSummoner['id'], singleSummoner['name'], singleSummoner['profileIconId'], singleSummoner['revisionDate'], singleSummoner['summonerLevel'], region))
		
		return summonersList
		
		
