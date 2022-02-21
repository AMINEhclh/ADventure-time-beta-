from re import X
import time 
coins=100
PlayerName=input("Put Your Name In The Game")
time.sleep(1)
print("Hello,  ",PlayerName,"  Welcome To Adventure Time ")
time.sleep(5)
print("hope u enjoy")
time.sleep(3)
print("******************************************  ADVENTURE TIME  ******************************************")
print("                                                                                     coins=",coins)
print("i think now you are ready to start your adventure")
time.sleep(5)
print("you have now", coins,"in your wallet let's buy your first gun")
time.sleep(5)
print("******************************************  SHOP  ******************************************")
print("                          |||      KNIFE     |||         AXE       |||")
print("                          |||     90 coin    |||       90 coin     |||")
time.sleep(4)
firstWeapon=input("what do u want KNIFE or AXE ")
while firstWeapon not in ["KNIFE","knife", "axe","AXE"]:
    firstWeapon=input("what do u want KNIFE or AXE ")
if firstWeapon=="KNIFE" and "knife":
    print("nice now u have a KNIFE in your inventory")
else:
    print("nice now u have an AXE in your inventory")
time.sleep(3)
print("ALISA : OH no! we are under attack you have to protect us")
time.sleep(3)
print("ALISA : go what are u waiting for")
time.sleep(2)
print("******************************************  FIGHT  ******************************************")
print("     BOSS HP = 100                                                                    HP=100 ")
time.sleep(3)
from random import*
bossHP=100
s=0
while 0<bossHP<1:
    if s>1:
        print("nice")
    elif s>3:
        print("good")
    else:
        print("nice hit")
    x=randint(15,50)
    bossHP=bossHP-x
    print( "bossHP =",bossHP,"                                                               HP=100 ")
    s+=1
    time.sleep(2)
print("nice you killed a giga chad boss")
time.sleep(4)
print("******************************************  END  ******************************************")
time.sleep(1)
print("*********************************** created by DaRealGuy  ******************************************")
time.sleep(1)
print("************************************ thanks for playing  *******************************************")
time.sleep(1)
print("****************************************    bye     *********************************************")