import sqlite3
from cryptography.fernet import Fernet

class Connection:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.key = b'dXhdh2hqrh-09LOT6UAsNiG0B3Hg2mqrlHQ9Cfv2w7Q='
        self.suite = Fernet(self.key)

    def read(self, table):
        data = []
        for record in self.cursor.execute('SELECT * FROM {}'.format(table)):
            dec_user = self.suite.decrypt(bytes(record[0], 'utf-8')).decode('utf-8')
            dec_pass = self.suite.decrypt(bytes(record[1], 'utf-8')).decode('utf-8')
            dec_ign = self.suite.decrypt(bytes(record[2], 'utf-8')).decode('utf-8')
            dec_record = (dec_user, dec_pass, dec_ign)
            data.append(dec_record)
        return data
    
    def write(self, table, record):
        enc_user = self.suite.encrypt(record[0].encode('utf-8')).decode('utf-8')
        enc_pass = self.suite.encrypt(record[1].encode('utf-8')).decode('utf-8')
        enc_ign = self.suite.encrypt(record[2].encode('utf-8')).decode('utf-8')
        enc_record = (enc_user, enc_pass, enc_ign)
        self.cursor.execute('INSERT INTO {} VALUES {}'.format(table, enc_record))
        self.connection.commit()

    def wipe(self, table):
        self.cursor.execute('DELETE FROM {}'.format(table))
        self.connection.commit()