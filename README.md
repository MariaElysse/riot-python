# riot-python
Python wrapper for the Riot Games API.

Dependencies
-------------
requests <= 2.0
Python <= 3.4 (Any Python3 is probably fine, but I haven't tested those)

Installing
----------
* Download/clone repository  
* Create a file called api_key.py with contents:  
    `API_KEY = 'YOUR-API-KEY'`  
* import the currently useful file (summoner.py)  

Using
-------
For now, the API only supports getting Summoner objects, and some basic data relating to Summoners (Mastery Pages, etc.)

For example: 
`  cd riot-python
python3
import summoner
c9_SummonerNames = ['C9 Meteos', 'C9 StealthBomber', 'C9 Hai', 'C9 Lemon', 'C9 Balls',]
c9_summoners = summoner.getSummoners(c9_SummonerNames) 
#returns a list of Summoner objects
for member in c9_summoners:
  print("Summoner Name: {}".format(member.summonerName))
  print("Last Seen: {}".format(member.revisionDate.ctime()))


