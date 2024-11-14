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
