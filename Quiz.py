def quiz():
    print("Welcome to a very simple and basic quiz!!!")
    print()

    print("Are you ready to play?")
    que=input("Type in your name to begin: ")
    print(f"Hi {que.title()}! \nLet's get started!")
    score=0  


    ans=input("1.How many colors do we have in a rainbow? ")
    if ans.lower()=="seven":      
        print("Correct,you really love the rainbow!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("2.What is the hardest substance in the world? ")
    if ans.lower()=="diamond":
        print("Correct,only a diamond can cut another diamond!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("3.How many wheels does a keke napep have? ")
    if ans.lower()=="three":
        print("Correct, keke napep is Nigerian name for tricycle!!")
        score+=10 
    else:
        print("Incorrect!!")    

    ans=input("4.Where is the eiffel tower located? ")
    if ans.lower()=="paris":
        print("Correct,Paris is located in France!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("5.Which country has the largest population? ")
    if ans.lower()=="china":
        print("Correct,it couldn't be any other country!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("6.Which country has the largest population in Africa? ")
    if ans.lower()=="nigeria":
        print("Correct,u wan try giant!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("7.What do you call an animal that can live on land and water? ")
    if ans.lower()=="amphibian":
        print("Correct,yeah a better name would have been better!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("8.What is the world's largest bird? ")
    if ans.lower()=="ostrich":
        print("Correct,it really is!!")
        score+=10
    else:
        print("Incorrect!!")    

    ans=input("9.What bones are babies born without? ")
    if ans.lower()=="kneecaps":
        print("Correct,welldone!!\nEven I couldn't have guessed that.")
        score+=10
    else:
        print("Incorrect!!")  
        
    ans=input("10.What was the first animal to be cloned? ")
    if ans.lower()=="sheep":
        print("Correct,welldone!!\nHer name was Dolly!")
        score+=10
    else:
        print("Incorrect!!") 

    print()
    print("You got " + str(score) + " questions correct.")
    print("You got " + str(score) + "%")
    if score == 100:
        print("Wow,you must really love quizzes!")
    else:
        print("You can do better next time!")
        print()   

    restart=input("Do you want play again?Yes/No  ").title()
    if restart=="Yes":
            quiz()
    elif restart=="No":    
        print("Game Over!!")          

quiz()        