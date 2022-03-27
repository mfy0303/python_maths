print("输入鸡与兔的总脚数～")
all_foot=int(input())
print("输入鸡与兔的总只数～")
all_numbers=int(input())
rabbit_num=(all_foot)/2-all_numbers
chicken_num=all_numbers-rabbit_num
print("兔有%d只，鸡有%d只"%(rabbit_num,chicken_num))
