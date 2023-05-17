#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_avg = total_sum / total_weight
    return weighted_avg
