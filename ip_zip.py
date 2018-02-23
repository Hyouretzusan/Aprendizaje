titles = ["Creature of habit", "Crewel fate"]
plots = ["A nun turns into a monster", "A haunted yarn shop"]
#ratings = ["5/10", "7/10"]
movies = {}
for title, plot, rating in zip(titles, plots):
    movies[title] = plot
print(movies)

newMovie = input("Ingrese título de la película: ")
append.titles(newMovie)
newplot = input("Ingrese el argumento: ")
append.plots(newplot)