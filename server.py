#!/usr/bin/env python

import socket
import logging
import redis

# add filemode="w" to overwrite
logging.basicConfig(filename="/var/log/server.log", level=logging.INFO)

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)
cache = redis.Redis(host='rediska', port=6379)
cache.ping()
while True:
    data = conn.recv(1024)
    if not data:
        break
    if cache.exists(data):
        conn.send("Cached:".encode('utf-8') + data)
    else:
        cache.set(data, data)
        print("Got:", data)
        conn.send("OK:".encode('utf-8') + data)
    logging.info(data)
conn.close()
