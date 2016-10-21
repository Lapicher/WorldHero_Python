# Guía de instalación y uso del API

Intrucciones para el correcto funcionamiento del sistema.

## Instalación de Python:
Lo primero que necesitamos para instalar es Python. Version utilizada: 3.5.2 ([descarga e instrucciones](https://www.continuum.io/downloads)).

Para comprobar que tienes la versión de Python correcta, una vez instalado abre una ventana de comandos, escribe `python` y presionar enter.

Deberás ver algo como:

```
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>_
```

Nota: Fíjate que vamos a utilizar la versión de Python 3.5.2.
Si tienes instalada cualquier otra versión necesitas crear un entorno virtual.


## Creación de Entorno Virtual.

Crear el entorno virutal.

Ya creado el entorno virtual necesitaremos activarlo para que el proyecto trabaje desde ese entorno e instale las dependencias en el mismo entorno.

Para activar situarse en el directorio donde se haya creado el entorno virutal y ejecutar la siguiente comando:

```
 ✝  ~/Documents/Nataly/KeepCoding/Python_y_Django/WorldHero>  source env/bin/activate

```

Para desactivar el entorno virtual (comando):

> deactivate


## 1. Instalación del Proyecto:
Para instalar Worldhero se necesita clonar el éste repositorio, para eso, tener instalado [GIT](https://git-scm.com/). Ya instalado ejecutar el comando para clonar el proyecto a nuestro repositorio:

    > git clone https://github.com/Lapicher/WorldHero_Python.git

Ya descargado el repositorio, cargar el proyecto en pyCharm e instalar las dependencias del proyecto que se encuentran en el archivo requeriments.txt
En la ventana de comandos y escribir:

    > pip install -r  requirements.txt
    
Adicional para agregar mas dependencias al archivo:
	
	> pip freeze > requirements.txt 

Tambien se utilizo gulp para el minimizado y optimizacion de imagenes, si se requiere utilizar, se necesita instalar las dependencias de node con (Opcional):
	
	> npm install
	
Y listo para ejecutar gulp:
	
	> gulp

## 2. Primera configuracion inicial:


Crear superusuario:

	python3 manage.py createsuperuser
	
Crear las migraciones de los modelos. 

	python3 manage.py makemigrations
	
para aplicar la migracion y crea las tablas en la base de datos en sqlite:
	
	python manage.py migrate
	
## 3. Configuracion finales:

Levantar el servidor web de desarrollo y listo, estaria ya corriendo el proyecto Worldhero en Django:

	python manage.py runserver
	
###***IMPORTANTE***

Ya ingresado en el administrador de Django, crear desde ahi las categorias de los posts.

El sistema permite registrarse e iniciar sesion, ya iniciado sesion puede crear posts, listar los posts publicados y ver detalle. Se puede buscar posts por el titulo, contenido del post.
	
	
# Uso de API REST:

## GET

#### * Listado de todos los posts:

Direccion url, donde localhost es el servidor API Rest:
	
	http://localhost:8000/api/1.0/blogs/
	
###Notas: 

Para listar los posts se puede estar autentificado o no. 
#####Autentificado
	
Podrá ver el listado de posts publicos y privados del usuario autentificado y solamente publicos de otros usuarios. El administrador podra ver todos los posts.

#####No autentificado

Solo podra listar los posts publicos de los usuarios.

###HEADERS

	Content-type: application/json
	Authorization: Basic bmF0YWx5OnN1cGVyc2VndXJh
	
Realizar la peticion GET y si la peticion fue correcta con codigo 200 OK verá algo como:

	{
	  "count": 3,
	  "next": null,
	  "previous": null,
	  "results": [
	    {
	      "title": "Gato",
	      "image": "uploads/1280x720-btt.jpg",
	      "intro": "Minino de Pelo Negro",
	      "datePub": "2016-10-11T00:00:00Z"
	    },
	    {
	      "title": "Perro",
	      "image": "uploads/12039400_1040383909305585_2169445179203185951_n.jpg",
	      "intro": "Perrito Hermoso",
	      "datePub": "2016-10-01T00:00:00Z"
	    },
	    {
	      "title": "Simone Simons",
	      "image": "uploads/Epica2014s_0.jpg",
	      "intro": "Epica Gennial",
	      "datePub": "2016-10-01T00:00:00Z"
	    }
	  ]
	}
	 

#### * Detalle de un post: 

Direccion URL:

	http://localhost:8000/api/1.0/blogs/67/
	
Donde el numero 67 es el identificador del post, Si el post es publico un usuario no autentificado podra verlo, si es administrador o propietario del post, podra ver el post publico y privado, el administrador puede ver el de cualquier usuario.

Al hacer la peticion se obtendra la siguiente respuesta en el body con toda la informacion del modelo:

	{
	  "id": 67,
	  "owner": "nataly",
	  "image": "http://static.hogarmania.com/archivos/201511/animales-albinos-848x477x80xX.jpg",
	  "title": "Tigre Blanco modified by nataly",
	  "intro": "Animal salvaje",
	  "body": "Mamifero carnivoro",
	  "datePub": "2016-10-11T00:00:00Z",
	  "created_at": "2016-10-21T04:04:15.296750Z",
	  "modified_at": "2016-10-21T04:17:01.687143Z",
	  "visibility": "PUB",
	  "type": [
	    1
	  ]
	}
	

## POST

Direccion URL:

	http://localhost:8000/api/1.0/blogs/
	
En el body se le manda el json como raw:

	{
	  "image": "http://elpais.com/elpais/imagenes/2016/03/01/icon/1456828391_987602_1457431840_sumario_normal.jpg",
	  "title": "Hamster",
	  "intro": "Animal chiquito y bonito",
	  "body": "Chulada de animalito cariñoso",
	  "datePub": "2016-10-11T00:00:00Z",
	  "created_at": "2016-10-21T03:21:12.364058Z",
	  "modified_at": "2016-10-21T03:21:12.364134Z",
	  "visibility": "PRI",
	  "type": [
	    1
	  ]
	}
	
Al realizar la creación del post, el propietario del post es el usuario autenticado, un usuario no autentificado no puede crear posts, necesita antes registrarse.


Respuesta correcta: 

	{
	  "id": 69,
	  "owner": "nataly",
	  "image": "http://elpais.com/elpais/imagenes/2016/03/01/icon/1456828391_987602_1457431840_sumario_normal.jpg",
	  "title": "Hamster",
	  "intro": "Animal chiquito y bonito",
	  "body": "Chulada de animalito cariñoso",
	  "datePub": "2016-10-11T00:00:00Z",
	  "created_at": "2016-10-21T05:33:29.100312Z",
	  "modified_at": "2016-10-21T05:33:29.100397Z",
	  "visibility": "PRI",
	  "type": [
	    1
	  ]
	}
	
En caso de algun error, puede mostrar el mensaje como error de autenticacion o que no tiene los permisos para realizar dicha acción.
	
	{
	  "detail": "Authentication credentials were not provided."
	}
ó

	{
	  "detail": "You do not have permission to perform this action."
	}

## PUT

Direccion URL:
	
	http://localhost:8000/api/1.0/blogs/67/


En el body se le manda el json como raw:

	{
	  "owner": "nataly",
	  "image": "http://static.hogarmania.com/archivos/201511/animales-albinos-848x477x80xX.jpg",
	  "title": "Tigre Blanco modified by nataly",
	  "intro": "Animal salvaje",
	  "body": "Mamifero carnivoro",
	  "datePub": "2016-10-11T00:00:00Z",
	  "created_at": "2016-10-21T04:04:15.296750Z",
	  "modified_at": "2016-10-21T04:04:15.296821Z",
	  "visibility": "PUB",
	  "type": [
	    1
	  ]
	}
	
Para modificar un post, es necesario estar autenticado, solo el propietario puede modificar sus posts. En el caso del administrador podra modificar cualquier posts y modificarle el campo owner.


Respuesta 200 OK: 

	{
	  "id": 67,
	  "owner": "nataly",
	  "image": "http://static.hogarmania.com/archivos/201511/animales-albinos-848x477x80xX.jpg",
	  "title": "Tigre Blanco modified by nataly",
	  "intro": "Animal salvaje",
	  "body": "Mamifero carnivoro",
	  "datePub": "2016-10-11T00:00:00Z",
	  "created_at": "2016-10-21T04:04:15.296750Z",
	  "modified_at": "2016-10-21T04:17:01.687143Z",
	  "visibility": "PUB",
	  "type": [
	    1
	  ]
	}

## Delete
	
Direccion URL:
	
	http://localhost:8000/api/1.0/blogs/65/

Respuesta correcta: Codigo 204 No Content

	Contenido vacío.
	
	

#***Listo!!***
###A disfrutar de Worldhero.



