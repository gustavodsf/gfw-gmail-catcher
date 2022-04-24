@ECHO OFF

ECHO Criando a imagem do aplicativo para o Docker
docker-compose build

Echo Colocando a imagem para rodar
docker-compose  -d

PAUSE
