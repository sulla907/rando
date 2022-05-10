
import sqlite3
import subprocess
import re
import os 
from datetime import datetime
import pandas

def get_speed():
    print('>> Checking download speed....')
    output = subprocess.run(['speedtest'], capture_output=True).stdout.decode()
    re_exp = 'Download:\s(.*)'
    internet_speed = re.findall(re_exp, output)
    return(internet_speed[0])
   

def record_data(timestamp, speed):
    db = sqlite3.connect('internet_speed.db')
    print('>> Connected to DB')
    c = db.cursor()
    data = [timestamp, speed]
    statment = 'INSERT INTO download_speed VALUES (?,?)'
    c.execute(statment, data)
    db.commit()
    c.close()
    print('>> Commited successfully\n>> Closing database connection...')
    
    

def speed_db(speed):
    time = datetime.now()
    time_stamp = time.strftime("%d-%h-%Y_%H%M")
    if os.path.isfile('./internet_speed.db'):
        
        record_data(time_stamp, speed)
        return
        
    else:    
        db = sqlite3.connect('internet_speed.db')
        print('>> DB created')
        c = db.cursor()
        make_table = '''CREATE TABLE download_speed (timestamp text, speed text)'''
        c.execute(make_table)
        print(">> Speed database table created")
        db.commit
        c.close()
        record_data(time_stamp, speed)
    
    
def show_data():
    db = sqlite3.connect('internet_speed.db')
    query = " SELECT * FROM download_speed"
    sql_data = pandas.read_sql_query(query, db)
    print(sql_data)
    
if __name__ == '__main__':
    speed = get_speed()
    speed_db(speed)
    show_data()