class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'db_name': 'test_db'
    })


Config = SystemConfig
