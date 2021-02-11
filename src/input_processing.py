import os
import re
import numpy
import pandas as pd

'''
dataframe format 
"{timestamp}:{Memory Allocated}:{Memory Used}:{CPU Allocated}:{CPU
Used}:{Network bandwidth utilization}:{Storage space utilization}"

'''

data = []
for folder in sorted(os.listdir('/home/kali/Desktop/TSdataset/group82_resource_utilization')):
    for file_log in sorted(os.listdir('/home/kali/Desktop/TSdataset/group82_resource_utilization/'+folder)):
	folder_name = re.split('_*_', folder)
	with open('/home/kali/Desktop/TSdataset/group82_resource_utilization/'+folder+'/'+file_log) as lines:
    		lines = lines.readlines()
	for line in lines:
		part = line.split(":")
		if len(part) >= 8:
			data.append((str(folder_name[0]+folder_name[1]), str(folder_name[2]), str(part[0][1:])+":"+str(part[1])+":"+str(part[2].split('\"')[0]), str(part[3].split('\"')[1]), part[4], part[5], part[6], part[7], part[8].split('\"')[0]))
df = pd.DataFrame(data, columns=['group', 'instance', 'timestamp', 'Memory_Allocated', 'Memory_Used', 'CPU_Allocated', 'CPU_Used', 'Network_bandwidth_utilization', 'Storage_space_utilization'])
print(df)
