# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')



# colors = ['red', 'green', 'blue']
# data =open('file.txt', 'w')
# # data.writelines(colors) # разделителей не будет
# data.write('line 1, 23 \n')
# data.write('line 234\n')
# data.close()


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

