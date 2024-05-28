## Funkcje wykorzystane do wykrywania oraz przygotowania tablicy rejestracyjnej:

1. `detect_and_straighten_plate(image: np.ndarray)`: Wykrywanie oraz prostowanie tablicy.
2. `process_plate_for_characters(plate_image: np.ndarray)`: Binaryzacja obrazu.
3. `resize_image(image: np.ndarray, width: int)`: Zmiana rozmiaru obrazu.

	Wszystkie funkcje zwracają odpowiednio przetworzony obraz

## Funkcje wykorzystane do wykrywania oraz rozpoznawania znaków:

Do rozpoznawania znaków został użyty algorytm KNN (K-Nearest Neighbors), który działa jako klasyfikator przypisując etykietę dla każdego wykrytego obrazu  znaku na podstawie podobieństwa do danych treningowych. Dane treningowe to obrazy znaków, które zostały odpowiednio przycięte tak aby znak zajmował jak największą powierzchnię 

1. `load_training_data(data_path: str)`: Ładowanie szablonów znaków. Zwraca dane treningowe oraz etykiety 
2. `recognize_characters(plate_bin: np.ndarray, knn)`: Wykrywanie i rozpoznawanie znakow. Zwraca rozpoznane znaki 


