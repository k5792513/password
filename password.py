
password = 'a123456'
x = 3
while True:
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('你已經成功登入')
		break
	else:
		x = x - 1
		print('密碼錯誤！你還有', x, '機會')
		if x == 0:
			break