
# def mean(lst):
#     sum(lst / len(lst))

def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

print(mean(a, trim_by=0))
print(mean(a, trim_by=1))