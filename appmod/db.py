import sqlite3

class DB:
    def open_DBConn(cls):
        cls.connection = sqlite3.connect('app.db')
        cls.pointer = cls.connection.cursor()
    
    def close_DBConn(cls):
        cls.connection.close()

    # Implement Create DB Tbl SQL Query
    def create_Table(self, tbl_Name: str, fields = []):
        '''
        The fields *arg take in a List of Dictionaries of VSAT Site: 
        Format: 
        create_Table('tbl_Name', fields = [{"field_Name":"", "field_Type":"", "field_Null":""}, etc...])
        '''
        # Create Table Query
        query = f"CREATE TABLE {tbl_Name} ("
        for row in fields:
            query += f"\n{row['field_Name']} \t{row['field_Type']} \t{row['field_Null']},"
        
        query = query[0:len(query)-1:]
        query += ");"

        try:
            self.pointer.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
            self.close_DBConn()
            return False
        return True

    # Implementing INSERT INTO DB Tbl in SQL Query
    def add_VSite(self, vid, lat, lon):
        # Insert Into Table Query
        query = f"INSERT INTO vsat (vsat_id, vsat_lat, vsat_lon) VALUES (?, ?, ?);"
        print(query)
        try:
            self.pointer.execute(query, (vid, lat, lon))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
            self.close_DBConn()
            return False
        return True

    def add_PSite(self, pcode, lat, lon):
        query = f"INSERT INTO province (pro_code, pro_lat, pro_lon) VALUES (?, ?, ?);"
        print(query)
        try:
            self.pointer.execute(query, (pcode, lat, lon))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
            self.close_DBConn()
            return False
        return True

    def remove_VSite(self, vid):
        query = "DELETE FROM vsat WHERE vsat_id = ?"
        try:
            self.pointer.execute(query, (vid,))
            self.connection.commit()
            print('ROW DELETE!')
        except sqlite3.Error as e:
            print(e)

    def pull_Site(cls, tbl_Name: str, col_id="", id = ""):
        cls.open_DBConn()
        # Pull VSAT Site Data From DB and Return
        query = f"SELECT * FROM {tbl_Name}"
        if id != "" and col_id != "":
            query += f"WHERE {col_id} = '{id}'"
        try:
            cls.pointer.execute(
                f"SELECT * FROM {tbl_Name};")
        except sqlite3.Error as e:
            print(e)
            cls.close_DBConn()
            return False
        tmp = cls.pointer.fetchall()
        cls.close_DBConn()
        return tmp
    
    def pull_PSite(self):
        pass
