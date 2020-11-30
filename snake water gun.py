import random
import time
print(":::snake water and gun game:::")
print("::Total 10 rounds::")

list1= ["snake","water","gun"]

matches=1
your_point=0
cpu_point=0
    

while(matches<=10):
    me = (input("TYPE=snake/ water/ gun:\n"))
    cpu = random.choice(list1)
    print(cpu)
    if me==cpu:
        print("Tie")
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("No points to both")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="snake" and cpu=="water":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("You won the match\n")
        your_point=your_point+1
        print("YOu got:", your_point, "points")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="water" and cpu=="snake":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("you lose the match")
        cpu_point=cpu_point+1
        print("computer got:", cpu_point, "points")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="gun" and cpu=="water":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("you lose the match")
        cpu_point=cpu_point+1
        print("computer got:", cpu_point, "points")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="water" and cpu=="gun":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("You win the match")
        your_point=your_point+1
        print("YOu got:",your_point,"points")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="gun" and cpu=="snake":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("you win the match")
        your_point=your_point+1
        print("You got:",your_point,"points")
        print(10 - matches, "Rounds left out of 10:\n")
        matches = matches + 1
    elif me=="snake" and cpu=="gun":
        print(f"you choosed {me} \n computer choosed {cpu}")
        print("you lose the match")
        cpu_point=cpu_point+1
        print("computer got:",cpu_point,"points")

        print(10-matches,"Rounds left out of 10:\n")
        matches=matches+1
    else:
        print("use proper input")
        if(matches>10):
          print("rounds over")
if cpu_point>your_point:
    print(":::::Computer is the winner:::::\n::YOU LOSE::")
if cpu_point<your_point:
    print(":::::You are the winner:::::\n::COMPUTER LOST")
print(f"your total points {your_point}\n Computer totsl points {cpu_point}")
"\n"
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
print(end=" ")
#end








