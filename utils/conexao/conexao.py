import psycopg2


class MyDatabase:
    def __init__(self, hostname="localhost", database="nuclea", username="postgres",
                 pwd="dev123", port_id=5432):
        self.conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()
