myfile = open('myfile.txt', 'w')      #Open for text output:create/empty0$$$
myfile.write('hello text file\n')
myfile.write('goodby text file\n')
myfile.close()

myfile = open('myfile.txt')    #opens file
myfile.readline()              #reads line by line
myfile.readline()