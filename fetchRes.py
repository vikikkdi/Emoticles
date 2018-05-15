import getcontent
import getresult
import re

def finalres(url):
	a = getcontent.getText(url)

	title = a[0]
	content = a[1]
	description = content[:100]+'.....'

	sss = re.sub('"',"'",content)
	sss = '"'+sss+'"'
	d = getresult.getResult(sss)
	sss = re.sub(':','-',title)
	sss = '"'+sss+'"'
	d1 = getresult.getResult(sss)
	s = d.split(':')
	s1 = d1.split(':')
	result = []
	result1 = []

	for i in s:
		m = i.split(',')
		result.append([m[0],int(m[1])])
	result = result[:-1]

	for i in s1:
		m = i.split(',')
		result1.append([m[0],int(m[1])])

	for i in result:
		if i[0]=='joy':
			i[1]-=5
			break

	result = sorted(result,key=lambda x:x[1],reverse=True)
	result1 = sorted(result1, key=lambda x:x[1], reverse=True)

	se = result[:3]
	se.append(result1[0])
	se.append(result1[1])
	se.append(result1[2])

	result = sorted(se, key=lambda x:x[1], reverse=True)

	r = result[:3]
	if r[0][0]=='positive' and r[1][0]=='negative':
		r[1][0] = result[3][0]
	elif r[0][0]=='positive' and r[2][0]=='negative':
		r[2][0] = result[3][0]
	elif r[0][0]=='negative' and r[1][0]=='positive':
		r[1][0] = result[3][0]
	elif r[0][0]=='negative' and r[2][0]=='positive':
		r[2][0] = result[3][0]	

	se = {i[0] for i in r}
	if len(se)==2:
		se.add(result[4][0])
	if len(se)==2:
		se.add(result[5][0])

	h = ""
	coun=0

	for i in se:
		if coun==3:
			break
		h+=i+'`'
		coun+=1

	h+=title+'`'+description+"`"+url

	return h


if __name__=='__main__':
	finalres('https://en.wikipedia.org/wiki/Iron_Man_(2008_film)')