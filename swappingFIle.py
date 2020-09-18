def swapFileData(file1, file2):

    f1 = open(file1, "r+")
    f2 = open(file2, "r+")

    savedData = f1
    print(savedData)
    f1.write(f2)
    print(f1)
    f2.write(savedData)
    print(f2)

    # for line in f2:
    #     savedData.append(line)
    #     f1.writelines(savedData2)

    # for line in f1:
    #     savedData.append(line)
    #     f2.writelines(savedData1)

    # f1.writelines(savedData2)
    # f2.writelines(savedData1)


file1 = input("path of first file : ")
file2 = input('path of second file : ')

swapFileData(file1, file2)
print("file1 data ")
