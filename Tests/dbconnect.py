import MySQLdb

my_connection = MySQLdb.connect(host='blusteele.com', port=3306, db="esop", user='dv8_esop', passwd='password')
cursor = my_connection.cursor()
