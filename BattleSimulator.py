import random
from time import sleep
class Player(object):
    def __init__(self, name, att, hp, defe, spd, exp, lvl, skillpt):
        self.name = name
        self.att = att
        self.hp = hp
        self.defe = defe
        self.spd = spd
        self.exp = exp
        self.lvl = lvl
        self.skillpt = skillpt
        self.gameover = 0
        # self.turncounter = turncounter

    def levelUp(self):
        self.lvl += 1
        self.exp = 0
        self.skillpt += round(5* (self.lvl* 0.5))

    def modSkill(self,userinput):
        pass
        # while self.skillpt != 0:
        #     userinput = input("What would you like to improve? ")
        #     if userinput == "att":

    def attack(self,opponent):
        if self.att == opponent.defe:
            return 2
        else:
            return self.att - opponent.defe
    def isDamaged(self, damage):
        self.hp -= damage
        return self.hp
    def isDefeated(self):
        if self.hp == 0:
            self.gameover = 1
            return True
        else:
            return False


Monster = Player("The Monster",10,20,5,5,0,1,0)
gameOver = 0
myPlayer = Player("name",10,20,5,10,0,1,0)
def battleFunction(player1, player2,gameover,temp):

    print("Let the battle commence!")
    # while gameover == 0:
    print("...")
    if temp == "player":
        print("It is your turn!")
        sleep(1)

        print(random.choice(["You attack!", "You lunge at the monster,weapon at the ready."]))
        random.seed(random.randint(1,200))
        num = random.randint(1,10)

        if num <= player1.spd - player2.spd:
            damage = player1.attack(player2)

            print(random.choice(["You hit!", "Score! Your attack connects!", "Your weapon draws blood as it connects with the monster!"]))
            print("The monster have "+ str(player2.isDamaged(damage))+" Hp left")
        else:
            print("You miss!")
            print("The monster have "+ str(player2.hp) + " Hp left")
        temp = "monster"

    elif temp == "monster":
        print("It is the monster's turn")
        sleep(1)
        print("The monster attacks!")
        num2 = random
        print("You have "+ str(player1.isDamaged(player2.attack(player1)))+" Hp left")

        sleep(1)
        temp = "player"
    if (player1.isDefeated()):
        print("Monster wins!")
        gameover = 1
    elif (player2.isDefeated()):
        print("You win!")
        gameover = 1
if myPlayer.spd >= Monster.spd:
    battleFunction(myPlayer,Monster,gameOver, "player")
elif myPlayer.spd < Monster.spd:
    battleFunction(myPlayer,Monster,gameOver,"monster")
