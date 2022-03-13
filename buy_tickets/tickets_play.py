print("欢迎咨询购票问题答案～")
def choices():
	print("您可以有以下选择：")
	print("1.了解什么是购票问题")
	print("2.购票问题求解")
	print("0.退出")
def factorial(fac):
	answer_of_fac=fac
	for i in range(1,fac):
		answer_of_fac=answer_of_fac*i
	return answer_of_fac
choices()
choice=int(input())
while choice != 0:
	if choice == 1:
		print("购票问题是一种排列组合类型题，\n指的是有持有大面值与小面值两种人来购票，\n票价一般等于小面值之价，\n大面值之价通常是小面值的2倍。\n而售票员此时无钱找零，\n问游客们有多少种排列方法不使售票员陷入无法找零的尴尬局面。")
		choices()
		choice=int(input())
	elif choice == 2:
		print("请输入持有小面值者人数～")
		x=int(input())
		print("请接着输入持有大面值者人数～")
		y=int(input())
		x_fac=factorial(x)
		y_fac=factorial(y)
		xy_fac=factorial(x+y)
		xp1_fac=factorial(x+1)
		yd1_fac=factorial(y-1)
		answer_of_buy_tickets=xy_fac/(y_fac*x_fac)-xy_fac/(yd1_fac*xp1_fac)
		print(int(answer_of_buy_tickets))
		choices()
		choice=int(input())
	else:
		print("对不起，无该选项～")
		choices()
		choice=int(input())
print("退出计算......")
