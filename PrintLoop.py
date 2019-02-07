


for i in range(7):
    for j in range(7):

        for n in range(4):
            for m in range(4):
                print("\t\t\tacc" + str(n*4+m) + " += x4d(n+" + str(n) + ", c, h+" + str(i) + ", w+" + str(j) + ") * mask4d(m+" + str(m) + ", c, " + str(i) + ", " + str(j) + ");")

        print("//----------------------------------------------------")
