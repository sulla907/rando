import psycopg2

print('>> Attempting to connect to database....')
con = psycopg2.connect(database='test', user='', password='', host='', port='5432')
print('>> Connected to database')
c = con.cursor()
make_table = '''CREATE TABLE download_speed (timestamp text, speed text)'''
c.execute(make_table)
con.commit()
print('>> Table created')
print('Win')