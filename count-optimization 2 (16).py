import random
dic={}
raw_data_list=[random.randint(0,500) for i in range(10000)]
print(f"{raw_data_list[0:100]} ......")
end_number=0
for i in range(len(raw_data_list)):
    value=raw_data_list[i]     
    if value in dic.keys():
        dic[value]+=1
    else:
        dic[value]=1
most=max(dic.values())
key=list(dic.keys())[list(dic.values()).index(most)]
print(f"{key} appears {most} times")