class Cookie:
    def __init__(self,color):
        self.color = color

    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color


cookieOne = Cookie('red')
cookieTwo = Cookie('yellow')

print('cookie one color is: ',cookieOne.getColor() )

print('cookie TWO color is: ',cookieTwo.getColor() )

cookieOne.setColor('PINK')
print('cookie ONE color is: ',cookieOne.getColor() )