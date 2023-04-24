# numbers = [1, 12, 2, 13, 3, 14, 4, 15, 5, 16, 6, 17, 7, 19, 8, 20, 9, 21, 10]
# text = ["cat", "dog", "elephant", "owl", "fish", "hamster", "crocodile", "bee", "dear"]

# QUESTION NR 1
def selection_sort(numbers: list):
    #  loop over list in reverse order = range 18 to 0, -1 to step backwards
    for fill_slot in range(len(numbers) - 1, 0, -1):
        position_of_max = fill_slot
        # fill_slot +1 = where unsorted part of list starts
        for location in range(fill_slot + 1):
            # check if new position is bigger than other one
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        # swap the biggest number with last element of the unsorted list part that is left
        else:
            numbers[fill_slot], numbers[position_of_max] = numbers[position_of_max], numbers[fill_slot]
    return numbers


# QUESTION NR 2
def binary_search(text: list, target: str):
    first = 0
    last = len(text) - 1
    while first <= last:
        # calculate middle of list
        mid = (first + last) // 2
        if target not in text:
            return
        elif text[mid] == target:
            return text[mid]
        # only search upper half of list
        elif text[mid] < target:
            first = mid + 1
        else:
            # only search lower half of the list
            last = mid - 1
    return target


# QUESTION NR 3, 4, 5, 6
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def __my_hash(self, key):
        if key.type() == str:
            key = len(key)
        return key % self.size

    def put(self, key, data):
        hash_key = self.__my_hash(self.key)  # or len(self.slots)
        if self.slot[hash_key] is None:
            self.slot[hash_key] = key
            self.data[hash_key] = data
        else:
            if self.slot[hash_key] is key:
                # if slot is empty put data in:
                self.data[hash_key] = data
            else:
                if type(self.slot[hash_key]) == list:
                    if key in self.slot[hash_key]:
                        # update data on given index if it was already taken
                        index = self.slot[hash_key].index(key)
                        self.data[hash_key][index] = data
                    else:
                        # if key not in list in slot
                        self.slot[hash_key].append(key)
                        self.data[hash_key].append(data)
                else:
                    self.slot[hash_key] = [self.slot[hash_key], key]
                    self.data[hash_key] = [self.data[hash_key], data]

    def get(self, key):
        hash_key = self.__my_hash(key)
        if slef.slot[hash_key] is None:
            return None
        if self.slot[hash_key] is key:
            return self.data[hash_key]
        else:
            if key in self.slot[hash_key]:
                index = self.slot[hash_key].index(key)
                return self.data[hash_key][index]
            else:
                return None
