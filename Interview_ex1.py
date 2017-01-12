#example 1

a_list = [1,2,3,4,5,1,2,3,7,1,7,6]

def dup(ex_list):
    for val in a_list:
        for other_val in a_list:
            if val == other_val:
                del other_val
    return ex_list

dup(a_list)
