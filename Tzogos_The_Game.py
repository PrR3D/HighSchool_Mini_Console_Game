#Imports
import datetime
import SetUp
#Money File -
def money1(cost,a):
    file=open("Money.txt","r")
    money=file.read()
    money=int(money)
    money=money-cost
    file.close()
    print("{{{ Τα λεφτά σου πλέων είναι:",money,"€ }}}")
    file=open("Money.txt","w")
    money=str(money)
    file.write(money)
    file.close()
#Money File +
def money2(cost,a):
    file=open("Money.txt","r")
    money=file.read()
    money=int(money)
    money=money+(cost*a)
    file.close()
    print("{{{ Τα λεφτά σου πλέων είναι:",money,"€ }}}")
    file=open("Money.txt","w")
    money=str(money)
    file.write(money)
    file.close()
#Score File
def score1(b):
    file=open("Score.txt","r")
    score=file.read()
    score=int(score)
    score=score+b
    file.close()
    print("{{{ Το SCORE σου είναι: ",score,"}}}")
    file=open("Score.txt","w")
    score=str(score)
    file.write(score)
    file.close()
#Difficulty
#Easy
def easy(cost):
    b=20
    import random
    L=[] 
    for i in range(30):
        L.append(i)
    random_number=random.choice(L)
    Flag=False
    for i in range(3):
        print("~~~~~Προσπάθεια",i+1,"η~~~~~")
        choice=int(input("~>Δώσε τον αριθμό που πιστεύεις ότι θα κερδίσει:")) 
        if choice==random_number:
            print("---->Κέρδισες! :) <----")
            a=2
            money2(cost,a)
            b=b*2
            score1(b)
            Flag=True
        elif choice>=random_number:
            print("---->Έδωσες Μεγαλύτερο!<----")
        else:
            print("---->Έδωσες Μικρότερο!<----")
    if Flag==False:
        print("---->Εχασες! :( <----")
        print(">>>>Ο αριθμός ήταν:",random_number,"<<<<")
        a=1
        money1(cost,a)
        score1(b)
#Medium
def medium(cost):
    b=50
    import random
    L=[] 
    for i in range(50):
        L.append(i)
    random_number=random.choice(L)
    Flag=False
    for i in range(3):
        print("~~~~~Προσπάθεια",i+1,"η~~~~~")
        choice=int(input("~>Δώσε τον αριθμό που πιστεύεις ότι θα κερδίσει:")) 
        if choice==random_number:
            print("---->Κέρδισες! :) <----")
            a=4
            money2(cost,a)
            b=b*3
            score1(b)
            Flag=True
        elif choice>=random_number:
            print("---->Έδωσες Μεγαλύτερο!<----")
        else:
            print("---->Έδωσες Μικρότερο!<----")
    if Flag==False:
        print("---->Εχασες! :( <----")
        print(">>>>Ο αριθμός ήταν:",random_number,"<<<<")
        a=2
        money1(cost,a)
        score1(b)
#Hard
def hard(cost):
    b=100
    import random
    L=[] 
    for i in range(100):
        L.append(i)
    random_number=random.choice(L)
    Flag=False
    for i in range(3):
        print("~~~~~Προσπάθεια",i+1,"η~~~~~")
        choice=int(input("~>Δώσε τον αριθμό που πιστεύεις ότι θα κερδίσει:")) 
        if choice==random_number:
            print("---->Κέρδισες! :) <----")
            a=8
            money2(cost,a)
            b=b*4
            score1(b)
            Flag=True
        elif choice>=random_number:
            print("---->Έδωσες Μεγαλύτερο!<----")
        else:
            print("---->Έδωσες Μικρότερο!<----")
    if Flag==False:
        print("---->Εχασες! :( <----")
        print(">>>>Ο αριθμός ήταν:",random_number,"<<<<")
        a=5
        money1(cost,a)
        score1(b)
#MAIN PROGRAM
print("|⠀⠀⠀⠀⠀⠀⠀⣶⡄⢠⣶⡄⢠⣶⢰⡶⠶⡆⢰⡆⠀⢰⣶⠀⠀⣤⡶⢶⡄⣠⡶⢶⣦⡀⣴⣶⡀⠀⣴⣶⠀⣶⡶⢶⠀⠀⠶⢶⣶⢶⢀⣴⠶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀|")
print("|⠀⠀⠀⠀⠀⠀⠀⢹⣇⣸⣿⣇⣸⡇⢸⣧⣤⡄⢸⡇⠀⢸⣿⠀⢸⣿⠀⠀⢰⣿⠀⠀⢻⡇⣿⡿⣷⢰⡟⣿⠀⣿⣧⣤⠀⠀⠀⢸⣿⠀⣿⡇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀|")
print("|⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠈⣿⣿⠀⢸⣧⣤⡄⢸⣧⣤⢸⣿⣤⡜⢿⣦⣤⡎⢿⣦⣤⣿⠃⣿⡇⢻⣿⠁⣿⡀⣿⣧⣤⠀⠀⠀⢸⣿⠀⠻⣧⣤⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀|")
print("|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|")
print("|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|")
print("|⣤⣤⣤⡤⣤⣤⣤⡄⣠⣴⣦⣄⠀⢀⣤⣶⣤⡄⣠⣴⣶⣤⡀⣠⣴⣦⡄⠀⢠⣤⣤⣤⣤⣤⠀⢠⣤⢠⣤⣤⣤⠀⠀⢀⣤⣶⣤⡄⠀⣠⣤⡀⠀⣤⣤⠀⠀⣤⣤⠀⣤⣤⣤|")
print("|⠀⣿⡇⠀⢀⣼⠟⢸⣿⠁⠀⣿⡇⣿⠃⣤⣤⡄⣿⠃⠀⢹⣧⠻⣷⣤⡀⠀⠀⢸⣿⠀⢸⣿⣤⣼⣿⢸⣿⣤⡄⠀⠀⣾⡏⣤⣤⡄⢠⣿⢹⣧⠀⣿⢹⣇⣸⡟⣿⠀⣿⣤⣤|")
print("|⠀⣿⡇⠀⣾⣏⣀⡜⣿⣄⣠⣿⠃⢿⣦⣀⣿⡇⢿⣦⣠⣾⠇⣤⣈⣿⡇⠀⠀⢸⣿⠀⢸⣿⠀⢸⣿⢸⣿⣀⣄⠀⠀⢻⣧⣄⣿⡇⣾⠟⠛⣿⡄⣿⠈⣿⡿⠀⣿⠀⣿⣀⣠|")
print("|⠀⠉⠁⠀⠉⠉⠉⠁⠈⠉⠉⠀⠀⠀⠉⠉⠉⠀⠀⠉⠉⠁⠀⠈⠉⠁⠀⠀⠀⠈⠉⠀⠀⠉⠀⠈⠉⠀⠉⠉⠉⠀⠀⠀⠈⠉⠉⠀⠉⠀⠀⠈⠁⠉⠀⠈⠁⠀⠉⠀⠉⠉⠉|")
print("Created by PrRed")
#PRINT WALLET & SCORE
file=open("Money.txt","r")
money=file.read()
print("--[ Πορτοφόλι:",money,"€ ]--")
file.close()
file2=open("Score.txt","r")
score=file2.read()
print("--[ Score:",score,"]--")
file2.close()
play_or_not=input("~~~~~>Δώστε P για να παίξετε ή E για έξοδο απο το παιχνίδι ή F για να δείτε τα Final Scores και να παίξετε ή R για reset και έξοδο απο το παιχνίδι(τα γράμματα πρέπει να είναι στα αγγλικά): ")
while play_or_not=="P" or play_or_not=="F":
    #Add Final Scores and Refill
    money=int(money)   
    if money<=0:
        print("Σας έχουν τελιώσει τα λεφτά.")
        NoMoney=input("Δώστε K για να ξεκινήσετε καινούργια προσπάθεια(Τα λεφτά σας θα πάνε στο 100000 και το score στο 0): ")
        if NoMoney=="K" or NoMoney=="Κ":
            name=input("Δώστε το nickname σας για να μπει στα Final Scores: ")
            file3=open("FinalScores.txt","a")
            dt=datetime.datetime.today()
            dt=str(dt)
            FS=dt+" "+name+" Score:"+score+"\n"
            file3.write(FS)
            file3.close()
            SetUp.setup1()
            #PRINT WALLET & SCORE
            file=open("Money.txt","r")#<--
            money=file.read()
            print("--[ Πορτοφόλι:",money,"€ ]--")
            file.close()
            file2=open("Score.txt","r")
            score=file2.read()
            print("--[ Score:",score,"]--")
            file2.close()
    
    #Final Scores
    if play_or_not=="F":
        print("------------------------------------")
        print("#@$%$!@#$>> Final Scores <<!%$~$#@#$")
        print("------------------------------------")
        file4=open("FinalScores.txt","r")
        for line in file4:
            print(line)
        file4.close()
        print("Δώστε enter για να συνεχίσετε")
        nothing=input()
    
    
    #Program
    print("--------------------")
    print("====>Difficulty<====")
    print("--------------------")
    print("* Easy όπου το ποσό που ποντάρεις αν κερδίσεις γίνεται x2 και η κλίμακα είναι από το 0 εώς 30.")
    print("** Medium όπου το ποσό που ποντάρεις αν κερδίσεις γίνεται x4 και η κλίμακα είναι από το 0 εώς 50.")
    print("*** Hard όπου το ποσό που ποντάρεις αν κερδίσεις γίνεται x8 και η κλίμακα είναι από το 0 εώς 100.")
    Difficulty=input("~~>Σε τι δυσκολία θέλεις να παίξεις?? ")
    while Difficulty!="Easy" and Difficulty!="easy" and Difficulty!="Medium" and Difficulty!="medium" and Difficulty!="Hard" and Difficulty!="hard":
        print("ERROR: Η δυσκολία που διαλέξατε δεν υπάρχει. Προσπαθίστε ξανά!!!")
        Difficulty=input("Σε τι δυσκολία θέλεις να παίξεις??")
    cost=int(input("Δώστε χρηματικό ποσό που θέλετε να ποντάρεται:"))
    while cost<=0:
        print("ERROR: Δεν γίνεται να δώσετε αρνιτικό αριθμό. Προσπαθίστε ξανά!!!")
        cost=int(input("Δώσε χρηματικό ποσό που θέλετε να ποντάρεται:"))
    file=open("Money.txt","r")
    money=file.read()
    money=int(money)
    if money/cost>=1.0:
        file.close()
        if Difficulty=="Easy" or Difficulty=="easy":
            easy(cost)
        elif Difficulty=="Medium" or Difficulty=="medium":
            medium(cost)
        else:
            hard(cost)
    else:
        print("ERROR: Δεν έχεις αρκετά λεφτά.")
    play_or_not=input("~~~~~>Δώστε P για να παίξετε ή E για έξοδο απο το παιχνίδι ή F για να δείτε τα Final Scores και να παίξετε ή R για reset και έξοδο απο το παιχνίδι(τα γράμματα πρέπει να είναι στα αγγλικά): ")
#Reset
if play_or_not=="R":
    ep=input("Είστε σίγουρος? Τα Final Scores θα διαγραφούν μαζί και όλη η πρόοδος σας.(YES or NO) ")
    if ep=="YES":
        SetUp.setup1()
    




