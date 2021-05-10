1. budujemy obrazy
cd dir_viewer
docker build -t dir_viewer .

cd uploader
docker build -t uploader .

2. Uruchamiamy kontenery z voluminami
docker run --name uploader -p 5000:5000 -v upload_shared:/var/files uploader
docker run --name dir_viewer -p 7000:7000 -v upload_shared:/opt/shared/server_files dir_viewer
