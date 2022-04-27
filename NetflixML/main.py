import  csv
import math
def train(file):
    csvreader=csv.reader(file)
    header=next(csvreader)
    noy={}
    y={}
    prob={}
    for i in range (len(header)):
        noy[i] = 0
        y[i] = 0
        prob[i] = 0
    counter=0
    dislike=0
    liked=0
    for row in csvreader:
        label=int(row[-1])
        counter+=1
        for i in range(len(row) - 1):
            if int(row[i]) == 1:
                prob[i] += 1
        if label == 0:
            dislike+=1
            for i in range(len(row)-1):
                if int(row[i])==1:
                    noy[i]+=1
        else:
            liked+=1
            for i in range(len(row) - 1):
                if int(row[i]) == 1:
                    y[i] += 1
    for elem in noy:
        noy[elem]=(noy[elem]+1)/(dislike+2)
    for elem in y:
        y[elem]=(y[elem]+1)/(liked+2)
    for elem in prob:
        (prob[elem])=(prob[elem]/counter)

    return noy, y, prob, header, ((liked)/((liked+dislike)))


def test(file, like, notlike, problike):
    header=next(file)
    totalliked=0
    totaldisliked=0
    real=[]
    ml=[]
    for row in file:
        row=row.strip()
        row=row.split(",")
        # row.strip gets rid of white space and enters
        for i in range (len(row)-1):
            if int(row[i])==1:
                totalliked+=math.log(like[i])
                totaldisliked+=math.log(notlike[i])
            else:
                totalliked+=math.log(1-like[i])
                totaldisliked+=math.log(1-notlike[i])
        totalliked+=math.log(problike)
        totaldisliked+=math.log(1-problike)
        totalliked=math.e**totalliked
        totaldisliked=math.e**totaldisliked
        if totalliked>totaldisliked:
            ml.append(1)
        else:
            ml.append(0)
        real.append(int(row[-1]))
    return (ml, real)
def main():
    trainfile=open("/Users/cheth/PycharmProjects/yousifreplacedme/netflix-small-train.csv")
    notlike,like,odds,header,problike=train(trainfile)
    print(like)
    testfile=open("/Users/cheth/PycharmProjects/yousifreplacedme/netflix-test.csv")
    ml,real=test(testfile, like, notlike,problike)
    print (ml)
    print (real)
    matchcounter=0

    for i in range (len(ml)):
        if ml[i]==real[i]:
            matchcounter+=1
    print (matchcounter/(len(ml)))
if __name__ == "__main__":
    main()
