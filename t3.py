from turtle import*
speed('fastest')
colors = ['red','yellow','blue','green','pink']

for i in range(100):
    pencolor(colors[i%5])
    fd(i*5)
    lt(60)
    circle(i*2,90)

mainloop()
