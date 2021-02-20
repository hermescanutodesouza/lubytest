from util.common import get_env_variable


class Config(object):
    POSTGRES_URL = get_env_variable('POSTGRES_URL')
    POSTGRES_USER = get_env_variable('POSTGRES_USER')
    POSTGRES_PASSWORD = get_env_variable('POSTGRES_PASSWORD')
    POSTGRES_DB = get_env_variable('POSTGRES_DB')

    RESTPLUS_VALIDATE = True
    ERROR_404_HELP = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PAGINATION_PER_PAGE = 10

    uri = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
    SQLALCHEMY_DATABASE_URI = uri.format(user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_URL, db=POSTGRES_DB)
