import ctypes, sys

class DynamicArray(object):

    def __init__(self) -> None:

        self.count = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        
        return self.count

    def __getitem__(self, index):

        if not 0 <= index < self.count:
            return IndexError("index is out of range.")
        
        return self.A[index]
    
    def append(self, element):

        if self.count == self.capacity:
            # print("append: inside if")
            self._resize(2 * self.capacity)

        # print(f"inside append: after if, count: {self.count}")
        self.A[self.count] = element
        self.count += 1
    
    def _resize(self, capacity):

        # print("inside _resize")
        B = self.make_array(capacity)

        for index in range(self.count):
            B[index] = self.A[index]

        self.A = B
        self.capacity = capacity
        # print(f"count: {self.count}, capacity: {self.capacity}")
    
    def make_array(self, capacity):

        return (capacity * ctypes.py_object)()
        

# array = DynamicArray()
array = list()

# print(f"count: {array.count}, capacity: {array.capacity}")

# array.append("a")
# array_size = sys.getsizeof(array)
# print(f"array_2[0]: {array[0]}")
# print(f"count: {array.count}, capacity: {array.capacity}, array_size: {array_size}")

# array.append("b")
# array_size = sys.getsizeof(array)
# print(f"array_2[1]: {array[1]}")
# print(f"count: {array.count}, capacity: {array.capacity}, array_size: {array_size}")

# array.append("c")
# array_size = sys.getsizeof(array)
# print(f"array_2[2]: {array[2]}")
# print(f"count: {array.count}, capacity: {array.capacity}, array_size: {array_size}")

# array.append("d")
# array_size = sys.getsizeof(array)
# print(f"array_2[3]: {array[3]}")
# print(f"count: {array.count}, capacity: {array.capacity}, array_size: {array_size}")

# array.append("e")
# print(f"array_2[4]: {array[4]}")
# array_size = sys.getsizeof(array)
# print(f"count: {array.count}, capacity: {array.capacity}, array_size: {array_size}")

# print(f"length array_2: {len(array)}")

n = 10

for i in range(n):

    count = len(array)
    # capacity = array.capacity
    array_size = sys.getsizeof(array)

    # print(f"count: {count}, capacity: {capacity}, array_size: {array_size}")
    print(f"count: {count}, array_size: {array_size}")

    array.append(n)