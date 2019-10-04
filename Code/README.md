# How to set your board for the first time for Micropython

You need to program your board using the esptool program from espressif Github repositorie

[esptool](https://github.com/espressif/esptool)

esptool.py is a Python-based, open source, platform independent, utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32 chips.

You will need Python 2.7 or Python 3.4 or newer installed on your system.

The latest stable esptool.py release can be installed from pypi via pip:

```
$ pip install esptool
```

Then erase the entire flash using:

```
$ esptool --chip esp32 --port COM# erase_flash
```

Now download Micropython firmware for your board from here:

[Download](https://micropython.org/download)


And flash the firmware on your board with:

```
$ esptool --chip esp32 --port COM# --baud 115200 write_flash -z 0x1000 esp32-20190529-v1.11.bin
```

Note: COM# means the COM number on your PC