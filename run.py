from EburgEats import app

if __name__ == '__main__':
    app.run(debug=True)


#app.config['MYSQL_USER'] = 'doadmin'
#app.config['MYSQL_PASSWORD'] = 'WRu4WXluYSFlA9lw'
#app.config['MYSQL_PORT'] = '25060'
#pp.config['MYSQL_HOST'] = 'db-mysql-sfo2-40132-do-user-10019964-0.b.db.ondigitalocean.com'
#app.config['MYSQL_DB'] = 'defaultdb'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)

##ssl_args = {'ssl_ca': r'C:\Users\John\Desktop\CWU Assignment File\2021-2022 School Year\Fall 2021\CS380\ca-certificate.crt.txt'}
##engine = create_engine("mysql+mysqlconnector://mysql://doadmin:WRu4WXluYSFlA9lw@private-db-mysql-sfo2-40132-do-user-10019964-0.b.db.ondigitalocean.com:25060/defaultdb", connect_args=ssl_args)
##conn = engine.connect()
##print(engine.connect())
##print(engine.table_names())

