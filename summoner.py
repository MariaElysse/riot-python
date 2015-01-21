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


import requests

Class Summoner(object):
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
		 return (isinstance(other, Summoner)) AND (self.summonerID == other.summonerID) AND (self.region == other.region)


