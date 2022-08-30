class Libarary:

    def __init__(self, list, name):

        self.ListOfLibaray = list

        self.Name = name

    def DisplayBook(self):

        print(self.ListOfLibaray)

    def AddBook(self):

        self.books = int(input("Enter number of books : "))

        if self.books > 0:

            for b in range(0, self.books):

                self.books = input()

                self.ListOfLibaray.append(self.books)

        else:

            print("please write integer number :(")

            return self.AddBook()

    def ReturnBook(self):

        self.Returnbooks = int(input("how much book to return to Libarary? "))

        if self.Returnbooks > 0:

            for b in range(0, self.Returnbooks):

                self.AreReturned = input()

                self.ListOfLibaray.append(self.AreReturned)
        else:

            print("please write integer number :(")

            return self.ReturnBook()

    def LendBook(self):

        print(self.ListOfLibaray)

        self.Lend = int(input("if you lend book write the Number of Book :"))-1

        if self.Lend > 0:

            print(f"The book is Lended is {self.ListOfLibaray.pop(self.Lend)}")
        else:
            print("please write integer number :(")

            return self.LendBook()


if __name__ == '__main__':

    Mohamed = Libarary(['Big Data', 'Data Struture', 'AI',
                       'Machin Learining'], "MohamedforProgramming")

    while(True):

        print(
            f"Welcome to the {Mohamed.Name} library. Enter your choice to continue")

        print("1. Display Books")

        print("2. Lend a Book")

        print("3. Add a Book")

        print("4. Return a Book")

        Choice = int(input())

        if Choice not in [1, 2, 3, 4]:

            print("Please enter a valid option")

            continue

        else:
            Choice = int(Choice)

        if Choice == 1:
            Mohamed.DisplayBook()

        elif Choice == 2:
            Mohamed.LendBook()

        elif Choice == 3:

            Mohamed.AddBook()

        elif Choice == 4:

            Mohamed.ReturnBook()

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        Choice2 = ""
        while(Choice2 != "c" and Choice2 != "q"):
            Choice2 = input()
            if Choice2 == "q":
                print("Nice to meet you , Good by :)")
                exit()

            elif Choice2 == "c":
                continue
