import random

d=0
p=0

while True:
	r=input("press r to roll,q to quit:")

	if r == 'r':
		d ==random.randint(1,6)
		print("u got :")
		if d == 6:

			print("congo,u can play now")
			break
		else:
			print("roll again,till u get 6")

while True:
	r =input("press r to roll,q to quit :")

	if r =='r':
		d == random.randint(1,6)
		print("u got :",d)

		p = p+d
		if p>100:
			print("u cant go")
			p = p-d
			print("wait till u get",100==p,"or less")

		print("ur new position is :",p)

		if p==100:
			print("wooo u win")
			exit()
		if p==8:
			p=37
			print("a ladder,go to",p)

	elif r=='q':
		print("byeee")
		exit()		

