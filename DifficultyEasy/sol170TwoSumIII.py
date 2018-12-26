"""
170. Two Sum III - Data structure design
Easy

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:
add(3); add(1); add(2);
find(3) -> true
find(6) -> false

    from DifficultyEasy.sol170TwoSumIII import TwoSum
    obj = TwoSum()
    obj.add(3)
    obj.add(1)
    obj.add(2)
    # obj.add(3)
    obj.printout()

    print("is sum of 3 exists? {}".format(obj.find(3)))
    print("is sum of 6 exists? {}".format(obj.find(6)))
    obj.clear()


"""


class TwoSum:

    val_map = {}

    def add(self, number):
        count = 0
        if number in self.val_map:
            count = self.val_map.get(number)
        self.val_map[number] = count + 1
        return

    def find(self, target):

        for k in self.val_map:
            y = target - k
            if y == k:
                if self.val_map.get(y) > 1: return True
            elif y in self.val_map:
                return True

        return False

    def clear(self):
        self.val_map.clear()
        return

    def printout(self):
        print(self.val_map)
        return