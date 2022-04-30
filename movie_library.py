print("BIBLOTEKA FILMÓW")

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
serial = Serial(title  = "Friends", year = "1994", type  = "comedy", num_of_plays = 45, episode_number = 2, season_number = 3 )
serial_two = Serial(title  = "Black Adder", year = "1982", type  = "comedy", num_of_plays = 30, episode_number = 4, season_number = 4 )


# 6/ Przechowywanie  filmów i seriali w jednej liście 
one_list = [movie,movie_two, serial,serial_two]

# 4/  Po wyświetleniu serialu jako string pokazywane się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” 
# (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
# 5/ Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”. 

# #### BRAKUJE NOTACJI 2-CYFROWEJ #####

# CSN: odwołanie w  pętli do listy - bez nawiasów 

for i in one_list:
    if isinstance(i, Serial) == False:
        print(f"{i.title},{i.year}")
    else:
        print(f"{i.title},{i.season_number},{i.episode_number}")

# 7.1 Funkcje get_movies oraz get_series, które filtrują listę i zwracają odpowiednio tylko filmy oraz tylko seriale. Sortowanie listy wynikowej alfabetycznie. 
print("\n")

by_title = sorted(one_list, key=lambda movie: movie.title)

def  get_movies():
    for i in by_title:
        if isinstance(i, Serial) == False:
            print(f"{i.title},{i.year},{i.type}")
        else:
            pass

get_movies()

print("\n")
def  get_series():
    for i in by_title:
        if isinstance(i, Serial) == True:
            print(f"{i.title},{i.year},{i.type},{i.num_of_plays},{i.episode_number},{i.season_number} ")
        else:
            pass

get_series()


# 8 Funkcja search, która wyszukuje film lub serial po jego tytule. 
print("\n")

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
    
search_movies()

# 9 Funkcja generate_views, która losowo wybiera element z biblioteki, 
# a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.

# ##### BRAKUJE LOSOWEGO WYBIERANIA sample() / random() / uniform() - FUNKCJA OBECNIE DODAJE 1 ODTWORZENIE DO KAŻDEGO ELEMENTU ######
print("\n")

print("Lista bazowa- wersja testowa")
for i in one_list:
    if isinstance(i, Serial) == False:
        print(f"{i.title},{i.num_of_plays}")
    else:
        print(f"{i.title},{i.num_of_plays}")  

print("Lista po dodaniu wyświetleń")
def generate_vievs():
    for i in one_list:
        i.num_of_plays = int(i.num_of_plays)+1
        print(f"{i.title}, {i.num_of_plays}")

generate_vievs()

# 10  Funkcja, która uruchomi generate_views 10 razy.
print("\n")

def ten_times_generate_views(amount):
    for i in range (1,amount+1):
        def generate_vievs():
            for i in (one_list):
                i.num_of_plays = int(i.num_of_plays)+1
                print(f"{i.title}, {i.num_of_plays}")
        generate_vievs()

ten_times_generate_views(10)

# 11 Funkcję top_titles(), która zwraca wybraną ilość najpopularniejszych tytułów z biblioteki. 

###  + Wyświetla na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
###  Wyświetla listę top 3 najpopularniejszych tytułów.
print("\n")

by_num_of_plays = sorted(one_list, key=lambda movie: movie.num_of_plays, reverse=True)
print(by_num_of_plays)

print("\n")

print("Lista posortowana- wersja testowa")

for i in by_num_of_plays:
    if isinstance(i, Serial) == False:
        print(f"{i.title},{i.num_of_plays},{i.year},{i.type}")
    else:
        print(f"{i.title},{i.num_of_plays},{i.year},{i.type},{i.episode_number},{i.season_number}")

print()
print("Lista obiektów - 2 o największej liczbie wyświetleń ")
# to wyświetli tylko adress
def top_titles(how_many_titles):
    print(by_num_of_plays[how_many_titles:])
top_titles(2)

#CSN: iteracja listy  + wywołanie tylko wskazanych z iterowanych elementów  +  podanie ich nazwy 

def top_titles(how_many_titles):
    for i in by_num_of_plays[:how_many_titles]:
        if isinstance(i, Serial) == False:
            print(f"{i.title},{i.num_of_plays},{i.year},{i.type}")
        else:
            print(f"{i.title},{i.num_of_plays},{i.year},{i.type},{i.episode_number},{i.season_number}")

top_titles(3)


