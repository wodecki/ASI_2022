# README

W tym prostym ćwiczeniu stworzysz i uruchomisz lokalnie prosty proces trenowania i ewaluacji modelu.

Aby stworzyć obraz, w linii komend wpisz:

`docker build --tag train_eval .`

Aby uruchomić kontener, w linii komend wpisz:

`docker run -ti train_eval`

Zauważ, że w tym podejściu:

1. kontener automatycznie uruchamia skrypt `run.py` (zgodnie z ostatnią instrukcją w pliku `Dockerfile`)
2. jest zarzymywany bezpośrednio po ukończeniu jego realizacji (możesz to sprawdź uruchamiają w linii komend polecenie `docker ps`)
3. wszystkie pliki niezbędne do uruchomienia (komponenty i artefakty) są przechowywane w kontenerze
4. użytkownik nie ma do nich dostępu, w szczególności nie może ich modyfikować.



