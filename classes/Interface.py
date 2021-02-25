from classes import DHT11
from classes import HCSR04
from classes import PIR
import time

from classes.MySqlConnection import DatabaseMySql
from classes.PyMongoConnection import MongoConect
from classes.File import File
from classes.DataList import DataList

DHTL = DataList()
HCSL = DataList()
PIRL = DataList()
connection = DatabaseMySql()
connectionMDB = MongoConect()
DB = connectionMDB.CLIENT['pymongo']
try:
    DHTL = File.readData("dht.bin")
except Exception as e:
    print("error " + str(e))
try:
    HCSL = File.readData("hcs.bin")
except Exception as e:
    print("error " + str(e))
try:
    PIRL = File.readData("pir.bin")
except Exception as e:
    print("error " + str(e))


class Interface:

    @staticmethod
    def saveDHT():
        while True:
            try:
                data = DHT11.readDht()
                DHTL.append(data)
                File.saveData(DHTL, "dht.bin")
                connection.sendData(data, "DHT")
                MongoConect.createMongo(connectionMDB, DB['DHT'], data)
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                raise error
            time.sleep(2.0)

    @staticmethod
    def saveHCS():
        while True:
            try:
                data = HCSR04.readHC()
                HCSL.append(data)
                File.saveData(HCSL, "hcs.bin")
                connection.sendData(data, "HCS")
                MongoConect.createMongo(connectionMDB, DB['HCS'], data)
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                raise error
            time.sleep(2.0)

    @staticmethod
    def savePIR():
        while True:
            try:
                data = PIR.readPir()
                PIRL.append(data)
                File.saveData(PIRL, "pir.bin")
                connection.sendData(data, "PIR")
                MongoConect.createMongo(connectionMDB, DB['PIR'], data)
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                raise error
            time.sleep(2.0)

    @staticmethod
    def showDHT():
        try:
            while True:
                data = DHT11.readDht()
                print(data)
        except KeyboardInterrupt:
            pass

    @staticmethod
    def showHCS():
        try:
            while True:
                data = HCSR04.readHC()
                print(data)
        except KeyboardInterrupt:
            pass

    @staticmethod
    def showPIR():
        try:
            while True:
                data = PIR.readPir()
                print(data)
        except KeyboardInterrupt:
            pass
