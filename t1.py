from turtle import *

speed('slowest')
pencolor('red')

#in range function a single value is a stop value.for ex range 10 will create ten memory spaces .
#range(start,stop)
#range(starrt,stop,step)
for  i in range(6): 
     fd(120)
     lt(360/6)
     dot(10,"yellow")
     write(i, font= 'calibri')
'''for  i in range(3,12): 
     fd(120)
     lt(360/10)
     dot(10,"yellow")
     write(i, font= 'calibri')'''
'''for  i in range(6,40,5): 
     fd(120)
     lt(360/10)
     dot(10,"yellow")
     write(i, font= 'calibri')'''
goto(100,100)
for i in range(6,0,-1):
     fd(120)
     lt(360/6)
     dot(10,"yellow")
     write(i, font= 'calibri')

mainloop()