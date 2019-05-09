# docker
docker with django 


1. 이미지 생성  
$ docker build . -t myapp
2. 컨테이너 생성 및 실행   
$ docker run -it --name myapp2 -p 4000:80 myapp
3. 브라우저에서 실행   
http://192.168.99.100:4000/
