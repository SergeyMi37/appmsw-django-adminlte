import jaydebeapi
#jdbc:IRIS://mswiris:S37^asu3@192.168.0.135:51774/USER
#con = jaydebeapi.connect('com.intersystems.jdbc.IRISDriver','jdbc:IRIS://iris:1972/USER',['superuser','SYS'],jars = ['appmsw/java/intersystems-jdbc-3.3.0.jar','appmsw/java/intersystems-jdbc-3.7.1.jar'])
con = jaydebeapi.connect('com.intersystems.jdbc.IRISDriver','jdbc:IRIS://192.168.0.135:51774/USER',['mswiris','S37^asu3'],jars = ['appmsw/java/intersystems-jdbc-3.3.0.jar','appmsw/java/intersystems-jdbc-3.7.1.jar'])
curs = con.cursor()
curs.execute("select * FROM apptools_core.Log order by id desc")
print(dir(curs))
print(curs.rowcount,curs.arraysize)
#print(curs.fetchall())
column_names = [record[0] for record in curs.description]
print(column_names)
#column_and_values = [dict(column_names, record) for record in curs.fetchall()]
#print(column_and_values)
for row in curs.fetchall():
    print(row)
con.close()
