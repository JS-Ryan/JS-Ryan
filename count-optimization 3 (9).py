import random
raw_data_list=[random.randint(0,500) for i in range(10000)]
print(raw_data_list)
num=int(input("which number do you want to count:"))
print(raw_data_list.count(num))