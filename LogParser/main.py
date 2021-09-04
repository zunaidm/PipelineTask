import re
import psycopg2

#Db Connection
conn = psycopg2.connect(
     dbname="djangotask",
     user="postgres",
     password="1234",
     host="localhost",
     port="5432"
)
cur = conn.cursor()

#Regular expression
pattern_date_time = re.compile(r'[A-Z][a-z]{2}[ ][0-9]{2}[ ][0-9]{2}[:][0-9]{2}[:][0-9]{2}')
pattern_log_category = re.compile(r'(?<=elk-anis-test ).+?(?=\[[0-9]+\]: |:)')
pattern_message = re.compile(r'(?<=]: |[A-Za-z]: ).+')

with open('log', 'r') as log:
    content = log.readlines()
    i = 0
    for line in content:
        i = i+1

        matches_date_time = pattern_date_time.finditer(line)
        matches_log_category = pattern_log_category.finditer(line)
        matches_message = pattern_message.finditer(line)

        date_time = ""
        category = ""
        message = ""

        for match in matches_date_time:
            date_time=match[0]
        for match in matches_log_category:
            category=match[0]
        for match in matches_message:
            message=match[0]

        cur.execute("INSERT INTO dashboard_log (date_time,category,message) values(%s,%s,%s)",(date_time,category,message))
        print(i," ", date_time," ", category," ", message)

conn.commit()
conn.close()


