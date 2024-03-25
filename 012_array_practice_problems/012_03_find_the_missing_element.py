"""
Problem:

Consider an array of non-negative integers. A second array is formed by shuffling the elements of 
the first array and deleting a random element. Given these two arrays, find which element is missing in 
the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""

def finder(arr1, arr2):

    result: [int] = 0

    print(arr1 + arr2)
    for number in arr1 + arr2:

        print(f"number: {number}, result: {result}")
        result ^= number
        print(f"XOR result: {result}")

    return result

array1 = [5,5,7,7]
array2 = [5,7,7]

print(finder(array1, array2))

array3 = [1,2,3,5,6,7,4,24]
array4 = [3,7,2,5,1,4,6]

print(finder(array3, array4))
