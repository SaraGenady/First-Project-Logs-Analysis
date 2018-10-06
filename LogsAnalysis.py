# import sqlite3 #
import sqlite3
# connect db #
conn= sqlite3.connect('LogsAnalysis.db')
# init cursor #
c = conn.cursor()

# What are the most popular three articles of all time? 
top_three_articles=c.execute("""select articles.title, count(*) as views_num
            from logs,articles
            where logs.status='200 OK'
			and articles.slug = substr(logs.path, 10)
            group by logs.path
            order by views_num desc 
            limit 3""")
# Print question
print("What are the most popular three articles of all time?")
# Loop on articles and print
for title, views_num in top_three_articles:
     print(" \"{}\" -- {} views".format(title, views_num))

# Who are the most popular article authors of all time?
top_authors =c.execute("""select authors.name, count(*) as views_num
              from articles, authors, logs
              where logs.status='200 OK'
              and authors.id = articles.author
              and articles.slug = substr(logs.path, 10)
              group by authors.name
              order by views_num desc""")
# Print question
print("Who are the most popular article authors of all time?")
# Loop on authors and print
for title, views_num in top_authors:
     print(" \"{}\" -- {} views".format(title, views_num))

# On which days did more than 1% of requests lead to errors?
error_requests =c.execute("""select substr(logs1.time,0,11) as DateError ,
                             (count(*) * 100 / (select count(1) 
                             from logs 
                             where substr(logs.time,0,11) = substr(logs1.time,0,11))) PresError
                             from logs logs1
                             where logs1.status='404 NOT FOUND'
                             group by DateError
                             having PresError > 1""")
# Print question
print("On which days did more than 1% of requests lead to errors?")
# Loop on error_requests and print
for DateError, PresError in error_requests:
     print(" \"{}\" -- {} % errors".format(DateError, PresError))


# conn commit #
conn.commit()

# conn close #
conn.close()