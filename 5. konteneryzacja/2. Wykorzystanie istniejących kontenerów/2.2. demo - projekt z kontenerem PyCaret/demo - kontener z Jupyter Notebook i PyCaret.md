# Demo: kontener ze środowiskiem PyCaret

<iframe width="560" height="315" src="https://www.youtube.com/embed/kGu5MS1e0Xs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



*Uwaga: komplet wersji demonstracyjnych, ćwiczeń i rozwiązań oraz rekomendacje dotyczące środowiska uruchomieniowego znajdziesz tutaj:*

https://github.com/wodecki/ASI_2022

## Cel

Naszym celem jest uruchomienie kontenera docker umożliwiającego realizację prostego projektu uczenia maszynowego z wykorzystaniem pakietu PyCaret. Instalacja pakietu na lokalnym systemie wymaga dużej uważności - oficjalny obraz Docker zdecydowanie ułatwia realizację tego zadania.

W tym celu wykorzystamy:

- Oficjalny, "lekki" obraz docker biblioteki Pycaret dostępny [tutaj](https://hub.docker.com/r/pycaret/slim)
- Notatnik z przykładowym projektem `Klasyfikacja binarna - CHURN.ipynb`
- Dane treningowe `customers_churn.csv`



## Lista kontrolna

- [ ] Uruchomiony notatnik Jupyter umożliwiający wczytanie własnego notatnika i aktywację jądra `pycaret`
- [ ] Wczytane pliki:
  - [ ]  `Klasyfikacja binarna - CHURN.ipynb`
  - [ ]  `customers_churn.csv`
- [ ] Zrealizowane z sukcesem komendy z notatnika  `Klasyfikacja binarna - CHURN.ipynb`



## Rozwiązanie

1. Uruchom oficjalny, "lekki" obraz docker biblioteki Pycaret:

`docker run -p 8888:8888 pycaret/slim`

2. Wejdź na wskazany na ekranie adres serwera jupyter (127.0.0.1:8888...)
3. Zaimportuj pliki `Klasyfikacja binarna - CHURN.ipynb` i `customers_churn.csv`  (przycisk  *Upload* w prawym górnym rogu) 
4. Uruchom notatnik  `Klasyfikacja binarna - CHURN.ipynb` i uruchom poszczególne komórki.



## Wskazówki

W sytuacji, gdy uruchomiony Jupyter Notebook wymagać będzie od Ciebie podania hasła (lub tokena), zaś ten wskazany przez Docker nie zadziała, problemem jest najpewniej uruchomiony wcześniej inny serwer Jupyter. Rozwiązanie:

1. sprawdź aktualnie uruchomione serwery Jupyter:

   `jupyter notebook list`

2. Zatrzymaj poprzednio uruchomiony serwer:
   `jupyter notebook stop 8888`

3. Uruchom ponownie obraz.



Niekiedy źródłem problemów mogą być też uruchomione wcześniej, i nadal aktywne kontenery. Aby sprawdzić, które z nich działają, uruchom:
`docker run ps`

Aby usunąć wszystkie uruchomione kontenery (uwaga: to ekstremalne rozwiązanie), uruchom:

`docker container prune`

