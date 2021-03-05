# Create an algorithm that can detect if an input string has two letters that are separated by EXACTLY N characters, and returns the two indices 
# if it finds such a case. Otherwise, return None.

# Example: If given and input string of "My name is Earl", two input characters "a" and "s", and a numeric value of "4" ... 
# your function should return "[4,9]" because "a" and "s" are separated by EXACTLY 4 characters somewhere in the input string (index 4 "a" & index 9 "s")


def letter_spacing(input_string, first_char, second_char, desired_spacing_value):
    my_arr = []
    count = 0
    f_index = input_string.index(first_char)
    s_index = input_string.index(second_char)
    for i in range(f_index,s_index):
        if i != s_index - 1:
            count += 1
        else:
            break
    if count == desired_spacing_value:
        return [f_index,s_index]
    else:
        return None


result = letter_spacing("My name is Earl", "a", "s", 4)
print(result) # should print out [4,9] (or [9,4])