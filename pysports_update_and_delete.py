'''
Garrett May
CSD310-306J Database Development and Use (2225-DD)
Module 9.3 Assignment
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
    cursor = db.cursor()
    
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                  "VALUES(%s, %s, %s)")
    
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)
    
    db.commit()
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")
    
    players = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYERS AFTER INSERT -- ")
    
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
        
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    
    db.commit()
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")    
    
    players = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYERS AFTER UPDATE -- ")
    
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
        
    cursor.execute("DELETE FROM player where first_name = 'Gollum'")    
    
    db.commit()
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")
    
    players = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYERS AFTER DELETE -- ")
    
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()

    input("\n\n Press any key to continue... ")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()