from databricks import sql

from config import SERVER_HOSTNAME
from config import HTTP_PATH
from config import ACCESS_TOKEN


def get_connection():

    connection = sql.connect(

        server_hostname=SERVER_HOSTNAME,

        http_path=HTTP_PATH,

        access_token=ACCESS_TOKEN

    )

    return connection