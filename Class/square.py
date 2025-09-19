class square():
    def area(self):
        s=int(input('Enter the side.'))
        area=s*s
        print('Area-',area)
        return area 
    def perimeter(self):
        s=int(input('Enter the side.'))
        perimeter=s*4
        print('Perimeter',perimeter)
        return perimeter
        
answer=square()
answer.area()
answer.perimeter()