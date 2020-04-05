# Weatherstation

## Build status

![CI](https://github.com/XDeschuyteneer/Weatherstation/workflows/CI/badge.svg)

## Description

Weather Station is composed of:
* Main base:
  - ESP8266 nodeMCU v3
  - waveshare e-paper 4.2" screen
* Nodes:
  - ESP8266 nodeMCU v3
  - BME/BMP 280 sensors
  - 32x128px I2C OLED screen

## Setup

Download micropython firmware:

``` sh
wget http://micropython.org/resources/firmware/esp8266-20191220-v1.12.bin -O micropython.bin
```

Or compile it from source:

Setup a virtual env:

``` sh
pip3 install virtualenv
virtualenv weatherstation
source weatherstation/bin/activate
```

Install dependencies:

``` sh
pip3 install esptool
```

Flash micropython:

```sh
esptool.py --port /dev/tty.usbserial-14430 erase_flash
esptool.py --port /dev/tty.usbserial-14430 --baud 460800 write_flash --flash_size=detect 0 micropython.bin
```

## Connect:

Using serial USB interface
```sh
minicom -D /dev/tty.usbserial-14440 -b 115200
```

## Upload files


Install ampy:
```sh
pip3 install ampy
```

Create hello world:
```sh
cat <<EOF > blink.py
import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
while True:
    print("blinking")
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep(1)
EOF
```

Ensuure to quit minicom
Then, flash your program:
```sh
ampy --port /dev/tty.usbserial-14440 -b 115200 put blink.py /blink.py
ampy --port /dev/tty.usbserial-14440 -b 115200 run blink.py
```
