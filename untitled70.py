def remove_empty_arrays(arr):
    new = []
    for i in arr:
        if len(i) != 0:
            new.append()
            return new
 

test_input = ["a", "b", [], [], [1, 2, 3]]
test_result = remove_empty_arrays(test_input)
print(test_result)
        
