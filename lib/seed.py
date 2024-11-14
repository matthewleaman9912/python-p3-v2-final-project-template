
from models.categories import Categories
from models.movies import Movies

def seed_database():
    Categories.drop_table()
    Movies.drop_table()
    Categories.create_table()
    Movies.create_table()

    action = Categories.create("Action")
    comedy = Categories.create("Comedy")
    drama = Categories.create("Drama")
    horror = Categories.create("Horror")
    romance = Categories.create("Romance")

    Movies.create("John Wick", 101, "Keanu Reeves", action.id)
    Movies.create("Deadpool & Wolverine", 127, "Ryan Reynolds", action.id)
    Movies.create("Taken", 93, "Liam Neeson", action.id)
    Movies.create("Superbad", 119, "Jonah Hill", comedy.id)
    Movies.create("The Hangover", 96, "Bradley Cooper", comedy.id)
    Movies.create("Step Brothers", 95, "Will Ferrell", comedy.id)
    Movies.create("Interstellar", 169, "Matthew McConaughey", drama.id)
    Movies.create("The Green Mile", 180, "Tom Hanks", drama.id)
    Movies.create("Gatsby", 143, "Leonardo DiCaprio", drama.id)
    Movies.create("The Conjuring", 112, "Vera Farminga", horror.id)
    Movies.create("Terrifier", 85, "David Howard Thornton", horror.id)
    Movies.create("The Ring", 110, "Daveigh Chase", horror.id)
    Movies.create("The Notebook", 121, "Ryan Gosling", romance.id)
    Movies.create("The Idea of You", 115, "Anne Hathaway", romance.id)
    Movies.create("50 First Dates", 106, "Adam Sandler", romance.id)

seed_database()
print("Seeded database")