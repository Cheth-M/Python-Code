import csv
def main():
    file=open("C:/Users/cheth/PycharmProjects/apstats/music.csv","r")
    csvreader=csv.reader(file)
    header=[]
    header=next(csvreader)

    header=header[1:]
    print(header)
    rapfan=0
    popandrap=0
    for row in csvreader:
        if int(row[6]) >= 4 and int(row[10]) >= 4:
           popandrap += 1
           rapfan += 1
        elif int(row[10])>=4:
            rapfan+=1

    print ("people who like both " + str(popandrap))
    print("people who like pop " + str(rapfan))
    print (popandrap / rapfan)
if __name__ == "__main__":
    main()