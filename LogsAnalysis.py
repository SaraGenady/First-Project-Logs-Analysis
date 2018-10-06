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

# conn commit #
conn.commit()

# conn close #
conn.close()