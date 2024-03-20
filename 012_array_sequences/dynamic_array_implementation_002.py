import ctypes

class DynamicArray(object):
    '''
    # DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
    
    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        '''
        # Return number of elements sorted in array
        '''
        return self.n
    
    def __getitem__(self,k):
        '''
        # Return element at index k
        '''
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!') # Check it k index is in bounds of array
        
        return self.A[k] #Retrieve from array at index k
        
    def append(self, ele):
        '''
        # Add element to end of the array
        '''
        if self.n == self.capacity:
            self._resize(2*self.capacity) #Double capacity if not enough room
        
        self.A[self.n] = ele #Set self.n index to element
        self.n += 1
        
    def _resize(self,new_cap):
        '''
        # Resize internal array to capacity new_cap
        '''
        
        B = self.make_array(new_cap) # New bigger array
        
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
            
        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity
        
    def make_array(self,new_cap):
        '''
        # Returns a new array with new_cap capacity
        '''
        return (new_cap * ctypes.py_object)()
        

array = DynamicArray()

print(f"count: {array.n}, capacity: {array.capacity}")
array.append("a")
print(f"array_2[0]: {array[0]}")
print(f"count: {array.n}, capacity: {array.capacity}")
array.append("b")
print(f"array_2[1]: {array[1]}")
print(f"count: {array.n}, capacity: {array.capacity}")
array.append("c")
print(f"array_2[2]: {array[2]}")
print(f"count: {array.n}, capacity: {array.capacity}")

print(f"length array_2: {len(array)}")
