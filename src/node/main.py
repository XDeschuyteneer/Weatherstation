#upip.install('micropython-umqtt.simple')
#upip.install('micropython-umqtt.robust')
import gc
from umqtt.robust import MQTTClient
from config import Config
import topics as t
import network
import utime
import machine
from BME280 import BME280
from machine import RTC
import ntptime

cfg = Config.init()

def toggle(pin):
    print("pin value=", pin.value())
    pin.value(not pin.value())

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network [%s] with [%s]' % (cfg.getSYS("wifi.essid"), cfg.getSYS("wifi.password")))
        wlan.connect(cfg.getSYS("wifi.essid"), cfg.getSYS("wifi.password"))
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=cfg.getSYS("ap.essid"))
    ntptime.settime()

def sub_cb(topic, msg):
    print("message [{msg}] received on [{topic}]".format(topic=topic, msg=msg))

def timeSTR():
    year, month, day, weekday, hours, minutes, seconds, subseconds = RTC().datetime()
    return "%.2d/%.2d/%.4d %.2d:%.2d:%.2d.%d" % (day, month, year, hours, minutes, seconds, subseconds)
    
def update_sensors(client, i2c):
    bme = BME280(i2c=i2c)
    print("t=%s, h=%s, p=%s, t=%s" % (bme.temperature, bme.humidity, bme.pressure, timeSTR()))
    client.publish(t.TEMP, str(bme.temperature))
    client.publish(t.HUMIDITY, str(bme.humidity))
    client.publish(t.PRESSURE, str(bme.pressure))
    client.publish(t.TIMESTAMP, timeSTR())
    
def main():
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=10000)
    led = machine.Pin(2, machine.Pin.OUT)
    do_connect()
    client = MQTTClient(cfg.getSYS("mqtt.id"), cfg.getSYS("mqtt.broker"))
    client.DEBUG = True
    client.set_callback(sub_cb)
    if not client.connect(clean_session=True):
        client.subscribe(t.ACTION_STATUS + "/#")
        client.publish(t.CONNECT, cfg.getSYS("serial"))
    while 1:
        print("loop START")
        gc.collect()
        toggle(led)
        update_sensors(client, i2c)
        utime.sleep(1)
        client.check_msg()
        toggle(led)
    client.disconnect()

main()
