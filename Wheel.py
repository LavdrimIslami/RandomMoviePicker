import csv
import random


list_of_movies = []

def create():
    global list_of_movies
    try:
        with open('Movies.csv', mode='r') as read_obj:
            reader = csv.reader(read_obj)
            list_of_movies = list(reader)
    except FileNotFoundError:
        print("File not found.")
       
def prin():
      create()
      for x in list_of_movies:
             print(x)
    

def roll():
    create()
    if list_of_movies:
        maxNum = len(list_of_movies)
        ranNum = random.randrange(0, maxNum)
        print(list_of_movies[ranNum])  
    else:
        print("The list is empty.")

def add():
    userValue = input("Enter the film:")
    list_of_movies.append([userValue])
    print("added " + userValue)
    update()

def update():
    global list_of_movies
    try:
        with open('Movies.csv', mode='w', newline='') as write_obj:
            writer = csv.writer(write_obj)
            writer.writerows(list_of_movies)
    except FileNotFoundError:
        print("File not found. Please check the file path and name.")



def manual():
    create()
    while True:
        decision = input("\n1.Roll\n2.Print list\n3.Add to list\n4.Exit\n")
        if decision == '1':
            roll()
        elif decision == '2':
            prin()
        elif decision == '3' :
            add()
        elif decision == '4':
             break
        else: 
            print("invalid")


manual()

