import config.ConfigSensitive as ConfigSensitive
FLASK_APP = "XCGSM"
SQLALCHEMY_DATABASE_URI = ConfigSensitive.DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = ConfigSensitive.SECRET_KEY
