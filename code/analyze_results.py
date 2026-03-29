import datetime
print("Roll Number: 727823TUCY033")
print("Timestamp:", datetime.datetime.now())
counts = {}
f = open('/tmp/auth_test.log', 'r')
for line in f:
    if "Failed" in line:
        ip = line.split()[10]
        counts[ip] = counts.get(ip, 0) + 1
f.close()
print("\n--- SIEM Analysis Report ---")
print("Total suspicious IPs found:", len(counts))
most_suspicious = max(counts, key=counts.get)
print("Most dangerous IP:", most_suspicious, "| Attempts:", counts[most_suspicious])
print("Report complete!")
