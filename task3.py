class my_lib:
    def __init__(self,li,name):
        self.list=li
        self.name=name
        self.lend={}

    def display(self):
        print("The books available are:-{self.name}")
        for book in self.list:
            print(book)
    def lend_book(self,person,book):
        if book not in self.lend.keys():
            self.lend.update({book:person})
            print("Your book database is updated,please take your book")
        else:
            print("Book is already been bought")
    def add(self,book):
        self.list.append(book)
        print("Book is added to the list")
    def return_book(self,book):
        self.lend.pop(book)

if __name__=='__main__':
    techedu =my_lib(["B.S Grewal","Principles of Physics","CS by PEARSON","Surveying_2"],"Shrav's DICTIONARY")
    while(True):
        print("Welcome")
        print("Enter Your Choice")
        print("1.Display books")
        print("2.Lend a book")
        print("3.Add books")
        print("4.Return books")
        person_choice=int(input())
        if person_choice ==1:
            techedu.display()
        elif person_choice ==2:
            book=input("enter the name of book")
            person=input("enter your name")
            techedu.lend_book(person,book)
        elif person_choice ==3:
            book=input("enter the name of book ")
            techedu.add(book)
        elif person_choice ==4:
            book=input("enter the name of book ")
            techedu.return_book(book)
        else:
            print("please enter valid input")

        print("Press q to quit or c to continue")
        person_c=""
        while(person_c!="q"and person_c!="c"):
            person_c=input()
            if person_c=="q":
                exit()
            if person_c=="c":
                continue

