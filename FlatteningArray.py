class ButtonAssignment:
    def __init__(self, arr):
        self.arr_new = arr

    #Method to flatten the input array
    def flatten(self, arr):
        for values in arr:
            if type(values) == list:
                self.flatten(values)
            elif not values == None:
                self.arr_new.append(values)
        return self.arr_new

#Input Array
arr =[0, 2, [[2, 3], 8, 100, None, [[None]]], -2]

#Output Array
arr_new =[]

obj = ButtonAssignment(arr_new)
arr_new = obj.flatten(arr)

#To print the output array
print("Flatten Array: ", arr_new)

