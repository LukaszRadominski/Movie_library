Movie_library

Program :
    #  Wyświetla na konsoli komunikat Biblioteka filmów.
    #  Wypełnia bibliotekę treścią.
    #  Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
    #  Wyświetla na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
    #  Wyświetla listę top 3 najpopularniejszych tytułów.


Program, spełnia następujące założenia:

1 Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:
    # Tytuł
    # Rok wydania
    # Gatunek
    # Liczba odtworzeń

2 Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
    # Tytuł
    # Rok wydania
    # Gatunek
    # Numer odcinka
    # Numer sezonu 
    # Liczba odtworzeń

3 Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.

4 Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
       
5 Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.

6 Przechowuje filmy i seriale w jednej liście.

7 Zawiera  funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Sortuje listę wynikową alfabetycznie.

8 Zawiera funkcję search, która wyszukuje film lub serial po jego tytule.
 
9 Zawiera funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń. 

10  Zawiera funkcję, która uruchomi generate_views 10 razy.

11 Zawiera funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. 

Program wykorzystuje:
    # budowanie klasy
    # dziedziczenie klasy 
    # metodę zwiększającą liczbę odtworzeń filmów 
    # jedna wspólna listę wszytskich obiektów
    # iterację przez listę instancji klas
    # funkcje wbudowane isinstance() oraz is subclass()
    # polecenie input() wykorzystywane w funkcji wyszukiwania filmów
