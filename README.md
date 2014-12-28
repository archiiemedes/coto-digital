Coto-Digital
============

Descripción
===========
Por el momento la única función de este proyecto es la de recopilar scripts de Python que puedan resultar útiles para
quienes hacen un poco de micro-economía hogareña y hacen sus compras en los supermercados Coto (digital o no).


imgprod.py  - Intenta solucionar la molestia de estar mirando el listado de lo que compramos y no tener idea que
              significa una descripción del estilo de "BOCADAMABTSX160G".

Dependencias
============
Requests - http://docs.python-requests.org/en/latest/


Instalación
===========
El único requerimiento antes de utilizar los scripts (además de las dependencias) es:
-Hacer una copia del archivo conf.tpl
-Nombrar a esta copia como conf.py
-Editar conf.py y configurar los parámetros necesarios ej. directorio temporal de trabajo


Uso
===
imgprod.py --> python imgprod.py prodid

prodid - id de producto
