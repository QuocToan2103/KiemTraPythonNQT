# from math import sqrt

# # def docFile():
# #     file = open('input.txt','r',encoding='utf-8')
# #     for line in file:
# #         print(line.strip())
# #     file.close()
# # docFile()    

# # class Shape:
# #     def chuvi(shape):
# #         a = int(input())
# #         b = int(input())
# #         c = int(input())
# #         p = (a + b + c) / 2
# #         print('Chu vi: ',p)
# #         print('Dien tich: ',sqrt(p*(p-a)*(p-b)*(p-c)))

# #     # def dientich(shape):
# #     #     a = int(input())
# #     #     b = int(input())
# #     #     c = int(input())
# #     #     p = (a + b + c) / 2
# #     #     print('Chu vi: ',p)
# #     #     print('Dien tich: ',sqrt(p*(p-a)*(p-b)*(p-c)))



from abc import ABC,abstractmethod 

class Shape(ABC): 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def chuVi():
        pass
    @abstractmethod
    def dienTich():
        pass