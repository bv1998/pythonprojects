#multiple txt files to csv files converter
#Bryan Vernon - 2019
import csv
#p is the start number of the txt file
p = 1
#c is the start number of the csv file that will be exported
c = 1027

while p < 36:
    if p < 36: 

        # "##" means where the file name and path should go
        f = open("##"+ str(p) + ".txt", encoding="utf8", errors='ignore')

        x = f.readlines()
        s = []


        for i in x:
            s.append(i)

        print(s)

        # "##" means where the file name and path should go
        csvex = csv.writer(open("##" + str(c) + ".csv","w"), delimiter="," , quotechar=",")
        csvex.writerow(s)
        p = p + 1
        c = c + 1
    else:
        exit()