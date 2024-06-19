import tkinter as tk
from tkinter import simpledialog, colorchooser

class OknoZLabelami:
    def __init__(self, root, cyfra):
        self.root = root
        self.root.title(f"Kropka {cyfra}")
        self.cyfra = cyfra

        # Label 1
        self.label1 = tk.Label(root, text="Pora roku:")
        self.label1.grid(row=0, column=0, sticky=tk.E)

        self.tekst_label1 = tk.StringVar()
        self.tekst_label1.set(self.wczytaj_dane("info.txt", cyfra, 1))

        self.label1_tekst = tk.Label(root, textvariable=self.tekst_label1)
        self.label1_tekst.grid(row=0, column=1, sticky=tk.W)
        self.label1_tekst.bind("<Double-Button-1>", lambda event, textvar=self.tekst_label1, index=(cyfra, 1): self.edytuj_tekst(event, textvar, index))

        # Label 2
        self.label2 = tk.Label(root, text="Pora dnia:")
        self.label2.grid(row=1, column=0, sticky=tk.E)

        self.tekst_label2 = tk.StringVar()
        self.tekst_label2.set(self.wczytaj_dane("info.txt", cyfra, 2))

        self.label2_tekst = tk.Label(root, textvariable=self.tekst_label2)
        self.label2_tekst.grid(row=1, column=1, sticky=tk.W)
        self.label2_tekst.bind("<Double-Button-1>", lambda event, textvar=self.tekst_label2, index=(cyfra, 2): self.edytuj_tekst(event, textvar, index))

        # Label 3
        self.label3 = tk.Label(root, text="Miejsce:")
        self.label3.grid(row=2, column=0, sticky=tk.E)

        self.tekst_label3 = tk.StringVar()
        self.tekst_label3.set(self.wczytaj_dane("info.txt", cyfra, 3))

        self.label3_tekst = tk.Label(root, textvariable=self.tekst_label3)
        self.label3_tekst.grid(row=2, column=1, sticky=tk.W)
        self.label3_tekst.bind("<Double-Button-1>", lambda event, textvar=self.tekst_label3, index=(cyfra, 3): self.edytuj_tekst(event, textvar, index))

        # Label 4
        self.label4 = tk.Label(root, text="Osoby:")
        self.label4.grid(row=3, column=0, sticky=tk.E)

        self.tekst_label4 = tk.StringVar()
        self.tekst_label4.set(self.wczytaj_dane("info.txt", cyfra, 4))

        self.label4_tekst = tk.Label(root, textvariable=self.tekst_label4)
        self.label4_tekst.grid(row=3, column=1, sticky=tk.W)
        self.label4_tekst.bind("<Double-Button-1>", lambda event, textvar=self.tekst_label4, index=(cyfra, 4): self.edytuj_tekst(event, textvar, index))

        # Label 5
        self.label5 = tk.Label(root, text="Wydarzenia:")
        self.label5.grid(row=4, column=0, sticky=tk.E)

        self.tekst_label5 = tk.StringVar()
        self.tekst_label5.set(self.wczytaj_dane("info.txt", cyfra, 5))

        self.label5_tekst = tk.Label(root, textvariable=self.tekst_label5)
        self.label5_tekst.grid(row=4, column=1, sticky=tk.W)
        self.label5_tekst.bind("<Double-Button-1>", lambda event, textvar=self.tekst_label5, index=(cyfra, 5): self.edytuj_tekst(event, textvar, index))

        # Dodajemy obsługę zdarzeń najechania i opuszczania myszką dla każdego labela
        self.label1_tekst.bind("<Enter>", self.zmien_kolor_kursora)
        self.label1_tekst.bind("<Leave>", self.przywroc_kolor_kursora)

        self.label2_tekst.bind("<Enter>", self.zmien_kolor_kursora)
        self.label2_tekst.bind("<Leave>", self.przywroc_kolor_kursora)

        self.label3_tekst.bind("<Enter>", self.zmien_kolor_kursora)
        self.label3_tekst.bind("<Leave>", self.przywroc_kolor_kursora)

        self.label4_tekst.bind("<Enter>", self.zmien_kolor_kursora)
        self.label4_tekst.bind("<Leave>", self.przywroc_kolor_kursora)

        self.label5_tekst.bind("<Enter>", self.zmien_kolor_kursora)
        self.label5_tekst.bind("<Leave>", self.przywroc_kolor_kursora)

    def edytuj_tekst(self, event, textvar, index):
        nowy_tekst = simpledialog.askstring("Edytuj tekst", "Wprowadź nowy tekst:")
        if nowy_tekst is not None:
            textvar.set(nowy_tekst)
            self.zapisz_dane("info.txt", index[0], index[1], nowy_tekst)

    def wczytaj_dane(self, filename, index, subindex=None):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(';')
                    if len(parts) == 2 and int(parts[0]) == index:
                        return parts[1]
                    elif subindex is not None and len(parts) == 3 and int(parts[0]) == index and int(parts[1]) == subindex:
                        return parts[2]
                    elif subindex is not None and subindex == 5 and len(parts) == 4 and int(parts[0]) == index:
                        return parts[3]  # Nowy label "Wydarzenia"
        except FileNotFoundError:
            return "Przykładowy tekst"

    def zapisz_dane(self, filename, index, subindex, data):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        with open(filename, 'w', encoding='utf-8') as file:
            found = False
            for line in lines:
                parts = line.strip().split(';')
                if subindex is not None and len(parts) == 3 and int(parts[0]) == index and int(parts[1]) == subindex:
                    file.write(f"{index};{subindex};{data}\n")
                    found = True
                elif subindex is not None and subindex == 5 and len(parts) == 4 and int(parts[0]) == index:
                    file.write(f"{index};;{data}\n")  # Nowy label "Wydarzenia"
                    found = True
                else:
                    file.write(line)

            if not found:
                file.write(f"{index};{subindex};{data}\n")

    def zmien_kolor_kursora(self, event):
        event.widget.config(fg="red")  # Zmiana koloru tekstu na czerwony
        self.root.config(cursor="arrow")  # Zmiana kształtu kursora na linię
        # Dla pionowej kreski należy wpisać "xterm"

    def przywroc_kolor_kursora(self, event):
        event.widget.config(fg="black")  # Przywrócenie koloru tekstu na czarny
        self.root.config(cursor="")  # Przywrócenie domyślnego kształtu kursora


class LiniaCzasuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linia Czasu")

        # Dodajemy Canvas do okna
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Inicjalizujemy listę przechowującą kropki
        self.kropki = []

        # Inicjalizujemy zmienne do przechowywania informacji o aktualnie przesuwanej kropce
        self.aktualnie_przesuwana_kropka = None
        self.pozycja_przesuwanej_kropki = None

        # Rysujemy linię czasu
        self.rysuj_linie_czasu()

        # Przypisujemy funkcję do zdarzenia zmiany rozmiaru okna
        self.root.bind("<Configure>", self.rysuj_linie_czasu)

        # Przypisujemy funkcję do zdarzenia kliknięcia lewym przyciskiem myszy
        self.canvas.bind("<Button-1>", self.zacznij_przesuwanie_kropki)

        # Przypisujemy funkcję do zdarzenia przesuwania myszy przy naciśniętym lewym przycisku
        self.canvas.bind("<B1-Motion>", self.przesuwaj_kropke)

        # Przypisujemy funkcję do zdarzenia zwolnienia lewego przycisku myszy
        self.canvas.bind("<ButtonRelease-1>", self.zakoncz_przesuwanie_kropki)

        # Przypisujemy funkcję do zdarzenia kliknięcia prawym przyciskiem myszy
        self.canvas.bind("<Button-3>", self.usun_kropke)

        # Przypisujemy funkcję do zdarzenia kliknięcia prawym przyciskiem myszy
        self.canvas.bind("<Button-2>", self.dodaj_kropke)

        # Przypisujemy funkcję do zdarzenia kliknięcia podwójnego lewego przycisku myszy
        self.canvas.bind("<Double-Button-1>", self.wyswietl_okno_z_labelami)

        # Lista przechowująca obiekty OknoZLabelami
        self.okna_labeli = []

        # Wczytujemy dane z pliku
        self.wczytaj_dane()
        self.wczytaj_kolory()  # Dodane wywołanie wczytywania kolorów

        # Dodajemy bind do zdarzenia najechania myszką i opuszczania myszki dla każdej kropki
        for kropka_id, _ in self.kropki:
            self.canvas.tag_bind(kropka_id, "<Enter>", self.zmien_kursor_na_kolko)
            self.canvas.tag_bind(kropka_id, "<Leave>", self.przywroc_kursor)

    def zmien_kursor_na_kolko(self, event):
        self.root.config(cursor="circle")

    def przywroc_kursor(self, event):
        self.root.config(cursor="")

    def wybierz_kolor_kropki(self, event):
        x_klik = event.x
        y_klik = event.y

        for kropka_id, _ in self.kropki:
            x_kropki, y_kropki, _, _ = self.canvas.coords(kropka_id)
            if x_kropki - 3 <= x_klik <= x_kropki + 10 and y_kropki - 3 <= y_klik <= y_kropki + 10:
                color = colorchooser.askcolor(title="Wybierz kolor kropki")[1]
                if color:
                    self.canvas.itemconfig(kropka_id, fill=color)
                    # Zapisz informacje o kolorze do pliku colors.txt
                    self.zapisz_kolor_do_pliku(kropka_id, color)
                break

    def zapisz_kolor_do_pliku(self, kropka_id, color):
        numer_kropki = self.pobierz_cyfre_dla_kropki(kropka_id)

        try:
            with open("colors.txt", "r") as plik:
                lines = plik.readlines()
        except FileNotFoundError:
            with open("colors.txt", "w"):  # Tworzymy plik, jeśli nie istnieje
                pass
            lines = []

        with open("colors.txt", "w") as plik:
            updated = False
            for line in lines:
                parts = line.strip().split(';')
                if len(parts) == 2 and int(parts[0]) == numer_kropki:
                    plik.write(f"{numer_kropki};{color}\n")
                    updated = True
                else:
                    plik.write(line)

            if not updated:
                plik.write(f"{numer_kropki};{color}\n")

    def rysuj_linie_czasu(self, event=None):
        # Pobieramy aktualny rozmiar okna
        szerokosc_okna = self.root.winfo_width()
        wysokosc_okna = self.root.winfo_height()

        # Przypisujemy funkcję do zdarzenia przewijania kółkiem myszy
        self.canvas.bind("<Button-5>", self.wybierz_kolor_kropki)  # Zmiana zdarzenia

        # Współrzędne początkowe i końcowe linii czasu
        procent_y = 85
        x_poczatek = 10
        y_poczatek = (wysokosc_okna * procent_y) / 100
        x_koniec = szerokosc_okna - 10
        y_koniec = y_poczatek

        # Usuwamy poprzednie rysunki
        self.canvas.delete("linia_czasu")
        self.canvas.delete("etykiety_kropek")

        # Rysujemy linię czasu
        self.canvas.create_line(x_poczatek, y_poczatek, x_koniec, y_koniec, width=4, fill="blue", tags="linia_czasu")

        # Aktualizujemy położenie kropek
        if self.kropki:
            odleglosc_miedzy_kropkami = (x_koniec - x_poczatek) / (len(self.kropki) + 1)
            for i, (kropka_id, cyfra) in enumerate(self.kropki):
                x_kropki = x_poczatek + odleglosc_miedzy_kropkami * (i + 1)
                _, y_linii, _, _ = self.canvas.coords("linia_czasu")

                # Rozmiar kropek ----------------------------------------------------------------------------
                self.canvas.coords(kropka_id, x_kropki - 5, y_linii - 5, x_kropki + 5, y_linii + 5)
                # Dodajemy etykietę z numerem kropki i cyfrą
                etykieta_id = self.canvas.create_text(x_kropki, y_linii + 15, text=f"{cyfra}", tags="etykiety_kropek")
                # Podnosimy kropkę do warstwy wyżej
                self.canvas.tag_raise(kropka_id)

    def wyswietl_okno_z_labelami(self, event):
        x_klik = event.x
        y_klik = event.y

        for kropka_id, cyfra in self.kropki:
            x_kropki, y_kropki, _, _ = self.canvas.coords(kropka_id)
            if x_kropki - 3 <= x_klik <= x_kropki + 10 and y_kropki - 3 <= y_klik <= y_kropki + 10:
                # Tworzymy nowe okno z labelami
                okno_labeli = tk.Toplevel(self.root)

                # Ustawiamy rozmiar okna z labelami (np. 300x200)
                okno_labeli.geometry("400x110")

                # Tworzymy obiekt klasy OknoZLabelami i przekazujemy mu okno_labeli oraz cyfrę
                okno_z_labelami = OknoZLabelami(okno_labeli, cyfra)

                # Ustawiamy kolor tekstu labeli
                okno_z_labelami.label1.config(fg="green")
                okno_z_labelami.label2.config(fg="blue")
                okno_z_labelami.label3.config(fg="orange")
                okno_z_labelami.label4.config(fg="red")
                okno_z_labelami.label5.config(fg="magenta")

                # Przekazujemy dane z kropki do obiektu OknoZLabelami
                okno_z_labelami.label1_tekst.set(cyfra)

                # Dodajemy obiekt OknoZLabelami do listy
                self.okna_labeli.append(okno_z_labelami)

                break


    def zacznij_przesuwanie_kropki(self, event):
        # Pobieramy współrzędne kliknięcia
        x_klik = event.x
        y_klik = event.y

        # Sprawdzamy, czy kliknięcie było na którejś z kropek
        for kropka_id, _ in self.kropki:
            x_kropki, y_kropki, _, _ = self.canvas.coords(kropka_id)
            if x_kropki - 3 <= x_klik <= x_kropki + 10 and y_kropki - 3 <= y_klik <= y_kropki + 10:
                # Ustawiamy aktualnie przesuwana kropkę i jej początkową pozycję
                self.aktualnie_przesuwana_kropka = kropka_id
                self.pozycja_przesuwanej_kropki = (x_kropki, y_kropki)
                break

    def przesuwaj_kropke(self, event):
        if self.aktualnie_przesuwana_kropka is not None:
            # Pobieramy współrzędne przesunięcia myszy
            x_przesuniecie = event.x - self.pozycja_przesuwanej_kropki[0]
            y_przesuniecie = event.y - self.pozycja_przesuwanej_kropki[1]

            # Przesuwamy kropkę
            self.canvas.move(self.aktualnie_przesuwana_kropka, x_przesuniecie, y_przesuniecie)

            # Aktualizujemy pozycję przesuwanej kropki
            self.pozycja_przesuwanej_kropki = (event.x, event.y)
            

    def zakoncz_przesuwanie_kropki(self, event):
        if self.aktualnie_przesuwana_kropka is not None:
            # Pobieramy aktualne współrzędne przesuniętej kropki
            x_przesunieta, y_przesunieta, _, _ = self.canvas.coords(self.aktualnie_przesuwana_kropka)

            # Znajdujemy indeks przesuwanej kropki w liście
            indeks_kropki = next((i for i, (kropka_id, _) in enumerate(self.kropki) if kropka_id == self.aktualnie_przesuwana_kropka), None)

            if indeks_kropki is not None:
                # Aktualizujemy pozycję przesuniętej kropki w liście
                self.kropki[indeks_kropki] = (self.aktualnie_przesuwana_kropka, self.kropki[indeks_kropki][1])

                # Sortujemy kropki względem współrzędnej x
                self.kropki.sort(key=lambda kropka: self.canvas.coords(kropka[0])[0])

                # Zapisujemy dane do pliku
                self.zapisz_dane()

            # Resetujemy zmienne
            self.aktualnie_przesuwana_kropka = None
            self.pozycja_przesuwanej_kropki = None

            # Aktualizujemy odległości między kropkami
            self.rysuj_linie_czasu()

    

    def dodaj_kropke(self, event):
        # Pobieramy współrzędne kliknięcia
        x_klik = event.x
        y_klik = event.y

        # Pobieramy współrzędne linii czasu
        _, y_linii, _, _ = self.canvas.coords("linia_czasu")

        # Sprawdzamy, czy kliknięcie było na linii czasu i czy nie jest zbyt blisko krawędzi
        if 10 < x_klik < self.root.winfo_width() - 10 and abs(y_klik - y_linii) < 5:
            # Wyświetlamy okno dialogowe do wprowadzenia cyfry
            cyfra = simpledialog.askinteger("Cyfra", "Wprowadź cyfrę dla kropki:")
            if cyfra is not None:
                # Dodajemy kropkę na linii
                kropka_id = self.canvas.create_oval(x_klik - 3, y_linii - 3, x_klik + 3, y_linii + 3, fill="red")
                self.kropki.append((kropka_id, cyfra))
                # Sortujemy kropki względem współrzędnej x
                self.kropki.sort(key=lambda kropka: self.canvas.coords(kropka[0])[0])
                # Zapisujemy dane do pliku
                self.zapisz_dane()
                # Aktualizujemy odległości między kropkami
                self.rysuj_linie_czasu()

    def pobierz_cyfre_dla_kropki(self, kropka_id):
        for kropka in self.kropki:
            if kropka[0] == kropka_id:
                return kropka[1]
        return None

    def usun_kropke(self, event):
        x_klik = event.x
        y_klik = event.y

        for kropka_id, _ in self.kropki:
            x_kropki, y_kropki, _, _ = self.canvas.coords(kropka_id)
            if x_kropki - 3 <= x_klik <= x_kropki + 10 and y_kropki - 3 <= y_klik <= y_kropki + 10:
                cyfra = self.pobierz_cyfre_dla_kropki(kropka_id)
                self.usun_info_z_pliku("info.txt", cyfra)
                self.usun_kolor_z_pliku("colors.txt", cyfra)  # Dodane usunięcie koloru z pliku
                self.canvas.delete(kropka_id)
                self.kropki = [(k, c) for k, c in self.kropki if k != kropka_id]
                self.canvas.delete("etykiety_kropek")
                self.zapisz_dane()
                self.rysuj_linie_czasu()
                break

    def usun_kolor_z_pliku(self, filename, numer_kropki):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return

        with open(filename, 'w') as file:
            for line in lines:
                parts = line.strip().split(';')
                if len(parts) == 2 and int(parts[0]) == numer_kropki:
                    continue
                elif len(parts) == 3 and int(parts[0]) == numer_kropki:
                    continue
                file.write(line)

    def usun_info_z_pliku(self, filename, numer_kropki):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return

        with open(filename, 'w') as file:
            for line in lines:
                parts = line.strip().split(';')
                if len(parts) == 2 and int(parts[0]) == numer_kropki:
                    continue
                elif len(parts) == 3 and int(parts[0]) == numer_kropki:
                    continue
                file.write(line)

    def zapisz_dane(self):
        # Dodajemy bind do zdarzenia najechania myszką i opuszczania myszki dla każdej kropki
        for kropka_id, _ in self.kropki:
            self.canvas.tag_bind(kropka_id, "<Enter>", self.zmien_kursor_na_kolko)
            self.canvas.tag_bind(kropka_id, "<Leave>", self.przywroc_kursor)
            
        with open("dane.txt", "w") as plik:
            for kropka_id, cyfra in self.kropki:
                x, y, _, _ = self.canvas.coords(kropka_id)
                plik.write(f"{x};{y};{cyfra}\n")

    def wczytaj_dane(self):
        try:
            with open("dane.txt", "r") as plik:
                for linia in plik:
                    x, y, cyfra = map(float, linia.strip().split(';'))
                    kropka_id = self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")
                    self.kropki.append((kropka_id, int(cyfra)))
        except FileNotFoundError:
            pass

    def wczytaj_kolory(self):
        try:
            with open("colors.txt", "r") as plik:
                for linia in plik:
                    numer_kropki, color = linia.strip().split(';')
                    numer_kropki = int(numer_kropki)
                    for kropka_id, cyfra in self.kropki:
                        if cyfra == numer_kropki:
                            self.canvas.itemconfig(kropka_id, fill=color)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LiniaCzasuApp(root)
    root.mainloop()
