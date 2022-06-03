import math

#La regla principal que da origen al triángulo es que 2 de sus lados sean mayores al 3er lado

def check_triangle(sides):

    a = sides[0]
    b = sides[1]
    c = sides[2]
    #if(((a+b)> c)or((b+c)>a)or((a+c)>b)):
    if((a+b)>c) and (b<(a+c)):
        print("This is a triangle")
        type_triangle(a,b,c)
    else:
        print("This is not a triangle")

def type_triangle(a,b,c): 	
    if (a==b==c):
        print('This is Equilateral')
    elif ((a==b)or(b==c)or(a==c)):
        print('This is Isosceles')
    else:
        print('This is Scalene')

def main():
    result=0
    sides=[0,0,0]
    sides[0] = int(input("Enter side of slide a \n" ))
    sides[1] = int(input("Enter side of slide a \n" ))
    sides[2] = int(input("Enter side of slide a \n" ))

    check_triangle(sides)
   
if __name__ == "__main__":

    main()
