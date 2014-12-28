#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Obtiene la imágen de un producto a partir del id de producto y la muestra en el visor de imagenes por defecto del
sistema de salida.
"""

__author__ = 'archie'

import sys
import subprocess
import os

import requests

import conf


def get_img(pid):
    pid_hundred = int(pid) - (int(pid) % 100)
    url = "http://www.cotodigital.com.ar/fotos/full/%s/%s.jpg" % (str(pid_hundred).zfill(8), pid.zfill(8))
    r = requests.get(url)
    if not r.status_code == requests.codes.OK:
        print "HTTP Error: %s" % r.status_code
        print "No se pudo obtener la imagen en %s" % url
        return None
    else:
        return r.content


def write_img(data, fname):
    try:
        with open(fname, "w+") as img:
            img.write(data)
        return True
    except IOError as e:
        print e.message
        return False


def open_img(fname):
    subprocess.call([conf.img_viewer, fname])


def main(pid):
    img_data = get_img(pid)
    if not img_data:
        sys.exit("Error en la ejecución: No se pudo obtener la imagen")
    fname = os.path.join(conf.tmp_dir, "%s.jpg" % pid)
    if not write_img(img_data, fname):
        sys.exit("Error en la ejecución: No se pudo guardar la imagen localmente!")
    open_img(fname)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit("Uso: \n imgprod.py idprod")
    main(sys.argv[1])