def stat(strg):

    # Its better if we import this known library.
    import numpy as np

    # As well as the rules says, if the string is empty we will return another empty.
    if strg == '':
        return ''

    # We split the numbers that there are between commas.
    sep = strg.split(',')

    # This loop is interesting.
    # First we will use each element in our list 'sep' and we will split the numbers that there are between forward slash again.
    # After this we will convert each string number in an integer number and depending the position in the list we will multiply it by 3600, 60 or 1.
    # This is useful because after that we will sum every number and we will have every time converted in seconds to be able to use better.
    add_list = list()

    for i in sep:

        sep2 = i.split('|')

        add = list()

        for j in range(len(sep2)):

            if j == 0:

                add.append(int(sep2[j])*3600)

            elif j == 1:

                add.append(int(sep2[j])*60)

            else:

                add.append(int(sep2[j]))

        add = sum(add)

        add_list.append(add)

    # This is simple, we will calculate the range, the average and the median.
    range2 = max(add_list)-min(add_list)
    average = np.mean(add_list)

    # Ordering is to calculate the median.
    ord_list = sorted(add_list)

    # CAUTION. If the list has a even number of elements, we will have to use the two in the middle and calculate the average between both.
    if len(add_list) % 2 != 0:

        med = ord_list[int(
            (len(add_list)/2))]

    else:

        med = (ord_list[int((len(add_list)/2))] +
               ord_list[int((len(add_list)/2))-1])/2

    # Here we will transform each number of the range, the average and the median in the first time format.
    hour_average = int(average/3600)
    minute_average = int(
        (average-(hour_average * 3600))/60)
    seconds_average = int(
        average-(hour_average*3600)-(minute_average*60))

    hour_range = int(range2/3600)
    minute_range = int(
        (range2-(hour_range * 3600))/60)
    seconds_range = int(
        range2-(hour_range*3600)-(minute_range*60))

    hour_med = int(med/3600)
    minute_med = int(
        (med-(hour_med * 3600))/60)
    seconds_med = int(
        med-(hour_med*3600)-(minute_med*60))

    # And finally we will express everything as well as the statement says.
    # Using the .zfill(2) comand to fill each number with zeros if we have only one number. The rules requiered that.
    result = "Range: "+str(hour_range).zfill(2)+"|"+str(minute_range).zfill(2)+"|"+str(seconds_range).zfill(2)+" Average: "+str(hour_average).zfill(2)+"|"+str(
        minute_average).zfill(2)+"|"+str(seconds_average).zfill(2)+" Median: "+str(hour_med).zfill(2)+"|"+str(minute_med).zfill(2)+"|"+str(seconds_med).zfill(2)

    return result
