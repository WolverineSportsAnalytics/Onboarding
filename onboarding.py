import mysql.connector
import requests
from bs4 import BeautifulSoup


def get_combine_data(cursor, cnx):
    ''' This will get combine data from http://nflcombineresults.com/nflcombinedata.php 
    and place that data into a table named WSA.nfl on the local host
    Takes a mysql connector cursor and connection object as parameters'''
    

    return None

def main():
    ''' Main function to create mysql connector object run get_combine_data '''
    cnx = mysql.connector.connect(user="root",
            host="127.0.0.1",
            database="WSA",
            password="")                                                                                                               
    cursor = cnx.cursor()

    clear_table(cursor, cnx)
    get_combine_data(cursor, cnx)

    # testing section don't edit
    try:
        testing_data(cursor, cnx)
    except Exception as e:
        print "Testing failed with error:" 
        print e

def clean_tuple(inserts):
     ''' This will take a tuple with empty values and replace those with python None '''
     inserts = list(inserts)
     for i in range(len(inserts)):
        if not inserts[i] or inserts[i]==u'9.99':
            inserts[i] = None
    return tuple(inserts)

def testing_data(cursor, cnx):
    ''' This is just a quick test to see if the first row of the database is correct '''

    select = "Select * from NFL where playerID = 1"
    cursor.execute(select)
    response = cursor.fetchall()[0]
    name = response[2]
    bench = response[8]

    if name == "Josh Adams" and bench == 18 :
        print "Testing Passed"
    else:
        print "First Row Does Not Match"

def clear_table(cursor, cnx):
    ''' Helper Function to call in order to clear table after mistakes '''

    cursor.execute("Delete from NFL")
    cursor.execute("ALTER TABLE NFL AUTO_INCREMENT = 1")
    cnx.commit()

if __name__=="__main__":
    main()
