r=float(input('enter cylinder radius :'))
h=float(input('enter cylinder height : '))
pi=3.14
perimeter=2*pi*r
circlearea=pi*r*r
sidearea=perimeter*h
volume=circlearea*h
totalarea=2*circlearea+sidearea
print('volume = ', volume)
print('totalarea =', totalarea)
print('sidearea =', sidearea)
