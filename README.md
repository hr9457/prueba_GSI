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



# Docker y Docker Compose

## Docker
archivod dockerfile para el levantamiento y configuracion de la api FastApi y requerimentos para instlacion en el ambien de despliegue

```
FROM python:3

WORKDIR /app

COPY req.txt .

RUN pip install --no-cache-dir --upgrade -r req.txt


COPY . .

EXPOSE 8000


CMD ["fastapi", "run", "main.py", "--port", "8000"]
```


## Docker Compose
Modelo del archivo docker-compose para el lenvantamiento de la base de datos postgres y de la api de python para el levantamiento de ambos servicios con la inicializacion dle modelo int.sql para el arranque de la base de datos.

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
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql


  api:
    build: ./backend
    container_name: api
    ports:
      - "8000:8000"
    environment:
      - USER = "root"
      - PASS = "root"
      - HOST = "192.168.122.128"
      - PORT = 5432
      - NAME = "mydatabase"
    depends_on:
      - postgres
```


# Modelo de Base de datos
Modelo utilizado para el modelado de la infrasestrucara de la base de datos utilzadopara el control de la API (MODELO TIPO KANBAN)

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