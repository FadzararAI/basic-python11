# nama = []
# # file = open('coba.txt','r')
# # for i in file.readlines():
# # 	i = i.replace('\n','')
# # 	nama.append(i)
# # file.close()
# # print(nama)
# with open('coba.txt','r') as file:
# 	for i in file.readlines():
# 		i = i.replace('\n','')
# 		nama.append(i)
# print(nama)
from os import remove
remove("coba.txt")