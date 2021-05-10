1. Piszemy plik Dockerfile oraz przeklejamy requirements.txt

2. Budujemy obraz
docker build -t sql_app .

3. Tworzymy dockerowy network 
docker network create some-net

4. Uruchamiamy kontener Postgresa (gdy nie mamy loklanie to zostanie pobrany automatycznie z docker hub)
Gdzie 
    -e, oznacza podanie zmiennych środowiskowych do kontenera. W naszym przypadku ustawimy dzięki nim użytkownika, hasło i bazę danych
    --network, oznacza wpięcie kontenera w wybrany network, w tym przypadku wcześniej utworzony some-net
    --name, nazwa kontenera, który zostanie stworzony (brak tego argumentu wygenerowałby by losową nazwę)
  
docker run --name some-postgres -e POSTGRES_PASSWORD=abc123 -e POSTGRES_USER=user -e POSTGRES_DB=db1 -d --network some-net --publish 5432:5432 postgres

5. docker run --name sql_app -p 5000:5000 --network some-net sql_app
6. Wejść na stronę http://0.0.0.0:5000/ na loklanym komputerze (można odświeżyć kilka razy)
7. Sprawdzić czy na stronie http://0.0.0.0:5000/results pojawiły się wyniki (są to timestampy wejścia na stronę główną - tak działa ta prosta apka flaskowa, 
odkładająca rejestr wejść w bazie danych)
