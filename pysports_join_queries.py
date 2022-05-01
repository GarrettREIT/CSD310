'''
Garrett May
CSD310-306J Database Development and Use (2225-DD)
Module 8.3 Assignment
1 May 2022
'''

""" import statements """
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "BluesHockey45",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    
    db = mysql.connector.connect(**config)
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")
    
    players = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYER RECORDS -- ")
    
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
        
    input("\n\n Press any key to continue... ")    
        
finally:
    db.close()        