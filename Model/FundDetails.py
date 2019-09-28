class FundDetails:
    def __init__(self, today_data, yesterday_data):
        self.today_fund = Fund(today_data)
        self.yesterday_fund = Fund(yesterday_data)
        self.name = self.today_fund.name
        self.fund_code = self.today_fund.code
        self.url = self.today_fund.url
        self.current_price_diff = self.today_fund.current_price - self.yesterday_fund.current_price
        self.benefit = (self.today_fund.current_price - self.today_fund.purchase_price) * self.today_fund.count
        self.current_price_color = self.diff_color(self.current_price_diff)
        self.benefit_color = self.diff_color(self.benefit)

    @staticmethod
    def diff_color(value):
        if value > 0:
            return "blue"
        elif value < 0:
            return "red"
        else:
            return "gray"

    def get_fund_detail_data(self):
        fund_detail_data = {"name": self.name, "code": self.fund_code, "today_price": self.today_fund.current_price,
                            "price_diff": self.current_price_diff, "count": self.today_fund.count,
                            "purchase_price": self.today_fund.purchase_price, "benefit": self.benefit}
        return fund_detail_data


class Fund:
    def __init__(self, data):
        self.current_price = data["current_price"]
        self.count = data["count"]
        self.code = data["fund_code"]
        self.purchase_price = data["purchase_price"]
        self.name = data["fund_name"]
        self.url = data["fund_url"]
