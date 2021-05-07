# Zadanie

Dla dwóch aplikacji 'dir_viewer.py' oraz 'uploader.py' wykonać Dockerfile'y, a następnie uruchomić je tak, aby
współdzieliły volumin, do którego zapisywane są pliki. 

Aplikacja uploader.py zapisuje pliki do /var/files

Aplikacja dir_viewer.py listuje pliki z katalogu /opt/shared/server_files

Należy więc podpiąć tak volumin, aby w obu przypadkach był wpięty ten
sam volumin, a załadowane pliki przez uploader.py były widoczne w aplikacji
dir_viewer.py
