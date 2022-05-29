data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #和count = count + 1 相等
		if count % 1000 == 0: #和1000求餘數=0
			print(len(data)) #print 很花時間
print(len(data))

print(data[0])
print('------------------')
print(data[1])