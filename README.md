# DOCKER 사용방법
## HOST OS : windows 10 home
## Docker : dockertoolbox
### ubuntu
* image : my_ubuntu  
1. Dockerfile 생성  
2. 이미지 생성  
$ docker build . -t my_ubuntu

3. 컨테이너 만들기    
3.1 port 설정 / volume mount (volumn은 반드시 c:/Users아래 있어야 함.)    
`$ docker run -dit --name my_ubuntu1  -p 3000:3000 -v /c/Users/src:/src my_ubuntu    `

$ docker container ps    
```CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
1bec59f746c5        my_ubuntu           "/bin/bash"         16 seconds ago      Up 10 seconds       0.0.0.0:3000->3000/tcp   my_ubuntu1
```
3.2  접속및 mounting확인   
```$ docker exec -it my_ubuntu1 bash
root@216beee81140:/# cd /src
root@216beee81140:/src# ls
Dockerfile
```
### python
* image :myapp, python
1. 이미지 생성  
$ docker build . -t myapp  
2. 컨테이너 생성 및 실행  
$ docker run -it --name myapp2 -p 4000:80 myapp  
3. 브라우저에서 실행  
http://192.168.99.100:4000/  

### django
* image :django
1. 이미지 생성  
$ docker build . -t django  
2. 컨테이너 생성 및 실행  
$ docker run -it --name mydjango1 -p 8000:8000 django  
3. 브라우저에서 실행  
http://192.168.99.100:8000/  
4. docker-machin ip 확인
$ docker-machine ip  
192.168.99.100

### django_compose
* image : django_compose
1.  컨테이너 실행  
$docker-compose up   
2. 브라우저에서 실행  
http://192.168.99.100:8000/

### django_mysql
* image : mysql:5.7, django_mysql  
1. windows환경변수에 path에 추가  
C:\Program Files\MySQL\MySQL Server 8.0\bin  
2. mysql 이미지 pull  
$ docker pull mysql:5.7  
3. mysql 실행   
$ docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=djangodocker_db mysql:5.7  
4. mysql 접속  
$ mysql -h127.0.0.1 -proot -uroot
mysql> show DATABASES;
5. database update  
$ python manage.py migrate
6. local에서 동작 확인
$ python manage.py runserver
7. 브라우저에서 실행
http://127.0.0.1:8000/
8. mysql이 떠 있는 상태인지 먼저 확인 
TIP: mysql 에 data를 update하였으므로 start해야 함. run하면 컨테이너가 새로 생성되므로 이전 저장한 데이타 사용 불가 
$ docker ps
$ docker start [container name] 
9. 컨테이너 실행 
$ docker-compose up
10. 브라우저에서 실행  
http://192.168.99.100:8000/


