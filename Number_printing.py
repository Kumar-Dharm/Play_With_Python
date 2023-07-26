# General program for printing any number
# nested list
# l=[["*" for i in range(5)] for j in range(2)]
# print(l)
# Note: no. of rows and columns of empty list should must be same as the printing matrix

def number():                            # defining a function named number
    for x in range(len(num)):            # it will iterate(run) till length of number
        # 0
        if num[x] == "0":
            print_0 = [[" " for j in range(5)] for i in range(7)]  # nested list of i-row and j-column
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 6) and j != 0 and j != 4) or ((j == 0 or j == 4) and i != 0 and i != 6):
                        print_0[i][j] = "*"                  # to store the * in the empty list
            list1.append(print_0)                            # to append the list if condition satisfied
        # 1
        elif num[x] == "1":
            print_1 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 2 or i == 6 or i == j == 1:
                        print_1[i][j] = "*"
            list1.append(print_1)
        # 2
        elif num[x] == "2":
            print_2 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (i == 0 and 0 < j < 4) or (i + j == 6 and 0 < i < 6) or i == 6 or (i == 1 and j == 0) or (
                            i == 1 and j == 4):
                        print_2[i][j] = "*"
            list1.append(print_2)
        # 3
        elif num[x] == "3":
            print_3 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 3 or i == 6) and 0 < j < 4) or (j == 4 and (0 < i < 3 or 3 < i < 6)) or (
                            j == 0 and (i == 1 or i == 5)):
                        print_3[i][j] = "*"
            list1.append(print_3)
        # 4
        elif num[x] == "4":
            print_4 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 4 or j == 3 or i + j == 3:
                        print_4[i][j] = "*"
            list1.append(print_4)
        # 5
        elif num[x] == "5":
            print_5 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or (j == 0 and i < 4) or (i == 2 and j < 4) or (i == 6 and j < 4) or (
                            j == 4 and 2 < i < 6):
                        print_5[i][j] = "*"
            list1.append(print_5)
        # 6
        elif num[x] == "6":
            print_6 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 3 or i == 6) and 0 < j < 4) or (j == 0 and 0 < i < 6) or (
                            j == 4 and (i == 1 or 3 < i < 6)):
                        print_6[i][j] = "*"
            list1.append(print_6)
        # 7
        elif num[x] == "7":
            print_7 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or i + j == 6 or (i == 1 and j == 4):
                        print_7[i][j] = "*"
            list1.append(print_7)
        # 8
        elif num[x] == "8":
            print_8 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 3 or i == 6) and 0 < j < 4) or (
                            (j == 0 or j == 4) and i != 0 and i != 3 and i != 6):
                        print_8[i][j] = "*"
            list1.append(print_8)
        # 9
        elif num[x] == "9":
            print_9 = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 3 or i == 6) and 0 < j < 4) or (j == 0 and (0 < i < 3 or i == 5)) or (
                            j == 4 and 0 < i < 6):
                        print_9[i][j] = "*"
            list1.append(print_9)
        # space
        elif num[x] == " ":
            print_ = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i <= 6 or j <= 4:
                        print_[i][j] = " "
            list1.append(print_)
        else:
            print("Invalid")
    return list1                          # list1 will be returned after the completion of loop

while True:
    num = input("Enter the number (type 'exit' to stop): ")
    if num.lower() == 'exit':
        break

    list1 = []
    list2 = number()
    for i in range(7):
        for x in range(len(list2)):
            for j in range(5):
                print(list2[x][i][j], end=" ")
            print(end=" ")
        print()

