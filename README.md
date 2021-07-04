# SrIT
Sr IT (Software para Registro de Información y Tipificación), este código está hecho para facilitar la gestión de casos en un HelpDesk ayudando a generar registros y guardarlos.

## Como instalar:
* Linux
```
git clone https://github.com/RodionButEncapsulated/SrIT.git
cd SrIT/
pip3 install -r requirements.txt
python3 SrIT.py
```
* Windows
```
git clone https://github.com/RodionButEncapsulated/SrIT.git
cd SrIT/
pip3 install -r requirements.txt
python3 SrIT.py
```

* Google Colab
```
!git clone https://github.com/RodionButEncapsulated/SrIT.git
%cd SrIT
!pip install -r requirements.txt
!python3 SrIT.py
```

## Requisitos:

Para que el programa funcione correctamente, será **necesario instalar** las siguientes **librerias**:

* [firebase](https://pypi.org/project/firebase/ "Ir a Firebase en PyPI"): Para realizar solicitudes la base de datos.

```
pip install -r requirements.txt
```

## Posibles Errores:
* Al ejecutarse, es posible que el programa genere un error como:
```
    from .async import process_pool
              ^
SyntaxError: invalid syntax
```
Esto ocurre porque la palabra "async" es una palabra reservada de Python. La solución es simplemente cambiar el nombre del archivo "async.py" a cualquier otro (incluyendo en otros archivos donde se le referencia).
Puede encontrar el error expuesto en StackOverflow [aqui](https://stackoverflow.com/questions/52133031/receiving-async-error-when-trying-to-import-the-firebase-package).