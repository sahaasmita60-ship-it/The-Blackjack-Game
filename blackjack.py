import random
cards=[2,3,4,5,6,7,8,9,10,10,10,10,11] #13
you=[]
comp=[]
print("~ Welcome to the Blackjack Game ~")
for i in range (0,2):
    you.append(random.choice(cards))
for i in range (0,2):
    comp.append(random.choice(cards))
sum1=0
sum2=0
print(f"These are your cards {you} and this is one of computer's cards [{comp[0]}]")
for i in range(0,100):
 choice=input(("Do you wish to draw another card?: yes/no "))
 if choice=="yes":
       you.append(random.choice(cards))
       print(f"These are your cards {you}")
 else:
     break
sum1=sum(you)
sum2=sum(comp)
while sum1>21 and 11 in you:
    you[you.index(11)]=1
    sum1=sum(you)
while sum2 < 17:
    comp.append(random.choice(cards))
    sum2 = sum(comp)
while sum2>21 and 11 in comp:
    comp[comp.index(11)]=1
    sum2=sum(comp)
print(sum1,sum2)
if sum1>21:
    print(f"Busted, you lose, Your points go over 21! Your cards {you} and computer's cards {comp}")
elif sum2>21:
    print(f"You win, computer's points are going over 21! Your cards {you} and computer's cards {comp}")
elif(sum1>sum2):
    print(f"You win! Your cards {you} and computer's cards {comp}")
elif(sum2>sum1):
    print(f"Busted, you lose! Your cards {you} and computer's cards {comp}")
elif(sum1==sum2):
    print(f"It is a tie. Your cards {you} and computer's cards {comp}")