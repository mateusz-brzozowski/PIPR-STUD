Slam tracker
=================

Program za pomocą wykresu przedstawia przedmeczowe statystyki zawodników tenisowych.

Schemat Kodu
------------

- `data/`: Pliki CSV z danymi
- `src/`: Kod źródłowy
    - `database.py`: Moduł bazy danych
    - `gui.py`: Moduł interfejsu gradicznego
    - `main.py`: Moduł uruchamiający program
    - `plotter.py`: Moduł wykresu
- `docs`: Dokumenty
    - `Slam tracker.docx`: Dokumentacja programu w pliku word.
    - `documentation.txt`: Dokumentacja programu w pliku tekstowym.


Dokumentacja
------------

Link: <https://gitlab-stud.elka.pw.edu.pl/mbrzozow/slam-tracker/-/blob/master/docs/Slam%20tracker.docx>.

Sposób korzystania z programu
------------
1.	Wybierz pierwszego zawodnika
2.	Wybierz drugiego zawodnika
3.	Wybierz turniej
4.	Wybierz parametry, które chcesz przedstawić na wykresie
5.	Opcjonalnie zaznacz „Najlepsze rekordy”
6.	Opcjonalnie wybierz zakres dat
7.	Naciśnij „Wygeneruj wykres”
8.	Na ekranie powinien ukazać się wykres danych

Biblioteki
------------
`pandas`, `numpy`, `matplotlib`, `PySide2`, `io`, `sys`
