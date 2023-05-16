# N20DCCN033_Trần Ngọc Đăng Khoa
# N20DCCN046_Nguyễn Tiến Ngọc
# N20DCCN060_Trịnh Công Sơn

import copy
from queue import PriorityQueue

data = []
with open('taci.txt') as f:
    data.extend(f.readlines())

start = []
for i in range(1, 4):
    tmp = []
    for j in data[i].rstrip().split(" "):
        if j != "x":
            tmp.append(int(j))
        else:
            tmp.append(0)
    start.append(tmp)

goal = []
for i in range(5, 8):
    tmp = []
    for j in data[i].rstrip().split(" "):
        if j != "x":
            tmp.append(int(j))
        else:
            tmp.append(0)
    goal.append(tmp)


class Node:
    def __init__(self, state, par=None, g=0, h=0):
        self.state = state
        self.par = par
        self.g = g
        self.h = h

    def Key(self):
        if self.state == None:
            return False
        res = ''
        for i in range(3):
            for j in range(3):
                res += str(self.state[i][j])
        return res

    def Print(self):
        print("g=", self.g, ", ", "h=", self.h, ", ", "f=", self.g + self.h)
        for i in range(3):
            for j in range(3):
                if (self.state[i][j] == 0):
                    print("x", end=" ")
                else:
                    print(self.state[i][j], end=" ")
            print()

    def copyNode(self):
        tmp = copy.deepcopy(self)
        return tmp

    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h


def h(puz, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if puz[i][j] != goal[i][j] and puz[i][j] != 0:
                count += 1
    return count


def findIndex(puz, x):
    for i in range(3):
        for j in range(3):
            if (puz[i][j] == x):
                return i, j


def shuffle(puz, x1, y1, x2, y2):
    if x2 >= 0 and x2 <= 2 and y2 >= 0 and y2 <= 2:
        temp_puz = puz.copy()
        temp = temp_puz[x2][y2]
        temp_puz[x2][y2] = temp_puz[x1][y1]
        temp_puz[x1][y1] = temp


def child(O):
    x, y = findIndex(O.state, 0)

    val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    children = []
    for i in val_list:
        child_node = O.copyNode()
        shuffle(child_node.state, x, y, i[0], i[1])
        child_node.g = O.g + 1
        child_node.h = h(child_node.state, goal)
        child_node.par = O
        children.append(child_node)
    return children


# def ghiFile(O):
#     with open('test.txt','a+', encoding="utf-8") as f:
#         f.write("\nBước " + str(O.g + 1) + ": " + "g=" + str(O.g) + ", h=" + str(O.h) + ", f=" + str(O.h+O.g) + "\n")
#         for i in range(3):
#             for j in range(3):
#                 if(O.state[i][j] == 0):
#                     f.write("x" + " ")
#                 else:
#                     f.write(str(O.state[i][j]) + " ")
#             f.write("\n")

def path(O):
    if O.par != None:
        path(O.par)

    print("Buoc ", O.g + 1, end=":")
    O.Print()
    print()
    # ghiFile(O)


def equal(O, G):
    if O == None:
        return False
    return O.Key() == G.Key()


def Run(S, G):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    Open.put(S)

    while (True):
        if Open.empty():
            print("Tim kiem that bai")
            return

        O = Open.get()
        O.h = h(O.state, goal)
        chilren = child(O)

        if equal(O, G) == True:
            path(O)
            return

        for i in chilren:
            Open.put(i)


if __name__ == "__main__":
    S = Node(state=copy.deepcopy(start))
    G = Node(state=copy.deepcopy(goal))

    Run(S, G)