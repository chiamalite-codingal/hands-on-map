num1 = [3,4,5]
num2 = [6,7,8]
res = map(lambda x,y:x+y, num1,num2) #comprehension
print(list(res))
#map
num =[3,4,5,6,7]
def square(n):
    return n*n
sq = list(map(square,num))
print(sq)