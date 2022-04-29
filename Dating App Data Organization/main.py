import csv


def main():
    file=open("/Users/chethmittal/PycharmProjects/Youaifwantsadate_analysis/DatingAppReviewsDataset.csv")
    c=csv.reader(file)
    tindercounter=0
    bumblecounter=0
    othercounter=0
    Hingecounter=0
    sumrevtin=0
    total=0
    header=next(c)
    app = 6
    Name = 1
    Review = 2
    Rating = 3
    Thumbs_up = 4
    datetime = 5

    print (header)
    bumble_sum = 0
    hinge_sum =0
    for row in c:
        if row[0].isalpha():
            continue
        elif row[app] == "Tinder":
            tindercounter+=1
            sumrevtin+=int(row[Rating])
        elif row[app] == "Bumble":
            bumblecounter += 1
            bumble_sum += int(row[Rating])
        elif row[app] == "Hinge":
            Hingecounter+=1
            hinge_sum += int(row[Rating])
        total+=1

    print (tindercounter)
    print(Hingecounter)
    print(bumblecounter)
    print(total)
    print (sumrevtin/tindercounter)
    print ("hinge average: " + str(hinge_sum/Hingecounter))
    print("bumble average: " + str(bumble_sum / bumblecounter))
if __name__ == "__main__":
    main()
