# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    def check_one_element(index):
        if index == len(array):
            return False
        elif array[index] == query:
            return True
        
        return check_one_element(index+1)
    
    return check_one_element(0)


# is_palindrome
def is_palindrome(text):
    def check_chars(for_index, back_index):
        if for_index >= back_index:
            return True
        elif text[for_index] != text[back_index]:
            return False
        
        return check_chars(for_index+1, back_index-1)
    
    return check_chars(0, len(text)-1)


# digit_match
def digit_match(num_1, num_2):
    num_1 = str(num_1)
    num_2 = str(num_2)
    
    def count_matches(index_1, index_2, counter):
        if index_1 < 0 or index_2 < 0:
            return counter
        
        if num_1[index_1] == num_2[index_2]:
            counter += 1
        
        return count_matches(index_1 - 1, index_2 - 1, counter)
    
    return count_matches(len(num_1) - 1, len(num_2) - 1, 0)

# digit match without casting int to str
def digit_match(num_1, num_2):
    if num_1 == 0 and num_2 == 0:
        return 1

    def count_matches(n1, n2):
        if n1 == 0 or n2 == 0:
            return 0

        if n1 % 10 == n2 % 10:
            count = 1
        else:
            count = 0

        return count + count_matches(n1 // 10, n2 // 10)

    return count_matches(num_1, num_2)