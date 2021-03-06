from micropython import const

# BME280 default address.
BME280_I2CADDR = const(0x76)

# Operating Modes
BME280_OSAMPLE_1 = const(1)
BME280_OSAMPLE_2 = const(2)
BME280_OSAMPLE_4 = const(3)
BME280_OSAMPLE_8 = const(4)
BME280_OSAMPLE_16 = const(5)

# BME280 Registers

BME280_REGISTER_DIG_T1 = const(0x88)  # Trimming parameter registers
BME280_REGISTER_DIG_T2 = const(0x8A)
BME280_REGISTER_DIG_T3 = const(0x8C)

BME280_REGISTER_DIG_P1 = const(0x8E)
BME280_REGISTER_DIG_P2 = const(0x90)
BME280_REGISTER_DIG_P3 = const(0x92)
BME280_REGISTER_DIG_P4 = const(0x94)
BME280_REGISTER_DIG_P5 = const(0x96)
BME280_REGISTER_DIG_P6 = const(0x98)
BME280_REGISTER_DIG_P7 = const(0x9A)
BME280_REGISTER_DIG_P8 = const(0x9C)
BME280_REGISTER_DIG_P9 = const(0x9E)

BME280_REGISTER_DIG_H1 = const(0xA1)
BME280_REGISTER_DIG_H2 = const(0xE1)
BME280_REGISTER_DIG_H3 = const(0xE3)
BME280_REGISTER_DIG_H4 = const(0xE4)
BME280_REGISTER_DIG_H5 = const(0xE5)
BME280_REGISTER_DIG_H6 = const(0xE6)
BME280_REGISTER_DIG_H7 = const(0xE7)

BME280_REGISTER_CHIPID = const(0xD0)
BME280_REGISTER_VERSION = const(0xD1)
BME280_REGISTER_SOFTRESET = const(0xE0)

BME280_REGISTER_CONTROL_HUM = const(0xF2)
BME280_REGISTER_CONTROL = const(0xF4)
BME280_REGISTER_CONFIG = const(0xF5)
BME280_REGISTER_PRESSURE_DATA = const(0xF7)
BME280_REGISTER_TEMP_DATA = const(0xFA)
BME280_REGISTER_HUMIDITY_DATA = const(0xFD)
