## DOCKER 사용방법
* HOST OS : windows 10 home
* Docker : dockertoolbox
* volume 설정 사용: default는 c:/Users만 공유되므로 다른 폴더를 공유하기 위해서는 virtualbxo에서 공유폴더 설정한뒤 docker-machine restart. 
### ubuntu
* image : ubuntu, my_ubuntu  
1. Dockerfile 생성  
2. 이미지 생성  
$ docker build . -t my_ubuntu
3. 컨테이너 만들기    
3.1 port 설정 / volume mount (volumn은 반드시 c:/Users아래 있어야 함.)    
```
$ docker run -dit --name my_ubuntu1  -p 3000:3000 -v /c/Users/src:/src my_ubuntu    
```

$ docker container ps    
```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
1bec59f746c5        my_ubuntu           "/bin/bash"         16 seconds ago      Up 10 seconds       0.0.0.0:3000->3000/tcp   my_ubuntu1
```
3.2  접속및 mounting확인   
```
$ docker exec -it my_ubuntu1 bash
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

### django_mysql
* image : mysql:5.7, django_mysql   
1. windows환경변수에 path에 추가   
C:\Program Files\MySQL\MySQL Server 8.0\bin   
2. mysql 이미지 pull  
$ docker pull mysql:5.7   
3. mysql 실행   
$ docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=djangodocker_db mysql:5.7  
4. mysql 접속/databse생성    
$ mysql -h127.0.0.1 -proot -uroot  
mysql> show DATABASES;  
5. local에서 docker database update  (local database service는 꺼야 함.)
$ python manage.py migrate
6. local에서 동작 확인  
$ python manage.py runserver  
http://127.0.0.1:8000/   
7. mysql이 떠 있는 상태인지 먼저 확인
$ docker ps   
* TIP: mysql 에 data를 update하였으므로 종료된 상태인 경우에 start해야 함.   
* run하면 컨테이너가 새로 생성되므로 이전 저장한 데이타 사용 불가   
$ docker start [container name]   
8. 이미지 생성 & 컨테이너 실행    
$ docker-compose up  
9. 브라우저에서 실행  
http://192.168.99.100:8000/

### django_compose
* image : django_compose
1. 이미지 생성 & 컨테이너 실행  
$docker-compose up   
2. 브라우저에서 실행  
http://192.168.99.100:8000/

### django_mysql_compose
1. 이미지 build   
$ docker-compose build
2. 컨테이너 실행  
$ docker-compose up
* database보다 django가 먼저 실행되는 경우 중간에 에러가 날 수 있음. 이때 docker-compose up을 한번 더 하면 됨. 

### django_postgress_compose
1. 이미지 build   
$ docker-compose build
2. 컨테이너 실행   
$ docker-compose up
* database보다 django가 먼저 실행되는 경우 중간에 에러가 날 수 있음. 이때 docker-compose up을 한번 더 하면 됨. 

### django_postgress_compose_volume
* 데이타베이스와 코드가 모두 초기화되어있으므로 compose-up만하면됨. 코드 수정시 실시간 반영됨. 
0. volume에 들어갈 데이터 초기화  
```
$ docker-compose run web django-admin startproject composeexample .
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py createsuperuser
```
1. docker-compose 수정  
이미지와 데이터베이스가 각각 volume으로 마운트되도록 수정 
```
  db:
    volumes:
      - /d/program/git/Docker/django_mysql_compose_volume/mysql:/var/lib/mysql
  web:
    volumes:
      - /d/program/git/Docker/django_mysql_compose_volume:/code
```
2. 이미지 build   
$ docker-compose build
3. 컨테이너 실행   
$ docker-compose up
4. 컨테이너 삭제
$ docker-compose down 

