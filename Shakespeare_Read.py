import pymysql
import time

myConnection = pymysql.connect(host = 'localhost', user = 'admin', passwd = 'LocalSQL1123!', db = 'shakespeare')
cur = myConnection.cursor()

start_time = time.time()

cur.execute('SELECT play_text FROM amnd;')
for line in cur.fetchall():
    print(line[0])

end_time = time.time()

cur.execute('SELECT COUNT(line_number) FROM amnd;')
numPlayLines = cur.fetchall()[0][0]
print(numPlayLines, ' rows')

queryExecTime = end_time - start_time
print('Total query time: ', queryExecTime)
queryTimePerLine = queryExecTime / numPlayLines
print('Query time per line ', queryTimePerLine)

insertPerfSQL = 'INSERT INTO performance VALUES ("READ", %s);'
cur.execute(insertPerfSQL, queryTimePerLine)

myConnection.commit()
myConnection.close()
