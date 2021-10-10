# does not uses classes and has one less check

def sort_in_place(array_given, number_to_move):
    first_pointer = 0
    second_pointer = len(array_given) - 1

    while first_pointer < second_pointer:

        while array_given[second_pointer] == number_to_move and second_pointer > first_pointer:

            second_pointer -= 1

            if array_given[first_pointer] == number_to_move:
                array_given[first_pointer], array_given[second_pointer] = array_given[second_pointer], array_given[
                    first_pointer]

        first_pointer += 1

    return array_given


array = [2, 1, 2, 2, 2, 3, 4, 2]
element_to_move = 2

print("original: ", array)

results = sort_in_place(array, element_to_move)

print("now: ", results)
