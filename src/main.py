from coin_change import CoinChange

message_input_1 = 'Please enter number of denomination (N) and value of money (M): '
message_input_2 = 'Please enter {} denominations in decreasing order: '
message_input_3 = '(Re-enter) Please enter {} denominations in decreasing order: '


def input_validation(num_denomination, denomination):
    return not (num_denomination == len(denomination) and sorted(denomination, reverse=True) == denomination)


def to_intlist(list_item):
    return list(map(int, list_item))


def make_change(num_denomination, money, denomination):
    coin = CoinChange(num_denomination, money, denomination)
    min_coin = coin.get_smallest_coin()
    print(f'Smallest number of notes and coins is {len(min_coin)}.')


def main():
    num_denomination, money = to_intlist(input(message_input_1).split())
    denomination = to_intlist(
        input(message_input_2.format(num_denomination)).split())
    while input_validation(num_denomination, denomination):
        denomination = to_intlist(
            input(message_input_3.format(num_denomination)).split())
    make_change(num_denomination, money, denomination)


if __name__ == '__main__':
    main()
