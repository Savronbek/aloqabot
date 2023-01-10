# import sqlite3 as sq

# async def db_start():
#     global db, cur

#     db = sq.connect('test.db')
#     cur = db.cursor()

#     cur.execute("CREATE TABLE IF NOT EXISTS profile")




from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

