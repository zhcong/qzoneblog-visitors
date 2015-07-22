#!python
# coding=utf-8
import qqlib, getpass, json, time, sys, codecs

reload(sys)
sys.setdefaultencoding(sys.stdin.encoding)

visitor=[]
fp=codecs.open('visitors.log','a',sys.stdin.encoding)
def ut2t(uttime):
	#unix time to date
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(uttime)))

def getjson(str):
	str=str.replace('_Callback(','')
	str=str.replace(');','')
	re=json.loads(str)
	return re

def justdoit():
	jsonstr=qq.getblogvisit(blogid,vqqid)
	jsondate=getjson(jsonstr)
	for i in range(0,len(jsondate['data']['list'])):
		if jsondate['data']['list'][i]==None:
			break
		vuin=jsondate['data']['list'][i]['uin']
		vname=jsondate['data']['list'][i]['name']
		vtime=jsondate['data']['list'][i]['time']
		flag=False
		for visi in visitor:
			if(visi['uin']==vuin and visi['time']==vtime):
				flag=True
				break
		if flag:
			continue
		visitoradd={'name':vname,'uin':vuin,'time':vtime}
		visitor.append(visitoradd)
		fp.write('\n'+str(vname.decode(sys.stdin.encoding))+'\t\t\t\t\t'+str(vuin)+'\t\t\t\t\t'+str(ut2t(float(vtime))))
	return jsondate['data']['viewCount']

qqid=raw_input("QQ number:")
qqpaswd = getpass.getpass('QQ password:')
blogidstr=raw_input("blog number(blog number,qq number):")
blogidspl=blogidstr.split(',')
blogid=blogidspl[0]
vqqid=None
if(len(blogidspl)>1):
	vqqid=blogidspl[1]
timepause=int(raw_input('Pause(seconds, at last 15s):'))
if timepause<15:
	timepause=15
qq=qqlib.QQ(qqid,qqpaswd)
qq.login()
print 'login success!'
while True:
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+', '+str(justdoit())+' peoples.\n'
	time.sleep(timepause)
fp.close()