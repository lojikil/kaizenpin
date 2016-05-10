import socket
import re
import time


"Are you human? Answer this question: 37 - 56 = "
find = re.compile(": (\d+)\s(.)\s(\d+)")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('challenges.kaizen-ctf.com', 31337))
line = s.recv(8192)
print line
matches = find.findall(line)[0]
print matches[0], matches[1], matches[2]
res = str(eval(' '.join(matches))) + '\n'
time.sleep(5)
print res
s.sendall(res)
line = s.recv(8192)
print "result: ", line
print len(line)
s.close()
