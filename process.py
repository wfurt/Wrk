#!/usr/bin/python
import math

def stdev(vals):
	d=0
	avg=sum(vals)/len(vals)
	for v in vals:
		d += pow(avg-v,2)
	#print "d=", d
	#print math.sqrt(d/(len(vals)-1))
	return math.sqrt(d/(len(vals)-1))

f = open("results.txt")
lines = f.readlines()
f.close()

rps=[]
transfer=[]
for line in lines:
	t, v = line.split()
	if t == 'Transfer/sec:':
	    transfer.append(float(v.split('.')[0]))
	elif t == 'Requests/sec:':
	    rps.append(float(v.split('.')[0]))
	else:
	    print "Unkonwn type:"
	    raise
	    
	#print(line)

rps_a = sum(rps)/len(rps)
transfer_a = sum(transfer)/len(transfer)

print "               avg    min    max    stdev"
print "Reqs/s    : %6d %6d %6d %6d " % ( rps_a, min(rps), max(rps), stdev(rps))
print "Transfer/s: %6d %6d %6d %6d " % ( transfer_a, min(transfer), max(transfer), stdev(transfer))
