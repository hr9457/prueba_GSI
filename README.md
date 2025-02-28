# prueba_GSI

## CREACION DE ENTORNO
comando para crear entron venv en windows para ejercutar api con sus depenedias

```
python -m venv venv
```

## ACTIVACION ENTORNO

Comando para activar el entorno de trabajo de la api

```
.\venv\Scripts\activate
```

## REQUERIMIENTOS


Instalacion de requerimientos para funcionamiento de la api

```
pip install -r req.txt
```

## GENERAR REQUERMIENTOS
comando para genera los requerimientos de las depencias utlizadas en la api

```` 
pip freeze > req.txt
```` 


## Arrenque fast api principal

```
fastapi dev main.py
```



# Docker BAse de datos

```
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
```


# Modelo de Base de datos

```



create table kanban(
	id_kanban serial primary key,
	name_kanban varchar(100) not null
);


create table stack(
	id_stack serial primary key,
	name_stack varchar(100) not null,
	id_kanban int not null,
	constraint fk_kanban foreign key (id_kanban) references kanban(id_kanban)
);

create table taks(
	id_task SERIAL primary key,
	name_task varchar(100) not null,
	description varchar(500) not null,
	asigned_to varchar(100) not null,
	id_stack int not null,
	constraint fk_stack foreign key (id_stack) references stack(id_stack)
);


```