import sys
import os
import socket

import getopt
import time
from faker import Faker
from faker.providers import internet

fake = Faker('en_US')
fake.add_provider(internet)
Faker.seed(0)
from datetime import datetime
from datetime import timedelta

from random import choice, randint, sample

from faker.providers import BaseProvider
os.chdir('/home/cdsw/faker_jira')
from flight_routes import routes

 
num = 1001
host = "3.122.10.192"
port = 63887

        
def netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    s.close()

"""
Tweet: structure
"""
for t in range(1,num):
  now = datetime.now()
  ts = now.strftime("%Y-%m-%d %H:%M:%S")
  ipv4 = fake.ipv4_public()
  email = fake.ascii_email()
  user_name = fake.user_name()
  route = choice ( routes )
  airport = route ["origin"]
  r1 = str(fake.random_number(fix_len=True))
  r2 = str(fake.random_number(digits=3))
  sentence = fake.sentence(30)
  content=str("%s,%s,%s,%s,%s,%s,%s,%s\n" % ( ts ,ipv4,email,user_name,airport,r1,r2,sentence))
  netcat (host,port, content)
