class CoinChange:
    def __init__(self, num_denomination, money, denomination):
        self.num_denomination = num_denomination
        self.money = money
        self.denomination = self.cut_coin_not_compute(denomination)

    def cut_coin_not_compute(self, denomination):
        money = self.money
        for coin in denomination:
            if money % coin == money:
                denomination.remove(coin)
        return denomination

    def get_smallest_coin(self):
        results = [result for result in self.cal(
            self.money, self.denomination, [])]
        return min(results, key=len)

    def cal(self, money, denomination, posible_coin):
        if sum(posible_coin) == money:
            yield posible_coin
        elif sum(posible_coin) > money:
            pass
        elif denomination == []:
            pass
        else:
            for posible in self.cal(money, denomination[:], posible_coin + [denomination[0]]):
                yield posible
            for posible in self.cal(money, denomination[1:], posible_coin):
                yield posible
