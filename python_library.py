

import os

book_list = list()


menu = """
1) Enter a book
2) Select a book
3) List all books
Q) Quit
"""

def enter_a_book(book:tuple,list_book:list):
    list_book.append(book)
    print("Thank you for adding books to our library :))")
    input("Press Enter to return menu")
def control(book:tuple,list_book:list):
    if book in list_book:
        return True
    else:
        return False
def select_book(book:tuple,list_book:list):
    if control(book,list_book):
        list_book.remove(book)
        print("You have chosen the book well, have a good read. Thank you")
        input("Press Enter to return menu")
    else:
        print("Unfortunately, the book you want to choose is not available. We are sorry")
        input("Press Enter to return menu")
def list_all_books(list_book: list):
    for a in list_book:

        print("Book name : {}         Author : {}     Published Year : {}".format(a[0],a[1],a[2]))
    input("Press Enter to return menu")
while True:
    os.system("cls")
    print(menu)
    choise = input("Enter the number of the transaction you want to do :  ")

    if choise == "1":
        book_name = input("Book name :")
        Author_name = input("Author  :")
        published_year = int(input("Published year : "))
        book = (book_name, Author_name, published_year)
        if book in book_list:
             print("This book is already available in the library ")
             input("Press Enter to return menu..")
        else:
            enter_a_book(book, book_list)



    elif choise == "2":
        book_name = input("Book name :")

        book = (book_name, Author_name, published_year)
        select_book(book, book_list,)
    elif choise == "3":
        list_all_books(book_list)

    elif choise == "q" or choise == "Q" :
        print("BYE BYE")
        quit()
    else:
        print("You have made an incorrect operation, please be careful...")
        input("Press Enter to return menu")


