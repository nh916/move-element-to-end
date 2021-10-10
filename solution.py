# space O(1) because no data structures are used
# runs in o(n) because looping
def sort_in_place(self, array_given, number_to_move):
    first_pointer = 0
    second_pointer = len(array_given) - 1

    while first_pointer < len(array_given) - 1:

        while array_given[first_pointer] == number_to_move and second_pointer > first_pointer:
            if array_given[first_pointer] == number_to_move and array_given[second_pointer] != number_to_move:
                array_given[first_pointer], array_given[second_pointer] = array_given[second_pointer], array_given[
                    first_pointer]

            second_pointer -= 1

        first_pointer += 1

    return array_given


array = [2, 1, 2, 2, 2, 3, 4, 2]
element_to_move = 2

print("original: ", array)

results = sort_in_place(array, element_to_move)

print("now: ", results)
