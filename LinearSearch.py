class LinearSearch:
    def __init__(self, arr):
        self.arr = arr
        

    def search(self,target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i  # Return the index of the target element
        return -1  # Return -1 if the target is not found


# Example usage
my_list = [5, 3, 8, 4, 2]
target_element = int(input('enter the element you want to search :'))

search_obj = LinearSearch(my_list)
index = search_obj.search(target_element)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")