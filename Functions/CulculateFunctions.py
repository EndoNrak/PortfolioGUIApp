from Functions.ConnectDB import DB
db = DB()


def today_calculation():
    # 最新の日付におけるデータを取得
    today_prices = db.get_today_prices()

    # 最新のh一つ前の日付におけるデータを取得
    second_latest_prices = db.get_second_latest_prices()

    # 計算
    today_benefit = sum([(i[1]-i[3])*i[2] for i in today_prices])
    today_total_value = sum([i[1]*i[2] for i in today_prices])
    second_latest_total_value = sum([i[1]*i[2] for i in second_latest_prices])
    total_dif = today_total_value - second_latest_total_value

    today = [today_total_value, today_benefit, total_dif]
    return today


def total():
    # データ取得
    fund_prices = db.get_today_prices()
    date_list = db.get_date_list()

    benefit_list = []
    for date in date_list:
        # data = filter(lambda x: x["date"] == date, fund_prices)
        data = [(n["purchase_price"]-n["current_price"]*n["count"]) for n in fund_prices]
        print(data)
        # benefit = [(n[2] - n[4]) * n[3] for n in data]
        # benefit = sum[[(n[2] - n[4]) * n[3]] for n in fund_prices if n[0] == date else pass]
        # benefit_list.append(benefit)
    return benefit_list


if __name__ == '__main__':
    total()
