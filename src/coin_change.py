class CoinChange:
    def __init__(self, num_denomination, money, denomination):
        self.num_denomination = num_denomination
        self.money = money
        self.denomination = self._cut_coin_not_compute(denomination)

    def _cut_coin_not_compute(self, denomination):
        money = self.money
        for coin in denomination:
            if money % coin == money:
                denomination.remove(coin)
        return denomination

    def get_smallest_coin(self):
        cal = self._make_change(self.money, self.denomination, [])
        results = [result for result in cal]
        return min(results, key=len)

    def _make_change(self, money, denomination, posible_coin):
        if sum(posible_coin) == money:
            yield posible_coin
        elif sum(posible_coin) > money:
            pass
        elif denomination == []:
            pass
        else:
            for posible in self._make_change(money, denomination[:], posible_coin + [denomination[0]]):
                yield posible
            for posible in self._make_change(money, denomination[1:], posible_coin):
                yield posible
