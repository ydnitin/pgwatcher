#!/usr/local/bin/python
import psycopg2
import sys
import pprint

def main():
    conn_string = "host='10.100.100.11' dbname='postgres' user='postgres'"
    print "Connecting to the database\n => %s" % (conn_tring)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print "Connected!\n"

if __name__ == "__main__":
    main()
