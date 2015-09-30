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
VALID_REGIONS = ('br', 'oce', 'na', 'las', 'lan', 'euw', 'eune', 'tr', 'kr', 'ru',) #this is probably going to be useless
API_KEY = api_key.API_KEY
DEFAULT_REGION = statics.DEFAULT_REGION #seemed sensible

class Summoner(object):
	"""
	Objects representing Summoners
	Required Parameters:
		valid SummonerId xor SummonerName.
	
	Optional Parameters:
		region (Defaults to DEFAULT_REGION, which itself defaults to "NA")
	"""
	
	def __init__(self, summonerId = None, summonerName = None, region = DEFAULT_REGION):
		if (summonerId == None) and (summonerName == None):
			raise RuntimeError("No summonerID or Summoner Name provided.")
		#If both are None, we got nothing and we can't work with nothing.
		elif (summonerId != None) and (summonerName != None):
			raise RuntimeError("Summoner ID and Summoner Name provided. Only one is needed.")
		#If both are set, this could potentially cause undefined behavior, as summoner names and ids are unique
		elif (summonerId == None):
			summonerData = requests.get('https://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/by-name/{1}?api_key={2}'.format(region,summonerName, API_KEY)).json()[summonerName]
		#if we got a summoner name (as in, we didn't get a summoner ID'), make summoner name specific request 
		elif (summonerName == None):
			summonerData = requests.get('https://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/{1}?api_key={2}'.format(region, summonerId, API_KEY))[summonerId]
		#if we got a summoner ID, as in did not get a summoner name, make summoner ID specific request.
		#both requests are of the same format.
		
		self.revisionDate = datetime.datetime.fromtimestamp(summonerData['revisionDate']/1000) 
		#convert from milliseconds to seconds
		self.summonerId = summonerData['id']
		self.summonerName = summonerData['name']
		self.profileIconId = summonerData['profileIconId']
		self.summonerLevel = summonerData['summonerLevel']
		self.region = region 
		
		def __eq__(self, other):
			"""returns whether the other instance of summoner is the same as this one"""
			return (isinstance(other, Summoner)) and (self.summonerID == other.summonerID) and (self.region == other.region)
		
		def __str__(self):
			return "Summoner \"{0}\", Region: {1}".format(self.summonerName, self.region)
	
	
