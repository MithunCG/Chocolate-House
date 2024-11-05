
# chocolate_house

## Instructions to run
### Follow the below commands to run



```bash  
git clone https://github.com/MithunCG/Chocolate-House.git
```

```bash  
docker-compose build
```

```bash  
docker-compose up
```

open new terminal, leave existing terminal running


```bash  
docker-compose exec web python manage.py makemigration
```

```bash  
docker-compose exec web python manage.py migrate
```

```bash  
docker-compose exec web python manage.py createsuperuser
```

give username, password


Open a browser and go to http://localhost:8000/admin to access admin interface

go to http://localhost:8000/ to access application
