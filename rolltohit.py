#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.
#Video Link: https://youtu.be/89G5DN0-O3k
import random

random.seed()

print("Enter the number of dice and the hit target: ")

diceCount = int(input("Number of dice: "))
hitTarget = int(input("Enter the hit target: "))

hitCount = 0
diceRoll = 0

for i in range (diceCount):
    diceRoll = random.randint(1,6)
    #print(f"Diceroll: {diceRoll}")
    if diceRoll >= hitTarget:
        hitCount += 1
        
print(f"You rolled {diceCount} dice with a hit target of {hitTarget} and hit {hitCount} times.")
