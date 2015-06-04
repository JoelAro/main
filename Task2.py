import os
os.mkdir("C:\\Users\\admin\\Desktop\\Newfolder")
os.chdir("C:\\Users\\admin\\Desktop\\Newfolder")
file1=open('C:\\Users\\admin\\Desktop\\Newfolder',"python1.py","w")
file1.write("""import mysql.connector
conn=mysql.connector.connect(user='root',password='joel',host='localhost')
mycursor=conn.cursor()
mycursor.execute("CREATE DATABASE python")
mycursor.execute("USE python")
mycursor.execute("""CREATE TABLE Time
(
Hours int
Minutes int
Seconds int)""")""")
file1.close()
file2=open('C:\\Users\\admin\\Desktop\\Newfolder',"python2.py","w")
file2.write("""from crontab import CronTab
import mysql.connector
import time
conn=mysql.connector.connect(user='root',password='joel',host='localhost',database='python')
mycursor=conn.cursor()
date=time.localtime(time.time())
mycursor.execute("""INSERT INTO python VALUES
(date[3],date[4],date[5])""")
conn.commit()
job=cron.new(command='/usr/bin/echo')
job.minute.every(10)""")
file2.close()
execfile('python1.py')
execfile('python2.py')




