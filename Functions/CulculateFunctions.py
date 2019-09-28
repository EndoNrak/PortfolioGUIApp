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


if __name__ == '__main__':
    today_calculation()
