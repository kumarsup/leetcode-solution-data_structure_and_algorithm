'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Solution:
Data Structure - Time O(1), Space- O(1).
    - insert
    - delete
    - random
Contraints-
    - 2^-31 <= val <= 2^31 - 1
    - At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
    - There will be at least one element in the data structure when getRandom is called.

    O(1) -
        - HashMap - elements - indexs
        - ArrayList - list of element
            - delete is a problem-
                - on delete- replace the item with last item in list and pop last - O(1)

    GetRandom-
         -

    - Insert:
        - We add the element to list and store the value -> index in hashmap
    - Delete-
        - Get the item index from hashmap
        - swap the item at index i with last index of list
        - update the new index of the last item in hashmap
        - pop the last item from the list
    - GetRandom -
        - pick any randome index between 0 and len(list)-1
        - return the item from i index
'''


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val is None: return False
        if val in self.hashmap: return False
        self.nums.append(val)
        self.hashmap[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashmap: return False

        lastItem, index = self.nums[-1], self.hashmap[val]
        self.nums[index], self.hashmap[lastItem] = lastItem, index
        del self.hashmap[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = randint(0, len(self.nums) - 1)
        return self.nums[rand]
