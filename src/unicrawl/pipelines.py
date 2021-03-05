# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from mysql.connector import errorcode
import logging


class UnicrawlPipeline:
    logger = logging.getLogger()

    def __init__(
        self,
        mysql_host,
        mysql_port,
        mysql_user,
        mysql_password,
        mysql_database,
        mysql_table,
        mysql_charset,
        mysql_collation,
        mysql_raise_on_warnings,
    ):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database
        self.mysql_table = mysql_table
        self.mysql_charset = mysql_charset
        self.mysql_collation = mysql_collation
        self.mysql_raise_on_warnings = mysql_raise_on_warnings
        self.cnx = self.mysql_connect()
        self.mysql_create_table()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get("MYSQL_HOST"),
            mysql_port=crawler.settings.get("MYSQL_PORT"),
            mysql_user=crawler.settings.get("MYSQL_USER"),
            mysql_password=crawler.settings.get("MYSQL_PASSWORD"),
            mysql_database=crawler.settings.get("MYSQL_DATABASE"),
            mysql_table=crawler.settings.get("MYSQL_TABLE"),
            mysql_charset=crawler.settings.get("MYSQL_CHARSET"),
            mysql_collation=crawler.settings.get("MYSQL_COLLATION"),
            mysql_raise_on_warnings=crawler.settings.get("MYSQL_RAISE_ON_WARNINGS"),
        )

    def process_item(self, item, spider):
        self.logger.debug("Saving item to " + self.mysql_table)
        self.save_item(dict(item))
        return item

    def save_item(self, new_item):
        cursor = self.cnx.cursor()
        sql_query = "INSERT INTO " + self.mysql_table + "(url, html) " "VALUES (%(url)s, %(html)s)"

        # Insert new_item as a new row into mysql_table
        cursor.execute(sql_query, new_item)
        rowId = cursor.lastrowid
        self.cnx.commit()
        cursor.close()
        self.logger.debug("Item saved with ID: {}".format(rowId))

    def mysql_connect(self):
        try:
            return mysql.connector.connect(
                host=self.mysql_host,
                port=self.mysql_port,
                user=self.mysql_user,
                password=self.mysql_password,
                database=self.mysql_database,
                charset=self.mysql_charset,
                collation=self.mysql_collation,
                raise_on_warnings=self.mysql_raise_on_warnings,
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.logger.critical("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.logger.critical("Database does not exist")
            else:
                self.logger.critical(err)

    def mysql_create_table(self):
        cursor = self.cnx.cursor()
        sql_query = (
            "CREATE TABLE IF NOT EXISTS `" + self.mysql_table + "` ("
            "  `id` mediumint NOT NULL AUTO_INCREMENT,"
            "  `url` text NOT NULL,"
            "  `html` mediumtext NOT NULL,"
            "  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
            "  PRIMARY KEY (`id`)"
            ")"
        )

        try:
            self.logger.debug("Creating table {} if it doesn't exists.".format(self.mysql_table))
            cursor.execute(sql_query)
        except mysql.connector.Error as err:
            self.logger.critical(err)
        else:
            self.logger.debug("Table OK")

        cursor.close()

    def close_spider(self, spider):
        self.cnx.close()
