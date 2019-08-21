import time
import random

r1 = [" ", " ", " "]
r2 = [" ", " ", " "]
r3 = [" ", " ", " "]
op = False
tu = False
temp = []
rand = 0
poz = 0
pc = "already used"


moves = 0
ocup = []


def treb():
    global ran
    ran = int(input("Where do i mark ==>"))
    if 0 > ran or ran > 8:
        print("you cand enter just numbers between 0 and 8")
        treb()


def check():
    global tu;
    global op;
    if r1 == ["X", "X", "X"] or r2 == ["X", "X", "X"] or r3 == ["X", "X", "X"]:
        tu = True
    elif r1[0] == "X" and r2[0] == "X" and r3[0] == "X":
        tu = True
    elif r1[1] == "X" and r2[1] == "X" and r3[1] == "X":
        tu = True
    elif r1[2] == "X" and r2[2] == "X" and r3[2] == "X":
        tu = True
    elif r1[0] == "X" and r2[1] == "X" and r3[2] == "X":
        tu = True
    elif r1[2] == "X" and r2[1] == "X" and r3[0] == "X":
        tu = True
    elif r1 == ["O", "O", "O"] or r2 == ["O", "O", "O"] or r3 == ["O", "O", "O"]:
        op = True
    elif r1[0] == "O" and r2[0] == "O" and r3[0] == "O":
        op = True
    elif r1[1] == "O" and r2[1] == "O" and r3[1] == "O":
        op = True
    elif r1[2] == "O" and r2[1] == "O" and r3[2] == "O":
        op = True
    elif r1[0] == "O" and r2[1] == "O" and r3[2] == "O":
        op = True
    elif r1[2] == "O" and r2[1] == "O" and r3[0] == "O":
        op = True
    else:
        pass


def show():
    print(r1)
    print(r2)
    print(r3);


def pune():
    global moves
    if ran == 0:
        if 0 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(0)
            r1[0] = "X"
    elif ran == 1:
        if 1 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(1)
            r1[1] = "X"
    elif ran == 2:
        if 2 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(2)
            r1[2] = "X"
    elif ran == 3:
        if 3 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(3)
            r2[0] = "X"
    elif ran == 4:
        if 4 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(4)
            r2[1] = "X"
    elif ran == 5:
        if 5 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(5)
            r2[2] = "X"
    elif ran == 6:
        if 6 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(6)
            r3[0] = "X"
    elif ran == 7:
        if 7 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(7)
            r3[1] = "X"
    elif ran == 8:
        if 8 in ocup:
            print(pc)
            treb()
            pune()
        else:
            ocup.append(8)
            r3[2] = "X"
    else:
        print("WHAT IS THAT??!!")
        treb()
        pune()
    moves += 1


def tuto():
    print("                X and O         ")
    print("You're X ")
    time.sleep(1)
    print(r1)
    print(r2)
    print(r3)
    time.sleep(0.3)
    print("to play you just need to enter the number of the box you want to mark")
    time.sleep(0.2)
    print("for example")
    print("Where do i mark ==>1")
    print(["0", "X", "2"])
    print(["3", "4", "5"])
    print(["6", "7", "8"])
    time.sleep(10)


class opo:
    def punr():
        global moves
        if move == 0:
            r1[0] = "O"
        elif move == 1:
            r1[1] = "O"
        elif move == 2:
            r1[2] = "O"
        elif move == 3:
            r2[0] = "O"
        elif move == 4:
            r2[1] = "O"
        elif move == 5:
            r2[2] = "O"
        elif move == 6:
            r3[0] = "O"
        elif move == 7:
            r3[1] = "O"
        elif move == 8:
            r3[2] = "O"
        moves += 1

    def timp():
        time.sleep(0.5)
        print("○○○")
        time.sleep(0.2)
        print("●○○")
        time.sleep(0.3)
        print("●●○")
        time.sleep(0.5)
        print("●●●")
        time.sleep(0.5)
        print("gata")

    def mov():
        global move
        move = random.randint(0, 8)
        if move in ocup:
            opo.mov()
        else:
            ocup.append(move)



print("wanna have a tutorial")
print("press y for yes.anything else for no")
vtut = input()
if vtut.lower() == "y":
    tuto()
    print("have fun")
else:
    pass

while True:
  ocup.sort()
  if op == True:
        print("you lost")
        break
  elif tu == True:
        print("you won")
        break
  elif moves == 9:
        print("equality")
        break
  else:
        print("your turn")
        treb()
        pune()
        show()
        check()
        ocup.sort()
        if op == True:
            print("you lost")
            break
        elif tu == True:
            print("you won")
            break
        elif moves == 9:
            print("equality")
            break
        else:
          print("computers turn")
          opo.timp()
          opo.mov()
          opo.punr()
          show()
          check()