# counter = 0

# while counter < 3:
#     print("name?")
#     counter += 1
    
    
# for i in range(3):
#     print('hi')



# print('hi\n' * 3, end='')

hiTimes = int(input('how mant hi times?'))
while hiTimes < 1:
    hiTimes = int(input("more hi times"))

else:
    print('hi\n' * hiTimes, end='')
    