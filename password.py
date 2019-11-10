
password = 'a123456'
x = 3
while x  > 0:
	x = x - 1
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('你已經成功登入')
		break
	else:
		print('密碼錯誤')
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('帳號被鎖，請洽管理員')