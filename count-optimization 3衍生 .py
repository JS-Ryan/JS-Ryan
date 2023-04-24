import random
k=[]
raw_data_list=[random.randint(0,500) for i in range(10000)]
print(raw_data_list)
for i, value in enumerate(raw_data_list):
    p=raw_data_list.count(value)
    k.append(p)
num=max(k)
print(f"{raw_data_list[k.index(num)]} appears {num} times")