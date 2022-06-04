# Uruchomienie z podłączeniem lokalnego systemu plików

Bardzo często istnieje potrzeba synchronizacji lokalnego systemu plików z kontenerem tak, by można było zmieniać dane źródłowe bez konieczności przebudowy obrazu. Przykładowo, chcemy mieć możliwość modyfikacji plików z danymi, zmiany skryptów python, czy też podglądu pod wyniki uruchomień kontenerów w lokalnym systemie.

Powyższe scenariusze mogą być zrealizowane z wykorzystaniem mechanizm **bind mount**.

## Synchronizacja folderu host'a z kontenerem

Aby stworzyć obraz, w folderze z plikiem Dockerfile uruchom w terminalu komendę:

`docker build -t bind_app1_app2:v3 . `

Po zbudowaniu obrazu,  uruchom odpowiedni kontener podłączając lokalny wolumin:

`docker run -ti -v"$(pwd):/app" bind_app1_app2:v3 python3 run.py `

Zauważ, że: 

1. tym razem pliki wygenerowane w ramach kontenera synchronizują się z Twoim folderem lokalnym. W szczególności, w folderach `app_1/input` i `app_1/output` pojawiły się nowe pliki
2. konieczne jest jednak uruchamianie kontenera w folderze, który zawiera niezbędne pliki. Opcja `-v"$(pwd):/app"` usuwa pliki z katalogu `\app` kontenera
3. jeśli chcesz uruchomić kontener w miejscu, w którym nie ma odpowiednich plików, uruchom go bez opcji bind mount: `docker run -ti bind_app1_app2:v3 python3 run.py`
   

## Modyfikacja pliku w folderze lokalnym

Sprawdźmy teraz, czy ta synchronizacja działa w obie strony. W tym celu zmodyfikuj skrypt `run.py` dodając do niego wydruk `cześć stary...`

Jak widać, modyfikacja pliku lokalnego jest uwzględniana przez kontener bez konieczności przebudowania obrazu.

## Scenariusze użycia

Wyżej wymieniony mechanizm możesz w szczególności zastosować w następujących sytuacjach:

### Organizacja

**Chcę kontynuować pracę nad moim projektem na innym komputerze**

Często zmieniam lokalizację: podróżuję, wracam do domu, etc. Chciałbym móc wykonywać obliczenia, trenować modele lub testować aplikację na komputerach, do których mam dostęp. Różnią się one nie tylko systemami operacyjnymi, ale też zainstalowanymi na nich środowiskami oraz konfiguracją sprzętową. W szczególności, część z nich nie może korzystać z akceleratorów takich jak karty graficzne.

Zamiast na każdym z nich instalować dedykowane środowiska, uruchamiam kontener docker z różnymi parametrami (np. z lub bez akceleracji GPU).

### Wytwarzanie

**Chcę zademonstrować innym członkom zespołu aplikację wykorzystującą uczenie maszynowe** 

...ale tak, by w razie potrzeby mogli sami eksperymentować z odpowiednimi komponentami.
(np. zmieniać dane, algorytmy trenowania, aplikację końcową, etc.).

Udostępniam im obraz docker z odpowiednim środowiskiem oraz kompletem kodów źródłowych.

### Udostępnianie

**Chcę przeprowadzić szkolenie z zakresu Data Science**

Chcę pokazać komuś rozwiązanie w jupyter notebook, wykorzystujące różne biblioteki (np. PyCaret). Użytkownicy nie mają zainstalowanych żadnych środowisk.

Proszę ich o instalację Docker, a potem uruchomienie mojego kontenera.

### Produkcja

**Chcę przekazywać do kontenera dane specyficzne dla danego hosta (np. jako parametry uruchomieniowy)**

Wykorzystuję w tym celu docker bind mount.

**Chcę zasymulować środowisko produkcyjne**

Nasz system analizy obrazu uruchamiany jest na urządzeniu końcowym typu NVidia Jetson Nano. Na swojej stacji roboczej chcę zasymulować, jak zachowa się na tym urządzeniu najnowsza wersja mojego modelu.

W tym celu uruchamiam kontener Docker z obrazem urządzenia końcowego.

## Przydatne źródła

Bardzo dobrą prezentację metod *bind mount* i *volume mount* znajdziesz w oficjalnej dokumentacji docker dostępnej [tutaj](https://docs.docker.com/storage/).