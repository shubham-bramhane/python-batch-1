# # import math

# # class rightangle():
# #     def __init__(self,left_side,hypo):
# #         # self.right_side=right_side
# #         self.left_side=left_side
# #         self.hypo=hypo

# #     # def result(self):
# #     #     new=self.right_side**2+self.left_side**2
# #     #     hypo=math.sqrt(new)
# #     #     print('the hypotenous is :-',hypo)

# #     def right_side_value(self):
        
# #         right_side=math.sqrt((self.hypo**2)-(self.left_side**2))
# #         print("the right side is",right_side)


# # a=c-b



# # tringle1=rightangle(3,4)
# # tringle1.right_side_value()

# # velocity=distance/time


# class volume():
#     def __init__(self,radius):
#         self.radius=radius

#     def result(self):
#         new=(4/3)*3.142*(self.radius)**3
#         print('volume of planet',new)


# class circumference(volume):
#     def __init__(self, radius):
#         super().__init__(radius)

#     def result2(self):
#         new=2*3.142*self.radius
#         print('circumference of planet',new)



# earth=circumference(6371)
# earth.result2()
# earth.result()


from unicodedata import name


class area():
    def __init__(self,length,breadth):
        self.lenght=length
        self.breadth=breadth

    def result(self):
        print('arrea of rectangle',self.lenght*self.breadth)



class volume(area):
    def __init__(self, length, breadth,height):
        super().__init__(length, breadth)
        self.height=height

    def result2(self):
        print('volume of rectanlge',self.lenght*self.height*self.breadth)



rectangle1=volume(10,20,30)
rectangle1.result()





class User():
    def __init__(self,name,password):
        self.name=name
        self.password=password




new=User.obzject.filter(id=1)





















