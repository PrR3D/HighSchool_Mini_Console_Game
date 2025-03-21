def setup1():
    #MONEY
    file=open("Money.txt","w")
    money=str(100000)
    file.write(money)
    file.close()
    #SCORE
    file2=open("Score.txt","w")
    score=str(0)
    file2.write(score)
    file2.close()
def setup2():
    #Reboot
    file3=open("FinalScores.txt","w")
    file3.close()
