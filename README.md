# Phase 3 Movie Database CLI ORM Project

---

## Introduction

This is my CLI (Command Line Interface) project for a movie database. I have created this CLI to help users to intereact with the databse in a few different ways. These few  ways include listing all movie objects, listing objects based on specific attributes, creating new objects, deleteing current objects, and listing specific attributes of some movies. This CLI is designed for users rather than programmers, so the entire CLI is meant to be as user friendly as possible.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── categories.py
    |   └── movies.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Below will be the different files that have been edited to create this CLI and a brief explanation about how they all work together to perform the different functions.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---
Below is the CLI for the project, I will give a brief explanation for each piece of this, including the functions. 

The import of functions from the 'helpers' file is used to allow the CLI to accomplish goals given from the user. Each of these functions complete their own task, which I will touch on later.

The main() section is what sets the CLI up and allows me to modify what the user will see. The menu_0() along with the other menus that can be seen throughout the rest of the main() section are the different direct outputs that the user will see on the screen that allows the programmer to give options to select from. In this case, the menus show the user options of different movie options or categories to see or learn more about their attributes. 

Next you will see a 'choice = input()' statement. This allows the CLI to prompt the user for a selection based on the provided choices, then record that choice or response as a variable. This is crucial to making the next step for the CLI because we can use this response to filter the out the next options to give to the user, as well as what the final goal is for the user while using the CLI.

After that, there are many 'if choice = "" ' statements. These statements are used to take the input the user gives in the previous section and choose, based on the users response, what the CLI should do. Each one of these statements is another piece of what this CLI can perform.

## CLI Below 
```py
# lib/cli.py

from helpers import (
    exit_program,
    all_movies,
    long_movies,
    short_movies,
    actors,
    categories,
    new_genre,
    action_movies,
    comedy_movies,
    drama_movies,
    horror_movies,
    romance_movies,
    remove_genre,
    update_genre,
    other_movies,
    new_movie,
    remove_movie,
    
)

def main():
    while True:
        menu_0()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Here are all the movies in the database!: ")
            all_movies()
        elif choice == "2":
            print("Genre specifications are listed below!: ")
            choice1 = 1
            while choice1 != 0:
                genre_menu()
                choice2 = input("Select an option above!: ")
                if choice2 == "0":
                    choice1 -= 1
                elif choice2 == "1":
                    action_movies()
                elif choice2 == "2":
                    comedy_movies()
                elif choice2 == "3":
                    drama_movies()
                elif choice2 == "4":
                    horror_movies()
                elif choice2 == "5":
                    romance_movies()
                elif choice2 == "6":
                    other_movies()
                else:
                    print("Please select an option listed!")
        elif choice == "3":
            choice1 = 1
            while choice1 != 0:
                print("Would you like to see short or long movies?")
                length_menu()
                decision = input("Please select an option!: ")
                if decision == "0":
                    choice1 -= 1
                elif decision == "1":
                    short_movies()
                elif decision == "2":
                    long_movies()
                else:
                    print("Please select an option listed!")
        elif choice == "4":
            choice1 =1
            while choice1 != 0:
                print("Here are all the actors in the database!: ")
                actors()
                actors_menu()
                decision = input("Please select an option!: ")
                if decision == "0":
                    choice1 -= 1
                elif decision == "1":
                    new_movie()
                elif decision == "2":
                    remove_movie()
                else:
                    print("Please select an option listed!")
        elif choice == "5":
            choice1 = 1
            while choice1 !=0:
                categories_menu()
                choice = input("Please select an option!: ")
                if choice == "0":
                    choice1 -= 1
                elif choice == "1":
                    print("Here are all the current genres in the database!: ")
                    categories()
                elif choice == "2":
                    new_genre()
                elif choice == "3":
                    remove_genre()
                elif choice == "4":
                    update_genre()
        else:
                    print("Please select an option listed!")

def menu_0():
    print("Welcome to the Movie Database! Please select an option below!:")
    print("0. Exit the program")
    print("1. See all movies!")
    print("2. See all movies with a specific genre!")
    print("3. See all movies with length specifications!")
    print("4. See options for actors in the movies!")
    print("5. See options for genres of movies!")

def genre_menu():
    print("0. Go back to the home screen!")
    print("1. Show Action Movies!")
    print("2. Show Comedy Movies!")
    print("3. Show Drama Movies!")
    print("4. Show Horror Movies!")
    print("5. Show Romance Movies!")
    print("6. Show Other Movies not in these main genres!")
    
def length_menu():
    print("0. Go back to the home screen!")
    print("1. Show short movies!")
    print("2. Show long movies!")

def actors_menu():
    print("0. Go back to the home screen!")
    print("1. Add a new movie and with a new actor!")
    print("2. Remove a movie and its' actor!")

def categories_menu():
    print("0. Go back to the home screen!")
    print("1. Show all genres!")
    print("2. Add a new genre!")
    print("3. Remove a genre!")
    print("4. Update a current genre!")

if __name__ == "__main__":
    main()

```

All of the functions being imported in this section can now be explained. Below each function will be listed with a brief description on what they do.

    * exit_program() - This function allows the user to exit the CLI
    * all_movies() - This function allows the user to view all movies in the database with a brief description of the movie title, movie length, and the actor in the movie.
    * long_movies() - This function allows the user to view movies that have a length of over 120 minutes, and puts the movie title followed by 'is a long movie'
    * short_movies() - This function allows the user to view movies that have a length of less than 120 minutes, and puts the movie title followed by 'is a short movie'
    * actors() - This function allows the user to view all of the actors that are in the database, along with a brief statement saying what movie they star in.
    * new_movie() - This function allows the user to create a new movie for the database. It prompts the user for the new movie title, movie length, movie actor, and the movie category. As long as the new movie attributes meet each qualification, The movie will be added to the database and the CLI will prompt a message explaining that it has been added. If not, the CLI will prompt a message explaining why it wasnt added.
    * remove_movie() - This function allows the user to delete a movie from the database. It prompts the user for a movie title to delete, and if that movie is in the database then it will be deleted. If not, the CLI will prompt a message saying to 'please try again'
    * categories() - This function allows the user to view all of the categories of movies currently in the database.
    * action_movies() - This function allows the user to view all of the action movies in the database, along with a brief message showing the movies title, length and actor.
    * comedy_movies() - This function allows the user to view all of the comedy movies in the database, along with a brief message showing the movies title, length and actor.
    * drama_movies() - This function allows the user to view all of the drama movies in the database, along with a brief message showing the movies title, length and actor.
    * horror_movies() - This function allows the user to view all of the horror movies in the database, along with a brief message showing the movies title, length and actor.
    * romance_movies() - This function allows the user to view all of the romance movies in the database, along with a brief message showing the movies title, length and actor.
    * other_movies() - This function allows the user to view all of the movies not in one of the main 5 categories but still in the database, along with a brief message showing the movies title, length and actor.
    * new_genre() - This function allows the user to create a new genre for the database. The CLI prompts the user for a new genre, then provides a message that the new genre has been added successfully as long as the genre meets the qualifications. If not then there will be an error message.
    * remove_genre() - This function allows the user to use the CLI to remove a genre from the database. This will provide a message saying that the genre has been deleted as long as it exists in the database and an error if not.
    * update_genre() - This function allows the user to change the name of a genre. The CLI will prompt a message asking for the new name, then update the genres name. If the genre cant be updated because it is not in the database, then the will be an error message.

```py
# lib/helpers.py
from models.categories import Categories
from models.movies import Movies

def exit_program():
    print("Goodbye!")
    exit()

def all_movies():
    movies = Movies.get_all()
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def long_movies():
    movies = Movies.get_all()
    for movie in movies:
        if movie.length >= 120:
            print(f'{movie.title} is a long movie!')

def short_movies():
    movies = Movies.get_all()
    for movie in movies:
        if movie.length < 120:
            print(f'{movie.title} is a short movie!')

def actors():
    movies = Movies.get_all()
    for movie in movies:
        print(f'{movie.actor} is in {movie.title}')

def new_movie():
    title = input("What's the name of your new movie?: ")
    length = int(input("How long is your new movie in minutes?: "))
    actor = input("What's the actor's name in your movie?: ")
    print("Would you like to create a 1. Action Movie, 2. Comedy Movie, 3. Drama Movie, 4. Horror Movie, 5. Romance Movie?")
    category = int(input("Please select an option for your genre: "))
    try:
        movie = Movies.create(title, length, actor, category)
        print(f'{movie.title} starring {movie.actor} has been added to the database!')
    except Exception as exc:
        print("Sorry try again!: ", exc)

def remove_movie():
    movie = input("What movie would you like to delete?: ")
    if title := Movies.find_by_title(movie):
        title.delete()
        print(f'{title.actor} from {title.title} has been deleted!')
    else: 
        print("Please try again!")

def categories():
    genres = Categories.get_all()
    for genre in genres:
        print(f'{genre.category}')

def action_movies():
    print("Bang! Pow! Action Movies Below!: ")
    movies = Movies.find_by_category(1)
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def comedy_movies():
    print("HAHAHA! Comedy Movies Below!: ")
    movies = Movies.find_by_category(2)
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def drama_movies():
    print("What's Next? Drama Movies Below!: ")
    movies = Movies.find_by_category(3)
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def horror_movies():
    print("Ahhh! Horror Movies Below!: ")
    movies = Movies.find_by_category(4)
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def romance_movies():
    print("Awww! Romance Movies Below!: ")
    movies = Movies.find_by_category(5)
    for movie in movies:
        print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def other_movies():
    print("Other Movies Below!: ")
    movies = Movies.get_all()
    for movie in movies:
        if movie.category_id > 5:
            print(f'{movie.title} is {movie.length} minutes long and has {movie.actor} starring in it!')

def new_genre():
    new_category = input("What is your new genre?: ")
    try:
        genre = Categories.create(new_category)
        print(f'{genre} has been added to the database!')
    except Exception as exc:
        print("Sorry try again!: ", exc)
    
def remove_genre():
    genre = input("What genre would you like to delete?: ")
    if category := Categories.find_by_category(genre):
        category.delete()
        print(f'{genre} is deleted! Poof!')
    else:
        print("Please try again!")

def update_genre():
    genre = input("What genre would you like to update?: ")
    if category := Categories.find_by_category(genre):
        change = input("What would you like this genre to be called?: ")
        category.category = change
        category.update()
        print(f'{category} is changed!')
    else:
        print("Please try again!")

```

---

## Other Python Files Updated

In the models folder, there are 2 files that were updated in this project:

    * categories.py - This file creates the foundation for the category table. This file also creates the error messages and qualifications for each attribute of the category. Class methods are created in this file as well using sql so that the other files are able to perform functions on this section of the database. 

    * movies.py - This file creates the foundation for the movies table. This file also creates the error messages and qualifications for each attribute of the movies. Class methods are created in this file as well using sql so that the other files are able to perform functions on this section of the database. 

There is also another file that was updated during this project:

    * debug.py - This file was used to create the initial database entires. It starts by dropping the tables for categories and movies if there are any current ones. Then, there are new tables created for each of these files. The file then proceeds to create a new category for each genre of movie in the database, followed by 3 movies of each genre being created. This file creates the foundation database that the CLI uses to provide the user with information on the movies.

---

## Conclusion

Overall, this CLI project performs a lot of different functions to provide the user with an optimal experience and plenty of choices while accessing the information in the movies database. Hopefully this CLI provides all the information that the user would like to know about the movies and if not, then that information should be able to be added through the CLI as well! Thanks for reading!

---
