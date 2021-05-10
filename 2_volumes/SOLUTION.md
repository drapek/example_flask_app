1. Piszemy pliki Dockerfile dla każdego modułu oraz przeklejamy do niego requirements.txt

2. budujemy obrazy
cd dir_viewer
docker build -t dir_viewer .

cd uploader
docker build -t uploader .

3. Tworzymy nowy dockerowy volumin
docker volume create upload_shared

4. Uruchamiamy kontenery z voluminami
gdzie, 
    -p oznacza udostępniane porty na zewnątrz kontenera
    -v oznacza podpięce volumnu do kontenera, ma formę typu <nazwa>:</ścieżka docelowa na kontenerze>
    
docker run --name uploader -p 5000:5000 -v upload_shared:/var/files uploader
docker run --name dir_viewer -p 7000:7000 -v upload_shared:/opt/shared/server_files dir_viewer
