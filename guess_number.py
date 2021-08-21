#產生一個隨機數給使用者猜
#猜錯 要告訴他比答案大/小
import random

r = random.randint(1,100)

while True:
	num = input('請猜一個數字 1~100: ')
	if int(num) == r:
		print('猜對了~', r)
		break
	elif int(num) > r:
		print('你的答案比real number大')
	elif int(num) < r:
		 print('你的答案比real number小')
