'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update
the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
'''
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class MyHashMap(object):
    def __init__(self):
        self.size = 2069
        self.hashTable = [Bucket() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hashKey = key % self.size
        self.hashTable[hashKey].update(key, value)

    def get(self, key: int) -> int:
        hashKey = key % self.size
        return self.hashTable[hashKey].get(key)

    def remove(self, key):
        hashKey = key % self.size
        self.hashTable[hashKey].remove(key)

# class ListNode(object):
#     def __init__(self, key):
#         self.key = key
#         self.val = None
#         self.next = None

# class MyHashMap:

#     def __init__(self):
#         self.size = 1000
#         self.bucket = [ListNode(-1) for _ in range(self.size)]

#     def put(self, key: int, value: int) -> None:

#         hashKey = self.hashCode(key)
#         head = self.bucket[hashKey]
#         current = head.next

#         while current:
#             if current.key == key: break
#             current = current.next
#         else:
#             current = ListNode(key)
#             current.next = head.next
#             head.next = current
#         current.val = value

#     def get(self, key: int) -> int:

#         hashKey = self.hashCode(key)
#         head = self.bucket[hashKey]
#         current = head.next

#         while current:
#             if current.key == key: break
#             current = current.next
#         else:
#             return -1
#         return current.val

#     def remove(self, key: int) -> None:
#         hashKey = self.hashCode(key)
#         current = self.bucket[hashKey]

#         while current and current.next:
#             if current.key == key: break
#             current = current.next
#         else:
#             return None
#         current.next = current.next.next

#     def hashCode(self, key):
#         return key % self.size