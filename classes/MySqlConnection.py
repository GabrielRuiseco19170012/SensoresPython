import pymysql


class DatabaseMySql:

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pymysql'
        )
        self.cursor = self.connection.cursor()
        print("Established Connection with MySql")

    def sendData(self, data, table):
        sqlDHT = "INSERT INTO `%s`" % table + "(temp,humidity) VALUES (%s,%s)"
        sqlHCS = "INSERT INTO `%s`" % table + "(distance) VALUES (%s)"
        sqlPIR = "INSERT INTO UserMaterials(precense) VALUES (%s)"
        try:
            if table == "DHT":
                self.cursor.execute(sqlDHT, (data["Temp"], data["Humidity"]))
                self.connection.commit()
            elif table == "HCS":
                self.cursor.execute(sqlHCS, data)
                self.connection.commit()
            else:
                self.cursor.execute(sqlPIR, data)
                self.connection.commit()
        except Exception as e:
            raise

    def getAllData(self, table):
        sql = 'SELECT * FROM `%s`' % table
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    def getOneData(self, column, table, value):
        sql = 'SELECT * FROM `%s`' % table + ' WHERE `%s`' % column + ' = %s'
        try:
            self.cursor.execute(sql, value)
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            raise

    def getManyData(self, column, table, value):
        sql = 'SELECT * FROM `%s`' % table + ' WHERE `%s`' % column + ' = %s'
        try:
            self.cursor.execute(sql, value)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    # def getUMList(self, mid, uid):
    #     sql = 'SELECT * FROM UserMaterials WHERE MaterialID = %s AND UserID = %s'
    #     try:
    #         self.cursor.execute(sql, (mid, uid))
    #         data = self.cursor.fetchone()
    #         return data
    #     except Exception as e:
    #         raise

    # def updateData(self, table, column, updCol, newVal, idVal):
    #     sql = ""
    #     if table == "Users":
    #         sql = 'UPDATE Users SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
    #     elif table == "UserMaterials":
    #         sql = 'UPDATE UserMaterials SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
    #     elif table == "Materials":
    #         sql = 'UPDATE Materials SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
    #     else:
    #         print("tabla no encontrada")
    #     try:
    #         self.cursor.execute(sql, (newVal, idVal))
    #         self.connection.commit()
    #     except Exception as e:
    #         raise

    # def deleteData(self, table, column, idval):
    #     sql = 'DELETE FROM `%s`' % table + 'WHERE `%s`' % column + ' = %s'
    #     try:
    #         self.cursor.execute(sql, idval)
    #         self.connection.commit()
    #     except Exception as e:
    #         raise
