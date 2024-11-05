
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
docker-compose exec web python manage.py makemigrations
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



## Walkthrough of the project


![Home page](images\img-1.png)
![Seasonal Flavours](images\img-2.png)
![Add Seasonal Flavours](images\img-3.png)
![Seasonal Flavours](images\img-4.png)
![Ingrediants](images\img-5.png)
![Add Ingrediants](images\img-6.png)
![Ingrediants list](images\img-7.png)
![User Suggestion](images\img-8.png)

