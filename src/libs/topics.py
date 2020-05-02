from config import Config

cfg = Config.init()

APP_NAME = "xws"
APP = "{app}/{serial}".format(app=APP_NAME, serial=cfg.getSYS("serial"))

CONNECT = "{app}/connect".format(app=APP)
ACTION_SET = "{app}/actions/set".format(app=APP)
ACTION_STATUS = "{app}/actions/status".format(app=APP)
LOGS = "{app}/logs/".format(app=APP)
SENSORS = "{app}/sensors/status".format(app=APP)
TEMP = "{sensors}/temp".format(sensors=SENSORS)
HUMIDITY = "{sensors}/humidity".format(sensors=SENSORS)
PRESSURE = "{sensors}/pressure".format(sensors=SENSORS)
TIMESTAMP = "{sensors}/timestamp".format(sensors=SENSORS)
