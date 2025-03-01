import random
def game():
    print("You are playing the game..")
    score =random.randint(1,62)
    #fetch the highscore
    with open("./Practiceset/highscore.txt", "r") as text:
        highscore=text.read()
        if(highscore!=""):
           highscore=int(highscore)
        else:
            highscore=0
    print(f" Your scoe {score}")
    if(score>highscore ):
        with open("./Practiceset/highscore.txt", "w") as f:
            f.write(str(score))
    return score

game()