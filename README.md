# django_learning
MTV - Model Template View

Documento: https://rukbottoland.com/blog/tutorial-de-python-virtualenv/

# INICIANDO CON DJANGO

-Instalamos virtualenv para crear entornos virtuales en python 

$sudo apt-get install python-virtualenv virtualenv

-Creamos el entorno Virtual

$ virtualenv env --python=python3

-Cómo activar un entorno virtual de Python con virtualenv

$ cd env
$ source bin/activate
(env)$

-Cómo desactivar un entorno virtual de Python con virtualenv

(env)$ deactivate
$

-Cómo instalar paquetes en un entorno virtual de Python

pip install Django


-Crear proyecto de django desde el entorno virtual

$ django-admin startproject mysite


- Crear migraciones django

$ python3 manage.py migrate

- Crear un apps en django

$ python3 manage.py startapp nombre

- Iniciar Servidor

$ python3 manage.py runserver
