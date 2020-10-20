import sqlite3 as sql

from django.http import Http404
from django.test import TestCase
from contextlib import contextmanager as ctm

from .paste import Paste

class DatabaseTest(TestCase):

    @ctm
    def con(self):
        try:
            print("YIELD")
            con = sql.connect("test.db")
            cursor = con.cursor()
            yield con, cursor
        finally:
            cursor.close()
            con.close()

    def test_len_find_paste(self):
        """
        
        Test if `bin.paste.Paste.create` well raise a Http404 exception in two case :
        - If id < 1
        - Else If id is not find in the database

        """

        with self.assertRaises(Http404):
            find = Paste.find(4000)

        with self.assertRaises(Http404):
            find = Paste.find(0) # 0 or -1, -2, ...

    def create_paste(self): # not test
        """
        
        Test create paste with limited next on "title", "body"

        """

        with self.con() as (con, cur):
            cur.execute("INSERT INTO abc_paste VALUES(?, ?, ?)", (cur.lastrowid, "ê"*100000, "body !!"))
            con.commit()

    def test_get_last_paste(self):
        print(Paste.get_last_paste())


    def test_get_datetime(self):
        con = sql.connect("test.db")
        cursor = con.cursor()

        let = cursor.execute("SELECT * FROM abc_paste").fetchall()

        print(let)

        for row in let:
            for col in row:
                print(col)
                print(type(col))
            print("---")

        cursor.close()
        con.close()