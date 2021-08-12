# car_sale

Тестовое задание FinSTC Software LLC

__Endpoints:__ 

![](https://github.com/annvlkva/car_sale/blob/master/dealers.PNG)
![](https://github.com/annvlkva/car_sale/blob/master/cars.PNG)


__Примеры запросов:__

+ GET `http://127.0.0.1:8000/cars/` 

Список всех машин

![](https://github.com/annvlkva/car_sale/blob/master/screenshots/cars_get.PNG)

+ GET `http://127.0.0.1:8000/cars/<int:id>`

Машина с данным id
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/car_get_id.PNG)

+ POST `http://127.0.0.1:8000/cars/`

Добавление новой машины
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/car_post.PNG)

+ PUT `http://127.0.0.1:8000/cars/<int:id>`

Редактирование данных машины
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/car_put.PNG)

+ DELETE `http://127.0.0.1:8000/cars/<int:id>`

Удаление машины
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/car_delete.PNG)


+ GET `http://127.0.0.1:8000/dealers/` 

Список всех дилеров

![](https://github.com/annvlkva/car_sale/blob/master/screenshots/dealers_get.PNG)

+ GET `http://127.0.0.1:8000/dealers/<int:id>`

Дилер с данным id
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/dealers_get_id.PNG)

+ POST `http://127.0.0.1:8000/dealers/`

Добавление нового дилера
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/dealer_post.PNG)

+ PUT `http://127.0.0.1:8000/dealers/<int:id>`

Редактирование данных дилера
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/dealer_put.PNG)

+ DELETE `http://127.0.0.1:8000/dealers/<int:id>`

Удаление дилера (также будут удалены машины, которые принадлежат данному дилеру)
![](https://github.com/annvlkva/car_sale/blob/master/screenshots/dealer_delete.PNG)
