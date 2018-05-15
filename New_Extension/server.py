from flask import Flask, request, session
import MySQLdb
import datetime

app = Flask(__name__,static_url_path = "")

@app.route('/getPlans', methods = ['POST'])
def getPlans():
	data = request.data
	data = str(data,'utf-8')
	#print(data)
	db = MySQLdb.connect("127.0.0.1","root","deepak123","dk")
	cursor = db.cursor()
	query = "select id from carriers where name='%s'"%(data)
	try:
		cursor.execute(query)
		res = cursor.fetchall()
		cID = ""
		for row in res:
			cID = row[0]
		query = "select * from plans where id=%d"%(cID)	
		cursor.execute(query)
		res = cursor.fetchall()
		plans = ""
		for row in res:
			plans+=row[0]+":"+row[2]+":"+str(row[3])+","
		return plans
	except Exception as e:
		raise e


@app.route('/login', methods = ['POST'])
def login():
	data = request.data
	data = str(data,'utf-8')
	db = MySQLdb.connect("127.0.0.1","root","deepak123","dk")
	cursor = db.cursor()
	query = "select password from user where email='%s'" %(data)
	try:
		cursor.execute(query)
		res = cursor.fetchall()
		print(data)
		if(len(res) == 0):
			return "wrongEmail"
		else:
			session['username'] = data
			for row in res:
				return row[0]
	except Exception as e:
		raise e


@app.route('/register', methods = ['POST'])
def register():
	data = request.data
	data = str(data,'utf-8')
	em,pwd = data.split("&")
	db = MySQLdb.connect("127.0.0.1","root","deepak123","dk")
	cursor = db.cursor()
	query = "insert into user(email,password) values('%s','%s')"%(em,pwd)
	try:
		cursor.execute(query)
		db.commit()
		session['username'] = em
		return "Done"
	except Exception as e:
		raise e


@app.route('/getUser',methods = ['POST'])
def getUser():
	if 'username' in session:
		username = session['username']
		return username
	else:
		return "no"


@app.route('/logout',methods = ['POST'])
def logout():
	session.pop('username', None)
	return ""

@app.route('/addTransaction', methods = ['POST'])
def addTransaction():
	data = request.data
	data = str(data,'utf-8')
	data = data.split('&')
	#print(data)
	email, mob, plan = data[0], data[1], data[2]
	db = MySQLdb.connect("127.0.0.1","root","deepak123","dk")
	cursor = db.cursor()
	timeStamp = str(datetime.datetime.now())
	#print(email,'\n',mob,'\n',plan,'\n',timeStamp)
	query = "insert into transactions(email,mobile,plan,dets) values('%s','%s','%s','%s')"%(email,mob,plan,timeStamp)
	try:
		cursor.execute(query)
		db.commit()
		return "Done"
	except Exception as e:
		raise e

@app.route('/add', methods = ['POST'])
def add():
	data = request.data
	data = str(data,"utf-8")
	a, b = data.split(",")
	print(str(int(a)+int(b)))
	return str(int(a)+int(b))


if __name__ == '__main__':
	app.secret_key = 'any random string'
	app.run(host='localhost',debug = True)