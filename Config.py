import os


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DATA_URL = os.getenv(os.path.join('DATABASE'))
    # SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
    TESTING = False
    USERS = os.getenv("use", os.environ.get("DB_USER"))
    PASSWD = os.getenv("pass", os.environ.get("DB_PASS"))
    DB_DATABASE = os.getenv("db_database")
    # 平台的key作为校验。
    SECRET_KEY = 'suibiandingyi123131'

    # 微信信息
    APPID = ''
    APPSERECT = ''
    TOKEN = ''
    APP_API_URL = ''

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DB_URL = os.getenv(
        f"mysql+cymysql://{Config.USERS}:{Config.PASSWD}@{os.environ.get('DB_URL')}:3306/{Config.DB_DATABASE}")


class DevelopmentConfig(Config):
    DEBUG = True
    DB_URL = os.getenv("DB_URL", f"mysql+cymysql://{Config.USERS}:{Config.PASSWD}@{os.environ.get('DB_URL')}:3306/{Config.DB_DATABASE}")


class TestingConfig(Config):
    DB_URL = os.getenv("DB_URL", f"mysql+cymysql://{Config.USERS}:{Config.PASSWD}@{os.environ.get('DB_URL')}:3306/{Config.DB_DATABASE}")
    TESTING = True


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'defaults': DevelopmentConfig
}
