import random
import time
def bubble(a):
	anew = a
	length = len(anew) - 1
	while(length > 0):
		place = 0
		for i in range(0, length):
			if anew[i] > anew[i+1]:
				(anew[i], anew[i+1]) = (anew[i+1], anew[i])
		length -= 1
	return anew

b = []
for c in range(1000):
	b.append(random.randint(1,10000))

current = int(round(time.time() * 1000))


check = bubble(b)


current2 = int(round(time.time() * 1000))


print check
print current
print current2