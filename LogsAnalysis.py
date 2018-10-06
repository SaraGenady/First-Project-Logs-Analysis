# import sqlite3 #
import sqlite3
# connect db #
conn= sqlite3.connect('LogsAnalysis.db')
# init cursor #
c = conn.cursor()



# conn commit #
conn.commit()

# conn close #
conn.close()