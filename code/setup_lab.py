import datetime
import random
print("Roll Number : 727823TUCY033")
print("Timestamp: ", datetime.datetime.now())

ips = ['192.168.1.5','10.0.0.9','172.16.0.3']
users = ['root','admin','pavithra']

f = open('/tmp/auth_test.log', 'w')
for i in range(50):
	ip = random.choice(ips)
	user = random.choice(users)
	f.write('Mar 29 12:00:0{} webserver sshd[1234]: Failed password for {} from {} port 22 ssh2\n'.format(i%9, user, ip))
f.close()

print("Setup complete! Log file created at /tmp/auth_test.log")

