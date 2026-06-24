import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'J8P+VBUv7sB6XooGHWnM+yHdh1lWePA41Wo5jsXnJpuM7sK7+PpAMoBsukDzaeoG7wKl4JEG7/Jo+AStBvg85g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
   ## BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or DefaultEndpointsProtocol=https;AccountName=images11;AccountKey=XBcsP1nrS4WSttc1bLw1Qp0fyMm8UamllCsiGcBZUTwfe8XU0OLsgNs+5FqhAUhc7s1kOwDJmoIr+ASt6HmCqg==;EndpointSuffix=core.windows.net

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'articlecms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = 'Qyb8Q~x5QsIP1nd9HPCP8AFt2OabKAWnyeDv1dB7'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = '208bd1fa-391e-4e4d-9260-5cba40f112b6'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session