import random
def game(comp,you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return False
        elif comp =="s":
            return True
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False     
    elif comp == "p":
        if you == "s":
            return True 
        elif you == "r":
            return False 

print("Computer Choose: Rock(r) Paper(p) or Sisicoor(s)")

randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo ==2:
    comp = "p"
else:
    comp = "s"

you = input("YOu Turn: Rock(r) Paper(p) or Sisicoor(s)")

print(f"Comp Choose {comp}")
print(f"You Choose {you}")
randNo = random.randint(1,3)


a = game(comp,you)

if a == None:
    print("Match Tie!")
elif a== True:
    print("You Won!")
else:
    print("YOu Loose")