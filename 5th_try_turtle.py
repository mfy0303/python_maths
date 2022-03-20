from turtle import*
shape('turtle')
speed(100)
r=5
for i in range(60):
	for i in range(10):
		for i in range(7):
			forward(r)
			right(180-(7-2)*180/7)
		r=r+1
		right(5)
	r=r-3	
