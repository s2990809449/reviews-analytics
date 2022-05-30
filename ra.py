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

# 留言篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言小於100個字')
print(new[0])

# 另外一個篩選
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言有good')
print(good[0])

# list comprehension(清單快寫法)
good = [d for d in data if 'good' in d]
# output = [(運算) for (變數) in (清單) if 篩選條件]
print('一共有', len(good), '筆留言有good')

bad = ['bad' in d for d in data]
# 'bad' in d 是是非題
print(bad)

# 也可以寫成這樣
bad = []
for d in data:
	bad.append('bad' in d)
