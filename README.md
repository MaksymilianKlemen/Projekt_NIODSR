## Opis
Projekt wykorzystuje model do predykcji listy zawodników, którzy otrzymają nagrody za sezon zasadniczy. Model przewiduje zawodników nominowanych do:
- All-NBA Team (trzy piątki)
- All-Rookie Team (dwie piątki)

Kod projektu został podzielony na 3 części:
1. Przygotowanie danych
2. Trenowanie modelu
3. Wykonanie predykcji

## Dane treningowe 
Do trenowania modelu wykorzystano nastepujace cechy:
    -'AGE': (wiek gracza)
    -'GP': (liczba rozegranych meczów)
    -'W': (liczba zwycięstw drużyny)
    -'L': (liczba porażek drużyny)
    -'W_PCT': (procent zwycięstw drużyny)
    -'MIN': (liczba minut gry)
    -'FGM': (średnia liczba celnych rzutów z gry na mecz)
    -'FGA': (średnia liczba oddanych rzutów z gry na mecz)
    -'FG_PCT': (procent celnych rzutów z gry)
    -'FG3M': (średnia liczba celnych rzutów za 3 punkty na mecz)
    -'FG3A': (średnia liczba oddanych rzutów za 3 punkty na mecz)
    -'FG3_PCT': (procent celnych rzutów za 3 punkty)
    -'FTM': (średnia liczba celnych rzutów wolnych na mecz)
    -'FTA': (średnia liczba oddanych rzutów wolnych na mecz)
    -'FT_PCT': (procent celnych rzutów wolnych)
    -'OREB': (średnia liczba zbiórek ofensywnych na mecz)
    -'DREB': (średnia liczba zbiórek defensywnych na mecz)
    -'REB': (średnia liczba zbiórek na mecz)
    -'AST': (średnia liczba asyst na mecz)
    -'TOV': (średnia liczba strat na mecz)
    -'STL': (średnia liczba przechwytów na mecz)
    -'BLK': (średnia liczba bloków na mecz)
    -'BLKA': (średnia liczba zablokowanych rzutów na mecz)
    -'PF': (średnia liczba fauli na mecz)
    -'PFD': (średnia liczba wymuszonych fauli na mecz)
    -'PTS': (średnia liczba punktów na mecz)
    -'PLUS_MINUS': (średnia różnica punktów z zawodnikiem na boisku)
    -'NBA_FANTASY_PTS': (punkty fantasy NBA)
    -'DD2': (liczba podwójnych punktów w meczu)
    -'TD3': (liczba potrójnych punktów w meczu)

## Przetwarzanie danych
Do przetwarzania danych wykorzystano 'ColumnTransformer', który umożliwia zastosowanie różnych transformacji dla każdej z kolumn. W tym przypadku używany jest on do standaryzacji cech numerycznych za pomocą 'StandardScaler'

## Zastosowane metody 
-'RandomForestRegressor': Estymator wykorzystujący uśrednianie w celu poprawy dokładności predykcji i zapobieganiu over-fitting'u
-'GridSearchCV': Zastosowany w celu znaleznia jak najlepszych hiperparametrow do 'RandomForestRegressor'. Wykorzystuje cross-validation i MSE (Błąd średniokwadratowy) do oceny modelu
-Wykorzystane parametry: 
	-'n_estimators': liczba drzew w lesie losowym. Więcej drzew może poprawić wydajność modelu, ale zwiększa czas obliczeń
    	-'max_depth': maksymalna głębokość drzewa. Ograniczenie głębokości drzewa może zapobiec over-fitting'u
    	-'min_samples_split': minimalna liczba próbek wymagana do podziału węzła. Większe wartości mogą prowadzić do bardziej ogólnych modeli
    	'min_samples_leaf': minimalna liczba próbek wymagana, aby węzeł został liściem. Większe wartości mogą pomóc w zapobieganiu over-fitting'u
    	

