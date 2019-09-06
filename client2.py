from json import loads
from socket import socket
from base64 import b64decode
def main():
	client=socket()
	client.connect(('192.168.0.102',5577))
	indata=bytes()
	data=client.recv(1024)
	while data:
		indata+=data
		data=client.recv(1024)
	client.close()
	jdata=indata.decode('utf-8')
	mydict=loads(jdata)
	filename=mydict['filename']
	filedata=mydict['filedata']
	with open('D:/python/'+filename,'wb') as f:
		f.write(b64decode(filedata))
	print('图片已保存！')

if __name__ == '__main__':
	main()


