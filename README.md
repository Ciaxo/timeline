# TimeLine

Projekt "TimeLine" jest narzędziem stworzonym w języku Python, który umożliwia efektywne rozwiązanie zagadki poprzez ułatwienie zapisu, manipulacji oraz wizualizacji informacji zawartych w książce. Głównym celem projektu jest zastosowanie systemu kategorii do analizy i porządkowania informacji na podstawie stron książki, co ułatwia ustalanie kolejności wydarzeń oraz ich zrozumienie.

## Opis projektu

Projekt składa się z dwóch głównych komponentów:
- **LiniaCzasuApp**: Interfejs umożliwiający wizualizację i manipulację kropkami na linii czasu.
- **OknoZLabelami**: Okna dialogowe do edycji szczegółowych informacji związanych z każdą kropką na linii czasu.

### LiniaCzasuApp

Klasa `LiniaCzasuApp` tworzy interaktywny interfejs, który zawiera linię czasu oraz umożliwia dodawanie, przesuwanie, edycję i usuwanie kropek reprezentujących wydarzenia na osi czasu.

#### Funkcje

- `rysuj_linie_czasu`: Funkcja rysuje linię czasu i aktualizuje pozycje kropek na podstawie danych z pliku.
- `dodaj_kropke`: Funkcja dodaje nową kropkę na linii czasu po kliknięciu prawym przyciskiem myszy.
- `przesuwaj_kropke`: Funkcja umożliwia przesuwanie kropki na linii czasu po kliknięciu lewym przyciskiem myszy i jej przeciągnięciu.
- `usun_kropke`: Funkcja usuwa kropkę z linii czasu po kliknięciu prawym przyciskiem myszy.
- `wyswietl_okno_z_labelami`: Funkcja wyświetla okno dialogowe z szczegółowymi informacjami o wybranej kropce po podwójnym kliknięciu lewym przyciskiem myszy.

### OknoZLabelami

Klasa `OknoZLabelami` odpowiada za wyświetlanie okna dialogowego z pięcioma kategoriami informacji związanymi z każdą kropką na linii czasu.

#### Funkcje

- `edytuj_tekst`: Funkcja umożliwia edycję tekstów dla każdej z pięciu kategorii (pora roku, pora dnia, miejsce, osoby, wydarzenia) po podwójnym kliknięciu na odpowiedni label.
- `wczytaj_dane` i `zapisz_dane`: Funkcje wczytują i zapisują dane do pliku tekstowego "info.txt" zgodnie z indeksem kropki na linii czasu.

### Technologie

Projekt wykorzystuje bibliotekę `tkinter` do budowy interfejsu graficznego oraz operacje na plikach tekstowych do przechowywania danych o kropkach i ich kolorach.
