from AVLTree import AVLTree

for i in range (1, 11):
    n = 300 * 2 ** i
    sorted_lst = []
    promotes = 0
    for j in range(n):
        sorted_lst.append(j)
    T = AVLTree()
    for j in sorted_lst:
        promotes += T.finger_insert(j, str(j))[2]
    print ("n = " + str(n) + " rebalancing actions: " + str(promotes))


