#Project for NA course in UMKC
####This project handles cache in proxyServer which can track clients acitivity with time

#####Requirements
* python 2.7 or higher version
* django==1.7

##Steps to run this project
* Clone this project folder to your pc.
* Open this project root folder in command promt
* If you want to use virtual environment do this step: run the following script to activate virtual environment
```
.\Scripts\activate
```
* Next navigate to proxyServer folder
```
cd proxyServer
```
* Do migration
 ```
python manage.py migrate
```
* Delete old Database - when you run this commnad it ask for yes or no. Enter yes
```
python manage.py flush
```
* Initialize Database - when you run this command it ask for username and password. give your own
```
python manage.py syncdb
```
* run server 
```
python manage.py runserver
```
