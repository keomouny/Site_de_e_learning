import psycopg2
import logging
from main import *
import time
from setup_logger import logger


class BDD():

    logger.info(
        '[SQL] Connection with sql docker for docker video table: start')

    def __init__(self):
        time.sleep(1)
        self.query_specify = None
        self.mydb = psycopg2.connect(
            host="mouny-db.postgres.database.azure.com",
            dbname="postgres",
            user="mouny@mouny-db",
            password="admin_part_1",
            sslmode="require"
        )

    def create_table(self):
        logger.info('create table data_video')
        self.query_specify = f'CREATE TABLE IF NOT EXISTS data_video (id SERIAL PRIMARY KEY NOT NULL, lien VARCHAR (2000), titre VARCHAR (100), videaste VARCHAR(100), duree VARCHAR (100), vue INT, theme VARCHAR(100));'

    def insert_data(self, query_plus):
        self.query_specify = f'INSERT INTO data_video (lien, titre, videaste, duree, vue, theme) VALUES ( %s, %s, %s, %s, %s, %s)'
        try:
            self.mycursor = self.mydb.cursor()
            self.mycursor.executemany(self.query_specify, query_plus)
        except psycopg2.Error as err:
            logging.error(err)
            exit()

    def select_from_db(self):
        self.mycursor = self.mydb.cursor()
        self.query_specify = 'SELECT * FROM data_video;'
        logger.info('hello')
        self.mycursor.execute(self.query_specify)
        result = self.mycursor.fetchall()
        dict_result = []
        for i in result:
            dict_single_result = {}
            dict_single_result['id'] = i[0]
            dict_single_result['lien'] = i[1]
            dict_single_result['titre'] = i[2]
            dict_single_result['videaste'] = i[3]
            dict_single_result['duree'] = i[4]
            dict_single_result['vue'] = i[5]
            dict_single_result['theme'] = i[6]
            dict_result.append(dict_single_result)
        return dict_result

    def __disconnect__(self):
        self.mydb.commit()
        self.mydb.close()

    def execute_query(self, callback_func):
        try:
            self.mycursor = self.mydb.cursor()
            callback_func()
            self.mycursor.execute(self.query_specify)
        except psycopg2.Error as err:
            logging.error(err)
            exit()
