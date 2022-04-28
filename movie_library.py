print("BIBLOTEKA FILMÓW")

# # 1/ pierwsza klasa 
class Movie:

    def __init__(self, title, year, type, num_of_plays):
       self.title = title
       self.year = year
       self.type = type
       self.num_of_plays = num_of_plays
    
    def increase_num_of_plays(self, step=1): # 3 dodałem metodę  play wyrażająca obiekt która zwiększa liczbę odtworzeń danego tytułu o 1 jako sring
       self.num_of_plays += step

    def __str__(self): #DODATKOWO : dodałem metodę wyrażająca obiekt jako sring tj sposób w jaki bedzą wyświatlane info przy iteracji 
        return f'{self.title} {self.year} {self.type} {self.num_of_plays}'



      
# 2/ druga klasa - dziedziczona po klasie Movie 
class Serial(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.episode_number = episode_number
       self.season_number = season_number

    def __str__(self): # DODATKOWO dodałem metodę wyrażająca obiekt jako sring tj sposób w jaki bedzą wyświatlane info przy iteracji 
        return f'{self.title} {self.year} {self.type} {self.num_of_plays} {self.episode_number} {self.season_number} '  
    

# BIBLIOTEKA MOJA  
movie = Movie(title  = "Miami vice", year = "1983", type  = "action", num_of_plays = 3)
movie_two = Movie(title  = "The_Gendarme_of_Saint_Tropez", year = "1961", type  = "comedy", num_of_plays = 15)
serial = Serial(title  = "Friends", year = "1994", type  = "comedy", num_of_plays = 45, episode_number = 2, season_number = 3 )
serial_two = Serial(title  = "Black Adder", year = "1982", type  = "comedy", num_of_plays = 30, episode_number = 4, season_number = 4 )