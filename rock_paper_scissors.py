


import random
import time

rock=1
paper=2
scissors=3

names={rock:'Rock',paper:'Paper',scissors:'Scissors'}
rules={rock:scissors,paper:rock,scissors:paper}

player_score=0
computer_score=0

def start():
    print("lets play this game ")
    while game():
        pass
    scores()

def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
    return playagain()
    
def move():
    while True:
        print()
        player=input("rock=1\npaper=2\nscissors=3\n")
        try:
            player=int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("enter a number netween 1-3")

def result(player,computer):
    print("1.....")
    time.sleep(1)
    print("2.....")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)   
    print("computer threw {}".format(names[computer]))
    global player_score,computer_score

    if player==computer:
        print("Tie Game")
    else:
        if rules[player]==computer:
            print("you won")
            player_score+=1

        else:
            print("you loose")
            computer_score+=1

def playagain():
    answer=input("do you want to play or not\n  yes or no\n")
    if answer in ("yes","y","yaa"):
        return answer
    else:
        print("ty for playing")

def scores():
    global player_score,computer_score
    print("hiigh score")
    print("player:",player_score)
    print("computer:",computer_score)


if __name__=="__main__":
    start()