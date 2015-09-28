#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  statics.py
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

"""
Static data for Riot Api, I should have this in a separate file for now 
till I decide if they would be better as parts of others or not
"""

import requests

import api_key

API_KEY = api_key.API_KEY

r = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key={}".format(API_KEY)).json()

CURRENT_PATCH = r[0]
#the first member in the list of patches, sorted by recency, is the most current patch


class Mastery:
	"""
	Describes a single mastery. 
	Does not interact with the Image object included in the Mastery object
	Instead, just gives a string with the DataDragon URL to the mastery's
	image.
	
	self.prereq contains None if there is no prerequisite mastery.
	""" 
	allMasteryData = requests.get("http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/mastery.json".format(CURRENT_PATCH)).json()['data'] #todo:i18n
	def __init__(self, masteryId, patch = CURRENT_PATCH):
		"""Initializes the Mastery object with data about that particular mastery."""
		
		self.masteryId = str(masteryId)
		
		#this block sets the member variables according to the JSON info we got 
		#from the DataDragon API
		
		self.masteryData = self.allMasteryData[self.masteryId]
		self.name = self.masteryData['name'] #name of mastery
		self.description = self.masteryData['description'] 
		
		#this is a list of the mastery's possibly numerous descriptions, as the 
		#descriptions may change depending on rank.
				
		self.imageURL = "http://ddragon.leagueoflegends.com/cdn/{0}/img/mastery/{1}.png".format(patch, self.masteryId)
		
		self.ranks = self.masteryData['ranks'] 	#this should be the length of the list in self.description
		
		if (self.masteryData['prereq']=='0'):
			self.prereq = None
		else:
			self.prereq = self.Mastery(masteryData['prereq'], patch)
		#self.prereq is the mastery that must be active for
		#this one to be used.
	def __str__(self):
		"""Returns a (Unicode) String describing the Mastery Object."""
		return self.name
	
	def __eq__(self, other):
		"""Returns whether two mastery objects (specifically) actually describe the same Mastery"""
		assert isinstance(other, Mastery), "Invalid Comparison with	Mastery object."
		#there really isn't anything else a mastery can conceivably be compared with
		#and False may be a misleading return.
		return (self.masteryId == other.masteryId)
