import psycopg2

print('>> Attempting to connect to database....')
con = psycopg2.connect(database='test', user='warPig', password='test', host='3.144.128.71', port='5432')
print('>> Connected to database')
c = con.cursor()
make_table = '''CREATE TABLE download_speed (timestamp text, speed text)'''
c.execute(make_table)
con.commit()
print('>> Table created')
print('Win')