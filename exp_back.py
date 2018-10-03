import sqlite3 as sq

def create():
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS records(name TEXT,amount INTEGER,date TEXT,nature TEXT)")
	con.commit()
	con.close()
 
def insert_ent(name,amount,date,nature):
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("INSERT INTO records VALUES(?,?,?,?)",(name,amount,date,nature))
	con.commit()
	con.close()

def view_ent():
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM records")
	rows=cur.fetchall()
	con.close()
	return rows

def search(name="",amount="",date="",nature=""):
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM records WHERE name=? OR amount=? OR date=? OR nature=?",(name,amount,date,nature))
	rows=cur.fetchall()
	con.close()
	return rows

def delete(name="",amount="",date=""):
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("DELETE FROM records WHERE name=? AND amount=? AND date=?",(name,amount,date))
	con.commit()
	con.close()

def cal_bal():
	con=sq.connect("expenditureee.db")
	cur=con.cursor()
	cur.execute("SELECT sum(amount) FROM 'records' WHERE nature='OUT'")
	total_exp=cur.fetchall()
	cur.execute("SELECT sum(amount) FROM 'records' where nature='IN'")
	total_inc=cur.fetchall()
	bal=total_inc[0][0]-total_exp[0][0]
	con.close()
	return bal

create()