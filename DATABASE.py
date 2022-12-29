from deta import Deta
from config.settings import PROJECT_KEY, DATABASE_NAME

deta = Deta(PROJECT_KEY)
PoemTable = deta.Base(DATABASE_NAME)
