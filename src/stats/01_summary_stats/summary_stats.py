
# def mean(lst):
#     sum(lst / len(lst))

def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=0)) # 238.3
# print(mean(a, trim_by=1)) # 47.75
# print(mean(a, trim_by=2)) # 26.167



'''
Breakout

An article published in the journal, Indoor Air, considered two different air samples to 
test for endotoxin concentrations, the first in urban households, and the second in farmhouses.
Urban: 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
Farmhouse: 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3
'''

urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

'''
A. Determine the sample mean for each group.
'''
print(f'Sample Mean Urban: {mean(urban)}')