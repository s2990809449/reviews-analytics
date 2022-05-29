data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #和count = count + 1 相等
		if count % 1000 == 0: #和1000求餘數=0
			print(len(data)) #print 很花時間
print('檔案讀取完了，總共有', len(data), '筆資料')

with open('reviews.txt', 'r') as a:
	for line in a:
		data.append(line)

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言的平均長度:', sum_len/len(data))
