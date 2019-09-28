import sqlite3 as sq
import psycopg2 as ps


class DB:
    __db = "C:\\Users\\eva_s\\Desktop\\PycharmProjects\\Sample\\portfolio_table_copy2.db"

    def __init__(self):
        self.conn = sq.connect(DB.__db)
        # self.conn.row_factory = sq.Row
        self.cursor = self.conn.cursor()
        self.today_prices = None
        self.second_latest_prices = None
        self.total_prices = None

    def commit(self):
        self.conn.commit()

    # heroku上のDBへ接続
    @staticmethod
    def open_heroku_db():
            conn = ps.connect(host="ec2-54-197-239-115.compute-1.amazonaws.com",
                              port="5432",
                              database="d86t2a5rdbb766",
                              user="sdqpteqaoenvnd",
                              password="410584eca7e4c6d50b8a4eed8fa155973f9f445f84fa659e6cbc2ae94980bdf1"
                              )
            cursor = conn.cursor()
            return cursor

    def get_today_prices(self):
        c = self.cursor
        c.execute("select date from fund_own order by date desc limit 1")
        latest_date = c.fetchone()[0]
        c.execute("select fund_price.fund_code, fund_p"
                  "rice.current_price, fund_own.count, fund_own.purchase_price, "
                  "fund_info.fund_name, fund_info.fund_url from fund_price "
                  "inner join fund_own on fund_price.fund_code = fund_own.fund_code "
                  "inner join fund_info on fund_own.fund_code = fund_info.fund_code "
                  "where fund_price.date='" + latest_date + "' and fund_own.date='" + latest_date + "'"
                  "order by fund_price.fund_code asc")
        self.today_prices = c.fetchall()
        return self.today_prices

    def get_second_latest_prices(self):
        c = self.cursor
        c.execute("select fund_code from fund_info")
        fund_list_number = len(c.fetchall())
        c.execute("select date from fund_own order by date desc limit " + str(fund_list_number + 1))
        second_latest_date = c.fetchall()[-1]
        c.execute("select fund_price.fund_code, fund_price.current_price, fund_own.count, fund_own.purchase_price, "
                  "fund_info.fund_name, fund_info.fund_url from fund_price "
                  "inner join fund_own on fund_price.fund_code = fund_own.fund_code "
                  "inner join fund_info on fund_own.fund_code = fund_info.fund_code "
                  "where fund_price.date='" + second_latest_date[0] + "' and fund_own.date='" + second_latest_date[0] +
                  "' order by fund_price.fund_code asc")
        second_latest_prices = c.fetchall()
        return second_latest_prices

    def get_fund_total_prices(self):
        c = self.cursor
        c.execute("select fund_price.*, fund_own.count, fund_own.purchase_price "
                  "from fund_price "
                  "inner join fund_own on fund_price.fund_code=fund_own.fund_code and fund_price.date=fund_own.date "
                  "order by date desc")
        fund_prices = c.fetchall()
        c.execute("select distinct fund_price.date from fund_price")
        date = c.fetchall()
        # return date
        return fund_prices[:17]


if __name__ == '__main__':
    a = DB().get_fund_total_prices()
    print(a)
