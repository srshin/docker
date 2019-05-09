# docker
docker with django 

Docker/django
$ ls  
app.py  db.sqlite3   Dockerfile  manage.py*  mysite/  requirements.txt
1. 이미지 생성    
$ docker build . -t django
2. 컨테이너 생성 및 실행    
$ docker run -it --name mydjango1 -p 8000:8000 django
3. 브라우저에서 실행    
http://192.168.99.100:8000/