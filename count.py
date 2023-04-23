import random
import time
dic={}
#生成一个具有随机整数的list
raw_data_list=[]
for i in range(100000):
    raw_data_list.append(random.randint(0,50000))
print(raw_data_list)
#处理raw data list
time.sleep(1)
processed_data_list=sorted(raw_data_list)
print(f"Here is a processed data list: processed_data_list")
time.sleep(1)
print(processed_data_list)
#开始筛选
end_number=0
for i, value in enumerate(processed_data_list):
    if value == processed_data_list[i-1]:
        dic.update({value : i-end_number+1 })
    if value != processed_data_list[i-1]:
        end_number = i
        dic.update({value : i-end_number+1 })
print(dic)
keys = list(dic.keys())
values = list(dic.values())
max_value = max(values) # 求列表最大值
max_idx = values.index(max_value) # 求最大值对应索引
print(f"{keys[max_idx]} appears {max_value} times")
