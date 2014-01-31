import MySQLdb

my_connection = MySQLdb.connect(host='blusteele.com', port=3306, db="dv8_esop", user='dv8', passwd='password')
cursor = my_connection.cursor()
