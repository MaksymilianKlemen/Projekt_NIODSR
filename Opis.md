## Opis
Celem projektu jest wykorzystanie szczegółowych statystyk z sezonu zasadniczego NBA oraz z poprzednich lat do utworzenia modelu, ktory zostanie wykorzystany do przewidywania listy zawodników, którzy otrzymają nagrody za sezon zasadniczy 2023/2024. Przewidywania obejmują:
- All-NBA Team (trzy piątki)
- All-Rookie Team (dwie piątki)

Kod projektu został podzielony na 3 części:
1. Przygotowanie danych
2. Trenowanie modelu
3. Wykonanie predykcji

### Przygotowanie danych  ###
W tej części wykonano połączenie danych ze wszystkich sezonów, zdefiniowano i przetworzono dane treningowe oraz wykonano niezbędne operacje do utworzenia modelu.

## Łączenie wszystkich danych sezonowych w jeden DataFrame
Program wczytuje oraz łączy wszystkie dostępne dane. W celu rozpoznania, z którego sezonu pochodzą, dodano kolumnę 'SEASON'. Następnie wszystkie dane ze wszystkich sezonów są łączone w jeden DataFrame.

## Dane treningowe 
Do trenowania modelu wykorzystano nastepujace cechy:
```
    -AGE: wiek gracza
    -GP: liczba rozegranych meczów
    -W: liczba zwycięstw drużyny
    -L: liczba porażek drużyny
    -MIN: liczba minut gry
    -FGM: średnia liczba celnych rzutów z gry na mecz
    -FG_PCT: procent celnych rzutów z gry
    -FG3A: średnia liczba oddanych rzutów za 3 punkty na mecz
    -STL: średnia liczba przechwytów na mecz
    -BLK: średnia liczba bloków na mecz
    -PTS: średnia liczba punktów na mecz
    -DD2: liczba punktów double-double w meczu
    -AST_RANK: Ranking asyst
    -TOV_RANK: Ranking strat
    -TD3_RANK: Ranking punków ttriple-double
```

## Przetwarzanie cech
Do przetwarzania danych wykorzystano 'ColumnTransformer', który umożliwia zastosowanie różnych transformacji dla każdej z kolumn. W tym przypadku używany jest on do standaryzacji cech numerycznych za pomocą 'StandardScaler'.

### Trenowanie modelu ###
Utworzono pipeline, który najpierw przetwarza cechy, a następnie trenuje model. Ze względu na brak utworzenia targetu z zawodnikami, którzy otrzymali nagrody za poprzednie sezony wykorzystano RandomForestRegressor (Estymator wykorzystujący uśrednianie w celu poprawy dokładności predykcji i zapobieganiu over-fitting'u). 
Zmienna docelowa (target) w tym przypadku to ranking punktowy (PTS_RANK), który jest wyliczany na podstawie statystyk. Wyniki predykcji były na zadowalającym poziomie, dlatego nie testowano innych modeli.
 
Do znaleznia jak najlepszych hiperparametrow do 'RandomForestRegressor' zastosowano:
* `GridSearchCV`: Przeszukiwanie siatki polega na trenowaniu modelu dla wszystkich kombinacji zadanych parametrów i wybieraniu tych, które dają najlepsze wyniki.
Wykorzystuje cross-validation i MSE (Błąd średniokwadratowy) do oceny modelu
* Wykorzystane parametry: 
	* `n_estimators`: liczba drzew w lesie losowym. Więcej drzew może poprawić wydajność modelu, ale zwiększa czas obliczeń
    	* `max_depth`: maksymalna głębokość drzewa. Ograniczenie głębokości drzewa może zapobiec over-fitting'u
    	* `min_samples_split`: minimalna liczba próbek wymagana do podziału węzła. Większe wartości mogą prowadzić do bardziej ogólnych modeli
    	* `min_samples_leaf`: minimalna liczba próbek wymagana, aby węzeł został liściem. Większe wartości mogą pomóc w zapobieganiu over-fitting'u

Najlepszy znaleziony model jest zapisywany do pliku model.pkl

## Wykonanie predykcji
W celu wykonania predykcji All-NBA Team dane z sezonu są ładowane, a następnie zostaje utworzona macierz cech. 
Po wykonaniu predykcji program dodaje kolumnę 'PREDICTED_RANK' z predykcjami do danych sezonu i sortuje dane według niej. 
Po przesortowaniu danych wybranych zostaje 15 pierwszych zawodników, a następnie są oni dzieleni na 3 piątki.

Przed wykonaniem predykcji dla All-Rookie Team ładowane są dane z poprzedniego sezonu i są one porównywane z aktualnym. 
Jeżeli jakiś zawodnik dopiero pojawił się w aktualnym sezonie, określany jest jako rookie. 
Następnie postępujemy analogicznie, tak jak z predykcją All-NBA Team.

Na koniec wyniki są wyświetlane oraz zapisywane do pliku JSON.