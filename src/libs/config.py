import ujson

class Config:
    UNDEFINED = "UNDEFINED"
    DEFAULT_BROKER = "mqtt.eclipse.org"
    DEFAULT_INDEX = "/index.html"
    DEFAULT_AP = "AP"
    CONFIG_PROTECTED = ["serial"]
    CONFIG_USR = "usr"
    CONFIG_SYS = "sys"
    CONFIG_SYS_PATH = "/config.%s.json" % (CONFIG_USR)
    CONFIG_USR_PATH = "/config.%s.json" % (CONFIG_SYS)

    me = None

    def __init__(self):
        self.cfg = {}
        self.cfg[Config.CONFIG_SYS] = Config.load(Config.CONFIG_SYS_PATH)
        self.cfg[Config.CONFIG_SYS]["path"] = Config.CONFIG_SYS_PATH
        self.cfg[Config.CONFIG_USR] = Config.load(Config.CONFIG_USR_PATH)
        self.cfg[Config.CONFIG_USR]["path"] = Config.CONFIG_USR_PATH

    def init():
        if not Config.me:
            Config.me = Config()
        return Config.me

    def get(self, ctype, key):
        try:
            return self.cfg[ctype][key]
        except:
            return Config.UNDEFINED

    def set(self, ctype, key, value):
        self.cfg[ctype][key] = value

    def save(self, ctype):
        Config.saveJSON(self.cfg[ctype], self.cfg[ctype]["path"])

    def getSYS(self, key):
        return self.get(Config.CONFIG_SYS, key)

    def setSYS(self, key, value):
        return self.set(Config.CONFIG_SYS, key, value)

    def saveSYS(self):
        return self.save(Config.CONFIG_SYS)

    def getUSR(self, key):
        return self.get(Config.CONFIG_USR, key)

    def setUSR(self, key, value):
        return self.set(Config.CONFIG_USR, key, value)

    def saveUSR(self):
        return self.save(Config.CONFIG_USR)

    def get_default():
        cfg = {}
        cfg["serial"] = Config.UNDEFINED
        cfg["mqtt.id"] = Config.UNDEFINED
        cfg["mqtt.broker"] = Config.DEFAULT_BROKER
        cfg["wifi.essid"] = Config.UNDEFINED
        cfg["wifi.password"] = Config.UNDEFINED
        cfg["web.index"] = Config.DEFAULT_INDEX
        cfg["ap.essid"] = Config.DEFAULT_AP
        return cfg

    def load(path):
        try:
            with open(path, "r+") as f:
                return ujson.load(f)
        except:
            with open(path, "w+") as f:
                cfg = Config.get_default()
                ujson.dump(cfg, f)
            return Config.load(path)

    def saveJSON(cfg, path):
        with open(path, "w+") as f:
            ujson.dump(cfg, f)
