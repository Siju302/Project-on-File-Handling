# open the file in read mode
file_read = open('Stundentinfo.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Stundentinfo.txt', 'w')
# write in the file
file_write.write("File in write mode ....")
file_write.write("6. Joseph 15 Physics")
file_write.close()

# open the file in append mode
file_append = open('Stundentinfo.txt', 'a')
# append in the file
file_append.write("\n File in append mode ....")
file_append.write("6. Joseph 15 Physics")
file_append.close()