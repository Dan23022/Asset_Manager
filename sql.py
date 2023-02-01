import sqlite3
con = sqlite3.connect("assets.db")
cur = con.cursor()
cur.execute("CREATE TABLE Assets(asset_number, asset_name, assignee)")
