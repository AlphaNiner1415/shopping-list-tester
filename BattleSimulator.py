import random
import time
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
        print(self.name + " attacks")
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


Monster = Player("The Monster",10,50,5,5,0,1,0)
gameOver = 0
def battleFunction(player1, player2,gameover):

    print("Let the battle commence!")
    while gameover == 0:
        print("...")
        if player1.spd >= player2.spd:
            print("It is your turn!")
            sleep(1)
            print("You attack!")
            print("The monster have "+ str(player2.isDamaged(player1.attack(player2)))+" Hp left")
        else:
            print("It is the monster's turn")
            sleep(1)
            print("The monster attacks!")
            print("You have "+ str(player1.isDamaged(player2.attack(player1)))+" Hp left")
        if (player1.isDefeated()):
            print("Monster wins!")
            gameover = 1
        elif (player2.isDefeated()):
            print("You win!")
            gameover = 1

userinput = str(input("What is your name? "))
myPlayer = (userinput,10,50,5,5,0,1,0)
battleFunction(myPlayer,Monster,gameOver)
