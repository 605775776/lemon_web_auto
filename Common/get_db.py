from Common.db_handler import DBHandler
from config.yaml_handler import yaml_data


class MyDBHandler(DBHandler):
    def __init__(self):
        super().__init__(host=yaml_data['database']['host'],
                         port=yaml_data['database']['port'],
                         user=yaml_data['database']['user'],
                         password=yaml_data['database']['password'],
                         charset=yaml_data['database']['charset'],
                         database=yaml_data['database']['db'])


if __name__ == '__main__':
    db = MyDBHandler()
    print(db)
    a = db.query("select * from crm_resource where id = 1")
    print(a)
