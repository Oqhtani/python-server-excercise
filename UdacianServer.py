#!/usr/bin/env python3
#
# Udacian activity to practice http get and post
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from  Udacian import*
import os

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
    	#Submit the form
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode()
        name = parse_qs(data)["name"][0]
        city = parse_qs(data)["city"][0]
        enrollment = parse_qs(data)["enrollment"][0]
        nanodegree = parse_qs(data)["nanodegree"][0]
        status = parse_qs(data)["status"][0]

        udacian=Udacian(name,city,enrollment,nanodegree,status)


        # Store it in memory.
        memory.append(udacian)

        # 1. Send a 303 redirect back to the root page.
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
    	#get the info and display it
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        list=""
        # 2. Put the response together out of the form and the stored messages.
        for udacian in memory:
            list+=Udacian.print_udacian(udacian)
        msg=form.format("\n"+list)
        self.wfile.write(msg.encode())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
