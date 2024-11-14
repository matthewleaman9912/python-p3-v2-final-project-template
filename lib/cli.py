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
