from typing import Callable, List, Tuple


class monkey:
    def __init__(self, starting_items: List[int], inspect_operation: Callable[[int], int],
                 test_divisor: int, true_throw: int, false_throw: int):
        self.items = starting_items
        self.inspect_operation = inspect_operation
        self.test_divisor = test_divisor
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.item_inspections = 0

    def catch_item(self, item: int):
        self.items.append(item)

    def inspect_item_and_throw(self) -> Tuple[int, int]:
        self.item_inspections += 1
        item = self.inspect_operation(self.items.pop(0)) # apply inspection worry
        item = item // 3 # relax a bit
        # return item and monkey to throw to
        return item, self.true_throw if item % self.test_divisor == 0 else self.false_throw

monkeys = [
    monkey([83, 62, 93], lambda x: x * 17, 2, 1, 6),
    monkey([90, 55], lambda x: x + 1, 17, 6, 3),
    monkey([91, 78, 80, 97, 79, 88], lambda x: x + 3, 19, 7, 5),
    monkey([64, 80, 83, 89, 59], lambda x: x + 5, 3, 7, 2),
    monkey([98, 92, 99, 51], lambda x: x * x, 5, 0, 1),
    monkey([68, 57, 95, 85, 98, 75, 98, 75], lambda x: x + 2, 13, 4, 0),
    monkey([74], lambda x: x + 4, 7, 3, 2),
    monkey([68, 64, 60, 68, 87, 80, 82], lambda x: x * 19, 11, 4, 5)
]

for i in range(20): # 20 rounds
    for m in monkeys:
        while m.items:
            item, throw_to = m.inspect_item_and_throw()
            monkeys[throw_to].catch_item(item)

most_active_monkeys = sorted([m.item_inspections for m in monkeys], reverse=True)
monkey_business = most_active_monkeys[0] * most_active_monkeys[1]

print(monkey_business)
