from settings import DATABASES

from sqlalchemy import create_engine


class DatabaseConnectionError(Exception):
    pass


def db_connect():
    for _, value in DATABASES.items():
        try:
            engine = value['ENGINE']
            if engine == 'sqlite3':
                try: 
                    name = value['NAME']
                    engine = create_engine(f"{engine}:///:memory:", echo=True)
                    return engine
                except KeyError:
                    _format = """DATABASES = {\n
                                    'default': {\n
                                        'ENGINE': 'sqlite3',\n
                                        'NAME': 'Route to sqlite',\n
                                    }\n
                                }"""
                    print (f"Use format {_format} in settings.py All lower case")                     
                    raise DatabaseConnectionError('Database name not defined in settings')
            try:
                name = value['NAME']
                try:
                    host = value['HOST']
                    try:
                        port = value['PORT']
                        try:
                            user = value['USER']
                            try:
                                password = value['PASSWORD']
                                match engine:
                                    case 'postgresql':
                                        try:
                                            engine = create_engine(f"{engine}+psycopg2://{user}:{password}@{host}/{name}", echo = True)
                                            return engine
                                        except ModuleNotFoundError:
                                            raise DatabaseConnectionError(f"You need (psycogp2) installed in your environment to use {engine}")
                                    case 'mysql':
                                        try:
                                            engine = create_engine(f"{engine}+mysqlconnector://{user}:{password}@{host}/{name}", echo = True)
                                            return engine
                                        except ModuleNotFoundError:
                                            try:
                                                engine = create_engine(f"{engine}+pymysql://{user}:{password}@{host}/{name}", echo = True)
                                                return engine
                                            except ModuleNotFoundError:
                                                raise DatabaseConnectionError(f"You need to install (pymysql, mysql-connector-python) to use {engine}")
                                    case _:
                                        raise DatabaseConnectionError("Unsupported DBMS only (postgresql, mysql, sqlite) are supported")
                            except KeyError:
                                _format = """DATABASES = {\n
                                                'default': {\n
                                                    'ENGINE': 'postgresql',\n
                                                    'NAME': 'drdebeletola',\n
                                                    'HOST': 'localhost',\n
                                                    'PORT': '5432',\n
                                                    'USER': 'postgres',\n
                                                    'PASSWORD': 'root',\n
                                                }\n
                                            }"""
                                print (f"Use format {_format} in settings.py All lower case")         
                                raise DatabaseConnectionError(f"Password for user {user} not defined in database")                   
                        except KeyError:
                            _format = """DATABASES = {\n
                                            'default': {\n
                                                'ENGINE': 'postgresql',\n
                                                'NAME': 'drdebeletola',\n
                                                'HOST': 'localhost',\n
                                                'PORT': '5432',\n
                                                'USER': 'postgres',\n
                                                'PASSWORD': 'root',\n
                                            }\n
                                        }"""
                            print (f"Use format {_format} in settings.py All lower case")
                            raise DatabaseConnectionError(f"Username for the database {user} not defined in settings")                        
                    except KeyError:
                        _format = """DATABASES = {\n
                                        'default': {\n
                                            'ENGINE': 'postgresql',\n
                                            'NAME': 'drdebeletola',\n
                                            'HOST': 'localhost',\n
                                            'PORT': '5432',\n
                                            'USER': 'postgres',\n
                                            'PASSWORD': 'root',\n
                                        }\n
                                    }"""
                        print (f"Use format {_format} in settings.py All lower case")
                        raise DatabaseConnectionError('Service address for database engine not defined in settings')
                except KeyError:
                    _format = """DATABASES = {\n
                                    'default': {\n
                                        'ENGINE': 'postgresql',\n
                                        'NAME': 'drdebeletola',\n
                                        'HOST': 'localhost',\n
                                        'PORT': '5432',\n
                                        'USER': 'postgres',\n
                                        'PASSWORD': 'root',\n
                                    }\n
                                }"""
                    print (f"Use format {_format} in settings.py All lower case")
                    raise DatabaseConnectionError('Host address for database engine not defined in settings')
            except KeyError:
                _format = """DATABASES = {\n
                                'default': {\n
                                    'ENGINE': 'postgresql',\n
                                    'NAME': 'drdebeletola',\n
                                    'HOST': 'localhost',\n
                                    'PORT': '5432',\n
                                    'USER': 'postgres',\n
                                    'PASSWORD': 'root',\n
                                }\n
                            }"""
                print (f"Use format {_format} in settings.py All lower case")
                raise DatabaseConnectionError('Database name not defined in settings')
        except KeyError:
            _format = """DATABASES = {\n
                            'default': {\n
                                'ENGINE': 'postgresql',\n
                                'NAME': 'drdebeletola',\n
                                'HOST': 'localhost',\n
                                'PORT': '5432',\n
                                'USER': 'postgres',\n
                                'PASSWORD': 'root',\n
                            }\n
                        }"""
            print (f"Use format {_format} in settings.py All lower case")
            raise DatabaseConnectionError('No database engine defined in settings')