# student_name: Pavithra
# roll_number: 727823TUCY033
# project_name: SKCT_727823TUCY033_LogAnalysis
# date: 2026-03-29

import datetime

print("Roll Number: 727823TUCY033")
print("Timestamp:", datetime.datetime.now())

LOG_FILE = "/tmp/auth_test.log"
THRESHOLD = 5

def test_case_1():
    print("[TC1] Brute Force Detection")
    counts = {}
    f = open(LOG_FILE, "r")
    for line in f:
        if "Failed" in line:
            ip = line.split()[10]
            counts[ip] = counts.get(ip, 0) + 1
    f.close()
    for ip, count in counts.items():
        if count > THRESHOLD:
            print("ALERT: Unauthorized access from", ip, "| Attempts:", count)

def test_case_2():
    print("[TC2] Multiple Users Attacked from Same IP")
    users_per_ip = {}
    f = open(LOG_FILE, "r")
    for line in f:
        if "Failed" in line:
            ip = line.split()[10]
            user = line.split()[8]
            if ip not in users_per_ip:
                users_per_ip[ip] = []
            users_per_ip[ip].append(user)
    f.close()
    for ip, users in users_per_ip.items():
        if len(users) > 3:
            print("ALERT: IP", ip, "tried usernames:", set(users))

def test_case_3():
    print("[TC3] Root Login Attempts Specifically")
    spe = {}
    f = open(LOG_FILE, "r")
    for line in f:
        if "Failed" in line and "root" in line:
            ip = line.split()[10]
            spe[ip] = spe.get(ip, 0) + 1
    f.close()
    for ip, count in spe.items():
        if count > 3:
            print("ALERT: Root attack from", ip, "| Attempts:", count)

test_case_1()
test_case_2()
test_case_3()
