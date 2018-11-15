def get_even_list(l):
    evenNumber = []
    for i in l:
        if i % 2 == 0:
            evenNumber.append(i) 
        else:
            pass
    return evenNumber
even_number = get_even_list([1,4,5,-1,10]) 
print(even_number) 