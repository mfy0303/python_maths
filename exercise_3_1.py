print("您嘞想求几个数的公因数？")
len_num=int(input())
r=1
b=0
all_num=[]
biggest_list=[]
answer_list_begin=[]
answer_list_over=[]
x1=0
x2=0
u=0
for i in range(len_num):
	print("请输入第%d个数～"%(r))
	all_num.append(int(input()))
	r=r+1
def factors(number):
	f_list=[]
	for i in range(1,number+1):
		if number % i == 0:
			f_list.append(i)
	return f_list
for i in range(len(all_num)):
	biggest_list.append(factors(all_num[i]))
for x in range(len(biggest_list[0])):
	for i in range(len(biggest_list)):
		for y in range(len(biggest_list[i])):
			if biggest_list[i][y]==biggest_list[x1][x2]:
				answer_list_begin.append(biggest_list[i][y])
	x2=x2+1
answer_list_begin.sort(reverse=True)
x=answer_list_begin[b]
res=answer_list_begin.count(x)
running=True
while running:
	if res == len(biggest_list):
		running=False
	else:
		b=b+1
		x=answer_list_begin[b]
		res=answer_list_begin.count(x)
print("这%d个数的最大公因数是%d～"%(len_num,x))
