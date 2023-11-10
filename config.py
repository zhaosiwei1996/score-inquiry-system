import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s [%(funcName)s]-%(process)d %(message)s')
logger = logging.getLogger(__name__)

hostip = '0.0.0.0'
listenport = 5000

# mysql config
mysqlhost = 'localhost'
mysqlport = 3306
mysqldb = 'studentsystem'
mysqluser = 'root'
mysqlpass = '111111'
