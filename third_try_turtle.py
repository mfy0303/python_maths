from turtle import*
def shape_drawing(line):
	turn=(line-2)*180/line
	for i in range(line):
		forward(50)
		right(180-turn)
print("请输入多边形边数～")
line_true=int(input())
if line_true >= 3:
	shape("turtle")
	speed(1)
	shape_drawing(int(line_true))
	while True:
		pass
else:
	print("WRONG")	
