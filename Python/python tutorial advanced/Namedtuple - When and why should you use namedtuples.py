color = (50,155,255)
print(color[0])

#instead of above we can use named tuple so it's much easier to read and you won't forget whats going on later

#extra notes :namedtuple returns a class (that's a child of the built-in class tuple).
# The first argument you pass to namedtuple becomes the name of the class, while the list of strings becomes the attributes (data fields). You can then call the constructor (the line of code before the print() method in the video) to make objects.

from collections import namedtuple

Color = namedtuple('Color_class', 'red green blue') #can use any iterable as well like list eg  ['red','green','blue']
color = Color(50, 155, 255)
white = Color(255, 255, 255)

#treat Color as class
random_color = Color(40,38,89)
print(random_color)
print(random_color.green,random_color.red)
print(random_color._asdict())
print(random_color._fields)
new_random_color = random_color._replace(green=154) #we have to use this method like this because it return a value like sorted() function
print(new_random_color.green)

#can also use dictionary but it needs more writing not recommended
# color = {'red': 50, 'green': 155, 'blue': 255}
# print(color['green'])


