def get_even_list(l):
    evenNumber = []
    for i in l:
        if i % 2 == 0:
            evenNumber.append(i) 
        else:
            pass
    return evenNumber
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
