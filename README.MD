# Django Poke Api

to run  the image follow the next instructions, just for local environment

## Create Environment file

    cp env_template .env

## build image

    docker-compose build

## up image

    docker-compose up 

## if you don't wanna see the logs of the containers, add -d after up

    docker-compose up -d


## give permissions for this files collectstatic.sh, migrate.sh, run_script.sh and setup.sh 

    chmod +x poke.sh && chmod +x poke_all.sh && chmod +x setup.sh && chmod +x test.sh 

## to setup the project, create database, make initial migrations, create superuser and fill the database just run

    ./setup.sh


## if everything works fine you should see something like this

![enter image description here](https://i.imgur.com/0YxHye9.png)

## Pycharm Support
first, we need to setup the common stuff to active the autocomplete adding the Django Support choosing the manage.py and settings.py files location.

![enter image description here](https://i.imgur.com/yxaLtUc.png)

now we need add the python interpreter what live inside the docker container to the project

Go to preferences and to click in Interpreter then in Project Interpreter and press add

![enter image description here](https://i.imgur.com/DwKsssx.png)

now, do click in Docker, select the image what contains the project name, then write python3 and press ok

![enter image description here](https://i.imgur.com/pI86DZb.png)

press apply and ok, done!.

![enter image description here](https://i.imgur.com/lmpULSQ.png)

now we have configured the interpreter what lives inside our Docker Container in our project

Please, DON'T UPDATE THE DEPENDENCIES ! **unless necessary**

if you wanna deploy this project in production, [go to here](https://gist.github.com/osw4l/cbfbfb3f7a7f42ab31fa5083b358f316)


**Thanks for using my project, if you need something else, feel you free to contact me**
**me@osw4l.com**
