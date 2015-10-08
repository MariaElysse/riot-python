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
```python3
cd riot-python
python3
import summoner
c9_SummonerNames = ['C9 Meteos', 'C9 StealthBomber', 'C9 Hai', 'C9 Lemon', 'C9 Balls',]
c9_summoners = summoner.getSummoners(c9_SummonerNames) 
#returns a list of Summoner objects
for member in c9_summoners:
  print("Summoner Name: {}".format(member.summonerName))
  print("Last Seen: {}".format(member.revisionDate.ctime()))
```
will print:
```
Summoner Name: C9 Hai
Last Seen: Fri Aug 28 22:05:15 2015
Summoner Name: C9 Balls
Last Seen: Sat Jun 20 20:13:06 2015
Summoner Name: C9 Meteos
Last Seen: Tue Oct  6 05:20:25 2015
Summoner Name: C9 Lemon
Last Seen: Thu Aug 27 22:57:47 2015
Summoner Name: C9 StealthBomber
Last Seen: Sat Jul 18 23:42:29 2015
```

> riot-python isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
