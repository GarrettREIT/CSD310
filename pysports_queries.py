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
    
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    
    teams = cursor.fetchall()
    
    print()
    print("-- DISPLAYING TEAM RECORDS --")
    
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()

    print("-- DISPLAYING PLAYER RECORDS --")

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")       
    players = cursor.fetchall()

    for player in players:
        print("Player ID: {}".format(player[0]))
        print("Player First Name: {}".format(player[1]))
        print("Player Lase Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()
        

finally:
    db.close()