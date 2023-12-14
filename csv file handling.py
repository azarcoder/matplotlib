import csv 
with open('sample.csv') as myfile:
    #reader = csv.DictReader(myfile) it read like dictionary
    reader = csv.reader(myfile)#return return list of our csv data
    #row=next(reader)#read row by row. next takes one row
    #row = next(reader)
    #print(*reader) print everything inside reader
    for i in reader:
        print(i)