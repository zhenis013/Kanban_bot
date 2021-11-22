import sqlite3
import pandas as pd

conn = sqlite3.connect('kanban_db.db', check_same_thread=False)
cursor = conn.cursor()

def get_user_name(chat_id):
	cursor.execute(f'select name from kanban_users where chat_id = {chat_id}')
	name = cursor.fetchall()
	name = list(sum(name, ()))


	# df = pd.DataFrame({'Chat_id':chat_ids,'Names':names})

	conn.commit()
	return name[0]

def insert_cause(name, defocus, decompos, nuance, tired, date):
	cursor.execute('INSERT INTO kanban_review (name, defocus, decompos, nuance,tired,review_date) VALUES (?, ?, ?, ?, ?,?)', (name, defocus, decompos, nuance, tired ,date))
	conn.commit()

def get_chat_id(chat_id,name):
	cursor.execute('insert into kanban_users (chat_id,Name) values(?,?)',(chat_id, name))
	conn.commit()


