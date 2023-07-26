# General program for printing any name
# nested list --eg.
# l=[["*" for i in range(5)] for j in range(2)]
# print(l)
# Note: no. of rows and columns of empty list should must be same as the printing matrix

def names():                                            # defining a function named name
    for x in range(len(name)):                          # it will iterate(run) till length of name
        # A
        if name[x] == "A":
            print_A = [[" " for j in range(5)] for i in range(7)]  # nested list of i-row and j-column
            for i in range(7):
                for j in range(5):
                    if (i != 0 and (j == 0 or j == 4)) or ((i == 0 or i == 4) and 0 < j < 4):
                        print_A[i][j] = "*"             # to store the * in the empty list
            list1.append(print_A)                       # to append the list if condition satisfied
        # B
        elif name[x] == "B":
            print_B = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or ((i == 0 or i == 3 or i == 6) and j != 4) or (
                            j == 4 and (i != 0 and i != 3 and i != 6)):
                        print_B[i][j] = "*"
            list1.append(print_B)
        # C
        elif name[x] == "C":
            print_C = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (j == 0 and (i != 0 and i != 6)) or (j > 0 and (i == 0 or i == 6)):
                        print_C[i][j] = "*"
            list1.append(print_C)
        # D
        elif name[x] == "D":
            print_D = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or (j == 4 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and 0 < j < 4):
                        print_D[i][j] = "*"
            list1.append(print_D)
        # E
        elif name[x] == "E":
            print_E = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or i == 0 or i == 3 or i == 6:
                        print_E[i][j] = "*"
            list1.append(print_E)
        # F
        elif name[x] == "F":
            print_F = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or i == 0 or (i == 3 and j != 4):
                        print_F[i][j] = "*"
            list1.append(print_F)
        # G
        elif name[x] == "G":
            print_G = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (j == 0 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and j > 0) or (j == 4 and i > 2) or (
                            (j == 3 and i == 3) or (j == 3 and i == 4)):
                        print_G[i][j] = "*"
            list1.append(print_G)
        # H
        elif name[x] == "H":
            print_H = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or j == 4 or i == 3:
                        print_H[i][j] = "*"
            list1.append(print_H)
        # I
        elif name[x] == "I":
            print_I = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or i == 6 or j == 2:
                        print_I[i][j] = "*"
            list1.append(print_I)
        # J
        elif name[x] == "J":
            print_J = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or (j == 3 and i < 6) or (i == 6 and 0 < j < 3) or (i == 5 and j == 0):
                        print_J[i][j] = "*"
            list1.append(print_J)
        # K
        elif name[x] == "K":
            print_K = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or i + j == 4 or i - j == 2:
                        print_K[i][j] = "*"
            list1.append(print_K)
        # L
        elif name[x] == "L":
            print_L = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or i == 6:
                        print_L[i][j] = "*"
            list1.append(print_L)
        # M
        elif name[x] == "M":
            print_M = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or j == 4 or (i == j and i < 3) or (i + j == 4 and i < 3):
                        print_M[i][j] = "*"
            list1.append(print_M)
        # N
        elif name[x] == "N":
            print_N = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or j == 4 or i - j == 1:
                        print_N[i][j] = "*"
            list1.append(print_N)
        # O
        elif name[x] == "O":
            print_O = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 6) and j != 0 and j != 4) or ((j == 0 or j == 4) and i != 0 and i != 6):
                        print_O[i][j] = "*"
            list1.append(print_O)
        # P
        elif name[x] == "P":
            print_P = [[" " for J in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or (i == 0 and j < 4) or (i == 3 and j < 4) or (j == 4 and 0 < i < 3):
                        print_P[i][j] = "*"
            list1.append(print_P)
        # Q
        elif name[x] == "Q":
            print_Q = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 5) and 0 < j < 4) or ((j == 0 or j == 4) and 0 < i < 5) or (
                            i == 4 and j == 2) or (i == 6 and j == 4):
                        print_Q[i][j] = "*"
            list1.append(print_Q)
        # R
        elif name[x] == "R":
            print_R = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or ((i == 0 or i == 3) and j < 4) or (j == 4 and (i != 0 and i != 3)):
                        print_R[i][j] = "*"
            list1.append(print_R)
        # S
        elif name[x] == "S":
            print_S = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if ((i == 0 or i == 3 or i == 6) and 0 < j < 4) or (j == 0 and 0 < i < 3) or (
                            j == 4 and 3 < i < 6) or (i == 1 and j == 4) or (i == 5 and j == 0):
                        print_S[i][j] = "*"
            list1.append(print_S)
        # T
        elif name[x] == "T":
            print_T = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or j == 2:
                        print_T[i][j] = "*"
            list1.append(print_T)
        # U
        elif name[x] == "U":
            print_U = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (j == 0 and i != 6) or (j == 4 and i != 6) or (i == 6 and 0 < j < 4):
                        print_U[i][j] = "*"
            list1.append(print_U)
        # V
        elif name[x] == "V":
            print_V = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (i == 0 and (j == 0 or j == 4)) or (i == 3 and (j == 1 or j == 3)) or (i == 6 and j == 2):
                        print_V[i][j] = "*"
            list1.append(print_V)
        # W
        elif name[x] == "W":
            print_W = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if j == 0 or j == 4 or (i + j == 6 and i > 3) or (i - j == 2 and i > 3):
                        print_W[i][j] = "*"
            list1.append(print_W)
        # X
        elif name[x] == "X":
            print_X = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (i == 0 and (j == 0 or j == 4)) or (i == 1 and (j == 1 or j == 3)) or (i == 3 and j == 2) or (
                            i == 5 and (j == 1 or j == 3)) or (i == 6 and (j == 0 or j == 4)):
                        print_X[i][j] = "*"
            list1.append(print_X)
        # Y
        elif name[x] == "Y":
            print_Y = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if (i == 0 and (j == 0 or j == 4)) or (i == 1 and (j == 1 or j == 3)) or (j == 2 and i > 1):
                        print_Y[i][j] = "*"
            list1.append(print_Y)
        # Z
        elif name[x] == "Z":
            print_Z = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i == 0 or i == 6 or i + j == 5:
                        print_Z[i][j] = "*"
            list1.append(print_Z)
        # space
        elif name[x] == " ":
            print_ = [[" " for j in range(5)] for i in range(7)]
            for i in range(7):
                for j in range(5):
                    if i <= 6 or j <= 4:
                        print_[i][j] = " "
            list1.append(print_)
        else:
            print("Invalid")
    return list1                           # list1 will be returned after the completion of loop

while True:
    name = input("Enter character in upper case:-")           # to take user's input
    if name.lower() == 'exit':
        break

    list1 = []  # empty list to store the results
    list2 = names()  # list to returned the stored results
    for i in range(7):  # for row
        for x in range(len(name)):  # for index of list2
            for j in range(5):  # for column
                print(list2[x][i][j], end=" ")
            print(end=" ")
        print()
