class Rectangle():
    def __init__(self,lengh,breadth,height):
        self.lengh=lengh
        self.breadth=breadth
        self.height=height

    def rectanglearea(self):
        print('area of rectangle',(self.lengh*self.breadth))

    def volume_of_rectangle(self):
        print('volume of  rectangle',(self.lengh*self.breadth*self.height))    


shubham=Rectangle(10,20,40)
liladhar=Rectangle(20,40,50)

shubham.rectanglearea()
shubham.volume_of_rectangle()
liladhar.rectanglearea()