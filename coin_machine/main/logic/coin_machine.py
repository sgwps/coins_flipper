import random
from .fraction import Fraction

class CoinMachine:

    def __init__(self, coins_for_one_exp: int, number_of_exits_to_cont: int, number_of_exits_event_happened: int):
        if coins_for_one_exp < 1:
            raise ValueError("Bad number of coins")
        self.coin_count = coins_for_one_exp
        max_number = 2 ** coins_for_one_exp
        if number_of_exits_to_cont + number_of_exits_event_happened > max_number:
            raise ValueError("Bad numbers")
        if number_of_exits_to_cont + number_of_exits_event_happened >= max_number:
            raise ValueError("Probability is const")
        exits_list = random.sample(range(2 ** coins_for_one_exp), number_of_exits_to_cont + number_of_exits_event_happened)
        self.exits_to_continue = exits_list[:number_of_exits_to_cont]
        self.exits_event_happened = exits_list[number_of_exits_to_cont:]


    def description(self):
        return 'Автомат за раз подбрасывает {} монет. В случае выпадания одного из {} исходов, подбрасывания продолжаются. В случае выпадания одного из {} других исходов, считается, что событие произошло. Иначе - событие не произошло'.\
        format(self.coin_count, len(self.exits_to_continue), len(self.exits_event_happened))
    
    def conduct(self):
        res = random.randint(0, 2 ** self.coin_count)
        while res in self.exits_to_continue:
            res = random.randint(0, 2 ** self.coin_count)
        if res in self.exits_event_happened:
            return True
        return False
    
    def probability_by_formula(self):
        x = 2 ** self.coin_count
        return Fraction(len(self.exits_event_happened), x - len(self.exits_to_continue))


    def try_experiments(self, number: int):
        result = []
        for i in range(number):
            result.append(self.conduct())
        good_exits = result.count(True)
        return good_exits / number