

<iframe width="560" height="515" src="https://www.youtube.com/embed/IQo5p8-73ZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# **Demo - pierwszy obraz docker**

### Organizacja

- [ ] Załóż konto na Docker
- [ ] Zaloguj się w Docker Hub, i stwórz pierwsze repozytorium
- [ ] Zainstaluj aplikację Docker

### Obraz

- [ ] Załóż folder, i stwórz w nim prostą aplikację

- [ ] Stwórz plik Dockerfile, na wzór:
  <img src="media//image-20220517102935475.png" alt="image-20220517102935475" style="zoom:25%;" />

- [ ] Stwórz obraz docker nadając mu nazwę (flaga --tag) *pierwsza_aplikacja*:

  `$ docker build --tag pierwsza_aplikacja .`

- [ ] Uruchom obraz o nazwie *pierwsza_aplikacja* lokalnie:

  `$ docker run pierwsza_aplikacja`

### Udostępnienie

- [ ] Zmień nazwę obrazu tak, by móc go opublikować swoim repozytorium Docker Hub:

  `$ docker build -t andrzejwodecki/ml_tests:pierwsza_aplikacja .`

- [ ] Opublikuj obraz w swoim repozytorium Docker Hub:

  `$ docker push -t andrzejwodecki/ml_tests:pierwsza_aplikacja`

- [ ] Uruchom obraz na innym systemie:

  - [ ] zainstaluj na nim Docker'a

  - [ ] uruchom kontener:

    `$ docker run -t andrzejwodecki/ml_tests:pierwsza_aplikacja`



# Przydatne źródła

Najlepszym znanym mi źródłem wiedzy nt systemu Docker jest oficjalny kurs dostępny na stronie:

https://docs.docker.com/get-started/