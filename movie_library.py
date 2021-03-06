import random

from datetime import date



# # 1/ pierwsza klasa 
class Movie:

    def __init__(self, title, year, type, num_of_plays):
       self.title = title
       self.year = year
       self.type = type
       self.num_of_plays = num_of_plays
    
    def increase_num_of_plays(self, step=1): # 3 dodałem metodę  play która zwiększa liczbę odtworzeń danego tytułu o 1 
       self.num_of_plays += step

    def __str__(self): #DODATKOWO : dodałem metodę wyrażająca obiekt jako sring tj sposób w jaki będzą wyświatlane argumenty  podczs iteracji 
        return f'{self.title} {self.year} {self.type} {self.num_of_plays}'


# 2/ druga klasa - dziedziczona po klasie Movie 
class Serial(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.episode_number = episode_number
       self.season_number = season_number

    def __str__(self): # DODATKOWO dodałem metodę wyrażająca obiekt jako sring tj sposób w jaki będzą wyświatlane argumenty  podczs iteracji 
        return f'{self.title} {self.year} {self.type} {self.num_of_plays} {self.episode_number} {self.season_number} '  
    

# BIBLIOTEKA  
movie = Movie(title  = "Miami vice", year = "1983", type  = "action", num_of_plays = 3)
movie_two = Movie(title  = "The_Gendarme_of_Saint_Tropez", year = "1961", type  = "comedy", num_of_plays = 15)
serial = Serial(title  = "Friends", year = "1994", type  = "comedy", num_of_plays = 45, episode_number = 22, season_number = 14 )
serial_two = Serial(title  = "Black Adder", year = "1982", type  = "comedy", num_of_plays = 30, episode_number = 4, season_number = 4 )


# 6/ Przechowywanie  filmów i seriali w jednej liście 
one_list = [movie,movie_two, serial,serial_two]


print("BIBLOTEKA FILMÓW \n")

# 4/  Wypełnienie biblioteię treścią. Po wyświetleniu serialu jako string pokazywane  np.: “The Simpsons S01E05” lub “Pulp Fiction (1994)”. 
for i in one_list:
    if not isinstance(i, Serial):
        print(f"{i.title},{i.year}")
    else:
        if i.season_number < 10: 
            print(f"{i.title} S{0}{i.season_number}E{0}{i.episode_number}")
        else:   
            print(f"{i.title} S{i.season_number}E{i.episode_number}")

# 7 Funkcje get_movies oraz get_series, które filtrują listę i zwracają odpowiednio tylko filmy oraz tylko seriale. Sortowanie listy wynikowej alfabetycznie. 
by_title = sorted(one_list, key=lambda movie: movie.title)

def  get_movies():
    for i in by_title:
        if not isinstance(i, Serial):
            print(f"{i.title},{i.year},{i.type},{i.num_of_plays}")
        else:
            pass

def  get_series():
    for i in by_title:
        if not isinstance(i, Serial):
            print(f"{i.title},{i.year},{i.type},{i.num_of_plays},{i.episode_number},{i.season_number} ")
        else:
            pass


# 8 Funkcja search, która wyszukuje film lub serial po jego tytule. 
def search_movies():
    print(f"Wpisz tytułu filmu:")
    search = input()
    zmienna = False 
    for i in one_list:
        if i.title == search:
            zmienna = True
            print(f"{i.title},{i.year},{i.type}")
        else:
            pass
    if zmienna == False:
        print("Brak takiego tytułu. Wpisz  raz jeszcze")
        search_movies()


# 9 Funkcja generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_vievs():
    random_movie = random.choice(one_list)
    random_nop = random.randrange(1,100)
    random_movie.num_of_plays = int(i.num_of_plays)+random_nop
    print(f"{random_movie.title}, {random_movie.num_of_plays}")


# 10  Funkcja, która uruchomi generate_views 10 razy.
print("\n")
def ten_times_generate_views(amount):
    for i in range (1,amount+1):    
        generate_vievs()

ten_times_generate_views(10)


# 11 Funkcja top_titles(), która zwraca wybraną ilość najpopularniejszych tytułów z biblioteki. 
# Wyświetla na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
# Wyświetla listę top 3 najpopularniejszych tytułów.

print("\n")

by_num_of_plays = sorted(one_list, key=lambda movie: movie.num_of_plays, reverse=True)

today = date.today()
d1 = today.strftime("%d.%m.%Y")

def top_titles(how_many_titles):
    print(f"Najpopularniejsze filmy i seriale dnia {d1}:")
    for i in by_num_of_plays[:how_many_titles]:
        if not isinstance(i, Serial):
            print(f"{i.title},{i.num_of_plays},{i.year},{i.type}")
        else:
            print(f"{i.title},{i.num_of_plays},{i.year},{i.type},{i.season_number},{i.episode_number}")

top_titles(3)


