def main():
    file=open("/Users/chethmittal/PycharmProjects/yousif_hatescoding/venv/Amazon_Products.csv")
    header=next(file)
    header=header.split(",")
    reviewdrone=0
    helicounter=0
    for i in range (len(header)):
        if header[i] == "":
            yousifsux= i
            break
    header = header[:i]
    print(header)
    for row in file:
        row = row.split(",")
        if len(row) > 8:
            if row[8] == "Arts & Crafts > Art Sand":
                helicounter+=1
                if any(char.isdigit() for char in row[7]):
                    for char in row[7]:
                        if char.isdigit():
                            reviewdrone += int(char)
                            break

    print (reviewdrone/helicounter)
if __name__ == "__main__":
    main()
