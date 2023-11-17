#!/usr/bin/env python
# https://pypi.python.org/pypi/JayDeBeApi/
# JAVA_HOME="c:\Program Files (x86)\Java\jre1.8.0_45\"
# JAVA_JRE="c:\Program Files (x86)\Java\jre1.8.0_45\"
'''
>>> import jaydebeapi
>>> conn = jaydebeapi.connect("org.hsqldb.jdbcDriver",
...                           "jdbc:hsqldb:mem:.",
...                           ["SA", ""],
...                           "/path/to/hsqldb.jar",)
>>> curs = conn.cursor()
>>> curs.execute('create table CUSTOMER'
...              '("CUST_ID" INTEGER not null,'
...              ' "NAME" VARCHAR(50) not null,'
...              ' primary key ("CUST_ID"))'
...             )
>>> curs.execute("insert into CUSTOMER values (1, 'John')")
>>> curs.execute("select * from CUSTOMER")
>>> curs.fetchall()
[(1, u'John')]
>>> curs.close()
>>> conn.close()
'''
import os
from urllib.parse import urlparse

_url = os.getenv("APPMSW_IRIS_URL")
o = urlparse(_url)

import jaydebeapi
import sys
if __name__ == '__main__':
  #jdbc_url = "jdbc:iris://superuser:SYS@iris-test:52773/USER"
  jdbc_url = "jdbc:iris://django:django-todo-37@iris-test:51773/APPTOOLSADMIN"
  driverName = "com.intersystems.jdbc.IRISDriver"
  statement = "select * FROM apptools_core.Log order by id desc"

  conn = jaydebeapi.connect(driverName, jdbc_url)
  curs = conn.cursor()
  curs.execute(statement)
  print(curs.fetchall())

  conn.close()

  sys.exit(0)

