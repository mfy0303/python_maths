print("您嘞想求多少个数的平均值？")
len_num=int(input())
r=1
d=[]
for i in range(len_num):
	print("请输入第%d个数～"%(r))
	d.append(int(input()))
	r=r+1
answer=sum(d)/len_num
print(answer)
