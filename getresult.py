import subprocess
import re
import json
#subprocess.call("Rscript getnrc.R")
def getResult(text):
	a = subprocess.check_output ("/usr/local/bin/Rscript getnrc.R "+re.sub(' ',':',text), shell=True)
	st = re.sub('\s',':',a.decode('utf-8'))
	st = re.sub(':+',':',st)
	st = st[1:]
	s = st.split(':')
	emotion = s[:10]
	score = s[10:]
	s = {emotion[i]:int(score[i]) for i in range(len(emotion))}
	h = ""
	for i, j in s.items():
		h+=i+','+str(j)+':'
	
	print(h)
	return h[:-1]

if __name__=='__main__':
	print(getResult('hello how are you i am happy'))