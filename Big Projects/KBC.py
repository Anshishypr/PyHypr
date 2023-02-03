# ------------------------------------------------------- KBC Simulation ------------------------------------------------------- #

q = "Quit"
win = "Congratulations !!!"
money = 0

Qs = [  [f"\nQ1. Who is the second Prime Minister of India ?              {q}(Q)"],
        [f"\nQ2. The International Literacy Day is observed on which day ?              {q}(Q)"],
        [f"\nQ3. Whom does the Indian Constitution permit to take part in the proceedings of Parliament ?              {q}(Q)"],
        [f"\nQ4. Who is Known as The Father of The Nation ?              {q}(Q)"]
]

As = [
['''    A. Chandra Shekhar   C. Lal Bahadur Shastri 
    B. Indira Gandhi     D. Jawaharlal Nehru \n'''],

['''    A. Sep 8      C. May 2
    B. Nov 28     D. Sep 22 \n'''],

['''    A. Solicitor General      C. Cabinet Secretary 
    B. Attorney General       D. Chief Justice \n'''],

['''    A. Ranbir Kapoor   C. Rahul Gandhi
    B. Joe Biden       D. Mahatma Gandhi \n''']
]

gameRules = '''
                1. All Questions must be Answered.
                2. You can Quit Anytime before Answering any Question.
                3. You Must be a Fax Machine.
                4. Look at the Chart Below to Know the Reward Cycle - 
                        
                        Question 1 ----- 10,000 $
                        Question 2 ----- 1,00,000 $
                        Question 3 ----- 1,00,00,000 $
                        Question 4 ----- 7,00,00,00,000 $

                5. Best of Luck.
            '''

user = str(input("Do You Want to Play KBC ? (Y / N) "))

def KBC():
    for i in Qs[0]:
        for j in As[0]:
            print(i)
            print(j)
    userIn = str(input("-> "))
    match(userIn):
        case "C":
            print("Correct Answer.")
            money = "10,000"
        case "c":
            print("Correct Answer.")
            money = "10,000"
        case "Q":
            money = "0"
            print(f"You are Taking {str(money)} $.")
            exit()
        case _:
            print("Wrong Answer.")
            money = "0"
            print(f"You are Taking {str(money)} $.")
            exit()


    for i in Qs[1]:
        for j in As[1]:
            print(i)
            print(j)
    userIn1 = str(input("-> "))
    match(userIn1):
        case "A":
            print("Correct Answer.")
            money = "1,00,000"
        case "a":
            print("Correct Answer.")
            money = "1,00,000"
        case "Q":
            money = "10,000"
            print(f"You are Taking {str(money)} $.")
            exit()
        case _:
            print("Wrong Answer.")
            money = "10,000" + " $ "
            print(f"You are Taking {str(money)} $.")
            exit()

    for i in Qs[2]:
        for j in As[2]:
            print(i)
            print(j)
    userIn2 = str(input("-> "))
    match(userIn2):
        case "B":
            print("Correct Answer.")
            money = "1,00,00,000"
        case "b":
            print("Correct Answer.")
            money = "1,00,00,000"
        case "Q":
            money = "1,00,000"
            print(f"You are Taking {str(money)} $.")
            exit()
        case _:
            print("Wrong Answer.")
            money = "1,00,000"
            print(f"You are Taking {str(money)} $.")
            exit()

    for i in Qs[3]:
        for j in As[3]:
            print(i)
            print(j)
    userIn3 = str(input("-> "))
    match(userIn3):
        case "D":
            print("Correct Answer.")
            money = "7,00,00,00,000"
            print(f'''
                    {win} You are Taking {str(money)} $.
            ''')
            exit()
        case "d":
            print("Correct Answer.")
            money = "7,00,00,00,000"
            print(f'''
                    {win} You are Taking {str(money)} $.
            ''')
            exit()
        case "Q":
            money = "1,00,00,000"
            print(f"You are Taking {str(money)} $.")
            exit()
        case _:
            print("Wrong Answer.")
            money = "1,00,00,000"
            print(f"You are Taking {str(money)} $.")
            exit()

if user == "Y":
    rules = str(input("Do You Want to See Rules First ? (Y / N) "))
elif user == "y":
    rules = str(input("Do You Want to See Rules First ? (Y / N) "))
elif user == "N":
    print("Thank You.")
    exit()
elif user == "n":
    print("Thank You.")
    exit()
elif user == "Yes":
    rules = str(input("Do You Want to See Rules First ? (Y / N) "))
elif user == "No":
    print("Thank You.")
    exit()
else:
    print(f"-> {user} is Not Valid.")

if rules == "Y":
    print(gameRules)
    KBC()
elif rules == "y":
    print(gameRules)
    KBC()
elif rules == "N":
    KBC()
elif rules == "n":
    KBC()
elif rules == "Yes":
    print(gameRules)
    KBC()
elif rules == "No":
    KBC()
else:
    print(f"-> {rules} is Not Valid.")
