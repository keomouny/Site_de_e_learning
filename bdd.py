import mysql.connector
import logging
from main import *
import time
from setup_logger import logger
import os
from dotenv import load_dotenv


class BDD():

    logger.info(
        '[SQL] Connection with sql docker for docker video table: start')

    def __init__(self):
        time.sleep(1)
        load_dotenv()
        self.query_specify = None
        self.mydb = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            port=3306,
            database=os.environ.get('MYSQ_DBNAME'),
            password=os.environ.get('MYSQL_PASSWORD'),
        )

    def create_table(self):
        logger.info('create table data_video')
        self.query_specify = f'CREATE TABLE IF NOT EXISTS data_video (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, lien VARCHAR (2000), titre VARCHAR (100), videaste VARCHAR(100), duree VARCHAR (100), vue INT, theme VARCHAR(100));'

    def insert_data(self, query_plus):
        self.query_specify = f'INSERT INTO data_video (lien, titre, videaste, duree, vue, theme) VALUES ( %s, %s, %s, %s, %s, %s)'
        try:
            self.mycursor = self.mydb.cursor()
            self.mycursor.executemany(self.query_specify, query_plus)
        except mysql.connector.Error as err:
            logging.error(err)
            exit()

    def select_from_db(self):
        self.mycursor = self.mydb.cursor(dictionary=True)
        self.query_specify = 'SELECT * FROM data_video;'
        self.mycursor.execute(self.query_specify)
        result = self.mycursor.fetchall()
        return result

    def __disconnect__(self):
        self.mydb.commit()
        self.mydb.close()

    def execute_query(self, callback_func):
        try:
            self.mycursor = self.mydb.cursor()
            callback_func()
            self.mycursor.execute(self.query_specify)
        except mysql.connector.Error as err:
            logging.error(err)
            exit()
