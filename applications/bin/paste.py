from django.http import Http404
import sqlite3

from datetime import datetime
from time import time

class Paste:
    FORMAT = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def all(cls):
        con = sqlite3.connect("test.db")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM nvm_paste")
        result = cursor.fetchall()

        cursor.close()
        con.close()

        def get_there_is_format(created_at):
            stats = {
                "ans":datetime.now().year - created_at.year,
                "mois":datetime.now().month - created_at.month,
                "jours":datetime.now().day - created_at.day,
                "heures":datetime.now().hour - created_at.hour,
                "minutes":datetime.now().minute - created_at.minute,
                "secondes":datetime.now().second - created_at.second,
            }

            print(stats)

            there_is_ago = "/"

            for x, y in stats.items():
                if y > 0:
                    if y == 1:
                        there_is_ago = f"{y} {x.rstrip('s') if x != 'mois' else x}"
                    else:
                        there_is_ago = f"{y} {x}"
                    break

            return there_is_ago

        list_of_tuple_to_dict = [
            {
                'id':x[0], 
                'title':x[1],
                'content':x[2],
                'tags':x[3],
                "img":x[4],
                'created_at':datetime.fromtimestamp(x[5]).strftime("%d %h. %Y, at %H:%M"),
                "views":x[6],
                'there_is_ago':get_there_is_format(datetime.fromtimestamp(x[5])),
            } for x in result
        ]

        return list_of_tuple_to_dict

    @classmethod
    def find(cls, id_:int) -> dict:
        """Find a paste in the database with its ID

        Used in the views create_paste in views.py
        Used in the /bin/paste/<int:id>
        <int:id> represent the id_ parameter we search in the database

        No return in `raise` case :
        -> If id_ is less than 1
        -> If the database request return None : "SELECT * FROM table WHERE id = {id_}"

        :param id_: the paste ID the web-user decide to search
        :type temp: int
        :return: request to database response "SELECT * FROM table WHERE id = {id_}"
        :rtype: dict
        :raise: django.http.Http404 (2 case)
        """

        # l'utilisateur tape toujours bin/paste/1 sauf qu'une liste commence par 0, donc 1 - 1 = 0 : premier(1) élément
        # finalement pas besoin de - 1, dans la base de donnée, l'auto increment commence par 1.
        id_  = int(id_)

        if id_ < 1: # first case
            raise Http404(f"Paste #{id_} does not exist anymore. Paste start by 1 !")

        con = sqlite3.connect("test.db")
        cursor = con.cursor()

        result = cursor.execute("SELECT * FROM nvm_paste WHERE id = ?", (id_,)).fetchone()

        if result is None: # second case
            raise Http404(f"Paste #{id_} does not exist anymore.")

        result = {
            "id":result[0],
            "title":result[1],
            "content":result[2],
            "tags":result[3],
            "img":result[4],
            "created_at":datetime.fromtimestamp(result[5]).strftime("%d %h. %Y, at %H:%M"),
            "views":result[6]
        }

        cursor.close()
        con.close()

        return result
            

    @classmethod
    def create_paste(cls, title, content, tags, img):
        """
        CREATE TABLE "nvm_paste" (
            "id"    INTEGER NOT NULL UNIQUE,
            "title" TEXT,
            "body"  TEXT,
            "tags"  TEXT,
            "timestamp"    INTEGER NOT NULL,
            "img"   TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
        con = sqlite3.connect("test.db")
        cursor = con.cursor()

        cursor.execute("INSERT INTO nvm_paste VALUES(?, ?, ?, ?, ?, ?, ?)", (cursor.lastrowid, title, content, tags, img, int(time()), 0))
        con.commit()

        cursor.close()
        con.close()

        return cursor.lastrowid


    @classmethod
    def get_last_paste(cls):
        con = sqlite3.connect("test.db")
        cursor = con.cursor()

        id_ = cursor.execute("SELECT max(id) from nvm_paste").fetchone()[0]

        cursor.close()
        con.close()

        return id_

    @classmethod
    def add_view(cls, id_):
        con = sqlite3.connect("test.db")
        cursor = con.cursor()

        views = cursor.execute("SELECT views from nvm_paste WHERE id = ?", (id_, )).fetchone()

        views = views[0] + 1 # (234,)[0] + 1

        cursor.execute("UPDATE nvm_paste SET views = ? WHERE id = ?", (views, id_))
        con.commit()

        cursor.close()
        con.close()

        return views