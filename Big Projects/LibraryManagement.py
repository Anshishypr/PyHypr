# Library Management System #
import random

class Library:
    def info(self):
        print('''
    What Do You Want to Do ? 

        1. Book Issue
        2. Book Donation
        3. Book Sell
        4. Book Purchase
        5. Book Return
''')
    def task(self):
        user = int(input(" [1-2-3-4-5] -> "))
        match(user):
            case 1:
                Issue(None)
            case 2:
                Donation(None)
            case 3:
                Sell(None)
            case 4:
                Purchase(None)
            case 5:
                Return(None)
            case _:
                print("Not Valid.")
                lib.task()

class Books():
    libBooks = ["Sapiens", "Bhagvad Geeta", "Rework", "Ramayana", "Can't Hurt Me", "Laws Of Human Nature", "Ratna Sagar",
    "Deus", "Atomic Habits", "Psychology Of Money", "21 Lessons For 21st Century", "DaVinci Code", "The Alchemist", "Ikigai",
    "Mindset", "Rich Dad, Poor Dad", "Hyper Focus", "Quiet", "Art Of War", "His And Hers", "Do Epic Shit", "Think & Grow Rich",
    "Ulysses", "War and Peace", "Moby Dick", "The Monk Who Sold His Ferrari", "The Lost Symbol", "Power Of Your Subconsious Mind",
    "Start With Why", "21 Lesson For The 21st Century", "The Courage To Be Disliked", "Tools Of Titans", "Almanack Of Naval Ravikant",
    "The Chalk Man", "Why Has No Body Told Me This Before", "Who Will Cry When You Die", "The Subtle Art Of Not Giving A Fuck", "Mad", 
    "A Good Girl's Guide To Murder", "Everything Is Fucked"
]
    notinlib = []

class Issue:
    def __init__(self, userbook):
        self.book = userbook
        self.book = str(input("Book To Issue -> "))
        if self.book in Books.libBooks:
            print("Sir, Here's Your Book.")
            issued = Books.libBooks.pop(Books.libBooks.index(self.book))
            Books.notinlib.append(issued)
            lib.task()
        elif self.book not in Books.libBooks and self.book in Books.notinlib:
            print("Sir, You Have Already Issued It.")
        else:
            print("Sorry Sir, We Don't Have That One.")

class Donation:
    def __init__(self, donate):
        self.donated = donate
        self.donated = str(input("Book To Donate -> "))
        if self.donated not in Books.libBooks:
            print("Thank You For Donating a Book.")
            lib.task()
            Books.libBooks.append((self.donated).title())
        elif self.donated in Books.libBooks:
            print("You Cannot Donate The Books Present In Library.")
            
class Sell:
    def __init__(self, sold):
        self.purchase = sold
        self.budget = 2500
        self.sold = str(input("Book To Sell -> "))
        if self.sold not in Books.libBooks:
            self.price = int(input("Price -> "))
            if self.price <= self.budget:
                print(f"Here's Your ₹ {self.price}")
                print("Thank You For Selling a Book.")
                Books.libBooks.append((self.sold).title())
                lib.task()
            elif self.price > self.budget:
                print("Sorry Sir, We Cannot Buy This As It Is Exceeding Our Budget.")
        else:
            print("You Cannot Sell The Books Present In Library.")

class Purchase:
    def __init__(self, purchase):
        self.purchase = purchase
        self.purchased = str(input("Book To Purchase -> "))
        self.cost = random.randint(500, 3200)
        if self.purchased in Books.libBooks or self.purchased in Books.notinlib:
            print(f"Cost Is Only ₹ {self.cost}")
            self.paid = int(input("Pay -> "))
            if self.purchased in Books.libBooks:
                if self.paid == self.cost:
                    print(f"Thank You For Purchasing {self.purchased}.")
                    Books.libBooks.pop(Books.libBooks.index(self.purchased))
                    lib.task()
                elif self.paid < self.cost:
                    print("Sorry Sir, The Paid Amount Is Less Than The Cost.")
                elif self.paid > self.cost:
                    print(f"Thank You Sir, Here's Your ₹ {self.paid - self.cost}")
                    Books.libBooks.pop(Books.libBooks.index(self.purchased))
                    lib.task()
            if self.purchased in Books.notinlib:
                if self.paid == self.cost:
                    pur = Books.notinlib.pop(Books.notinlib.index(self.purchased))
                    print(f"Thank You For Buying {pur}.")
                    lib.task()
                elif self.paid < self.cost:
                    print("Sorry Sir, The Paid Amount Is Less Than The Cost.")
                elif self.paid > self.cost:
                    print(f"Thank You Sir, Here's Your ₹ {self.paid - self.cost}")
                    pur = Books.notinlib.pop(Books.notinlib.index(self.purchased))
                    print(f"Thank You For Buying {pur}.")
                    lib.task()
        else:
            print("You Cannot Purchase This Item As This is Not Present In Library.")

class Return:
    def __init__(self, returns):
        self.returns = returns
        self.returned = str(input(("Book To Return -> ")))
        if self.returned in Books.notinlib:
            print(f"The Book Has Been Returned.")
            bookreturn = Books.notinlib.pop(Books.notinlib.index(self.returned))
            Books.libBooks.append(bookreturn)
            lib.task()
        elif self.returned not in Books.notinlib and self.returned in Books.libBooks:
            print("This Book Has Not Been Issue Yet.")
            lib.task()
        else:
            print("Invalid Book.")

lib = Library()
lib.info()
lib.task()