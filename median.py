def median(lista):
    sorted_lista = sorted(lista)
    print sorted(lista)
    if len(lista) % 2 == 0:
        middle_index_even = len(lista)/2
        index_for_median_even = middle_index_even -1
        print "index_for_median_even",index_for_median_even
        result = (sorted_lista[index_for_median_even] + sorted_lista[index_for_median_even+1])/2.0

    else:
        print "len:",len(sorted_lista)
        middle_index_odd = len(lista)/2
        print "middle_index_odd", middle_index_odd
        index_for_median_odd = middle_index_odd
        result = sorted_lista[index_for_median_odd]

    return result

print median([6, 8, 12, 2, 23])