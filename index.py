from flask import Flask, request
import fetchRes
import MySQLdb
import re

app = Flask(__name__,static_url_path = "")

@app.route('/sendURL', methods = ['POST'])
def sendURL():
	data = request.data
	data = str(data,'UTF-8')
	print(data)
	result = fetchRes.finalres(data)
	print(result)
	return (result)

@app.route('/addArticles', methods = ['POST'])
def addArticles():
	data = request.data
	data = str(data,'UTF-8')
	data = data.split('`')
	url = data[-3]
	url = re.sub('\'','',url)
	description = data[-2]
	description	= re.sub('\'','',description)
	title = data[-1]
	title = re.sub('\'','',title)
	data = data[:-3]
	db = MySQLdb.connect("localhost","root","vikikkdi","codefundo")
	for i in data:
		print(i)
		sql="select max(id) from links"
		cursor = db.cursor()
		try:
			cursor.execute(sql)
			result = cursor.fetchall()
			id = int(result[0][0])+1
			sql = "select id from links where link='%s'"%(url)
			cursor.execute(sql)
			result = cursor.fetchall()
			print(len(result))
			print(result)
			if len(result)==0:
				print(url,title,description)
				sql = "insert into links values(%d,'%s','%s','%s')"%(id,url,title,description)
				cursor.execute(sql)
				db.commit()
			else:
				id = int(result[0][0])
				print('ID ::',id)
			sql = "select id from emotions where name='%s'"%(i)
			cursor.execute(sql)
			result = cursor.fetchall()
			print(result[0][0])
			li = result[0][0].split('`')
			li.append(str(id))
			print('LIST SIZE ::',len(li))
			li = list(set(li))
			print(li)
			new_id = '`'.join(li)
			print(new_id)
			if new_id[0]=='`':
				new_id=new_id[1:]
			sql = "update emotions set id='%s' where name='%s'"%(new_id,i)
			cursor.execute(sql)
			db.commit()
			return "done"
		except Exception as e:
			print(e)
	return "done"

@app.route('/displayArticles', methods = ['POST'])
def displayArticles():
	db = MySQLdb.connect("localhost","root","vikikkdi","codefundo")
	cursor = db.cursor()
	msg = ""
	try:
		sql = "select * from emotions"
		cursor.execute(sql)
		result1 = cursor.fetchall()
		for _ in result1:
			emotion = _[0]
			ids = _[1].split('`')
			msg+=emotion+'|'
			print(ids)
			if len(ids)==1 and ids[0]=='':
				msg+=';'
				continue
			links = []
			for i in ids:
				print(i)
				sqq = "select * from links where id=%d"%(int(i))
				cursor.execute(sqq)
				#links.append(cursor.fetchall())
				res = cursor.fetchall()
				for row in res:
					msg+=row[1]+'`'+row[2]+'|'
			msg+=';'
		print(msg)
		return msg;
	except Exception as e:
		print(e)
	return "done"

@app.route('/searchArticles', methods = ['POST'])
def searchArticles():
	print("HERE")
	db = MySQLdb.connect("localhost","root","vikikkdi","codefundo")
	cursor = db.cursor()
	data = request.data
	data = str(data,'UTF-8')
	dataL = data.split()
	msg = ""
	try:
		sql = "select * from emotions"
		cursor.execute(sql)
		result1 = cursor.fetchall()
		for _ in result1:
			emotion = _[0]
			ids = _[1].split('`')
			msg+=emotion+'|'
			print(ids)
			if len(ids)==1 and ids[0]=='':
				msg+=';'
				continue
			links = []
			for i in ids:
				print(i)
				sqq = "select * from links where id=%d"%(int(i))
				cursor.execute(sqq)
				#links.append(cursor.fetchall())
				res = cursor.fetchall()
				for row in res:
					flag = False
					st = row[2].lower()
					for i in dataL:
						if i.lower() in st:
							flag = True
							break
					if flag:
						msg+=row[1]+'`'+row[2]+'|'
			msg+=';'
		print(msg)
		return msg;
	except Exception as e:
		print(e)
	return "done"


if __name__ == '__main__':
	app.run(host='localhost',debug = True)
