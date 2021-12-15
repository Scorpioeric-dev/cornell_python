# monthly expenses and revenues over course of year
expenses = [40000., 42500., 47000., 40500., 38000., 36000., 39500., 43000., 47000., 48500., 49000., 50000.]
# print(expenses)

revenues = [38000., 42500., 52000., 50000., 48000., 43000., 44500., 45000., 50000., 49500., 52000., 54000.]
# print(revenues)

monthly_gross = [revenues[i] - expenses[i] for i in range(12)]


# print(monthly_gross)


def mean(x):
    """
    return the mean value of the elements in x
    by summing the elements and dividing by the length;
    if the input type does not support this,
    return the input itself
    """
    try:
        return sum(x) / len(x)
    except TypeError:
        return x


print(mean(expenses))
print(mean(revenues))


# Grabbing Quarterly values
# print(mean(expenses[0:3]))


def compute_quarterly_figures(expenses, revenues):
    quarterlies = {}
    for quarter in [1, 2, 3, 4]:
        start = (quarter - 1) * 3
        end = start + 3
        total_expenses_qtr = sum(expenses[start:end])
        mean_expenses = mean(expenses[start:end])
        total_revenues_qtr = sum(revenues[start:end])
        mean_revenues = mean(revenues[start:end])
        total_gross_qtr = total_revenues_qtr - total_expenses_qtr
        summary = 'Q{}: rev = {:.2f}, exp = {:.2f}, gross = {:.2f}'
        summary_line = summary.format(
            quarter, mean_revenues, mean_expenses, total_gross_qtr)

        print(summary_line)

        quarterlies['Q{0}'.format(quarter)] = \
            (mean_revenues, mean_expenses, total_gross_qtr)

    return quarterlies


quarterlies = compute_quarterly_figures(expenses, revenues)
# print(quarterlies)


# balance = 100.0
# rate = 0.03
# #
# print(0, round(balance, 2))
# for n in range(1, 11):
#     balance = round(balance * (1 + rate), 2)
#     print(n, round(balance, 2))


rate = 0.03


def compound(balance, rate, num_periods):
    # print(0, round(balance, 2))
    for n in range(1, num_periods + 1):
        balance = round(balance * (1 + rate), 2)
        # print(balance[-1])
        print(n, round(balance, 2))


print(compound(100, 0.03, 10))


# balance = 1
# rate = 1


def compound_by_period(balance, rate, num_periods):
    # print(0, round(balance, 2))
    balances = [balance]
    for n in range(1, num_periods + 1):
        balance = round(balance * (1 + rate), 2)
        balances.append(balance)
    return balances


print(compound_by_period(0.01, 1, 30))
total = compound_by_period(0.01, 1, 30)

print(total.pop())

mylist = compound_by_period(100, 0.03, 10)
# print(mylist)


def change_per_period(mylist):
    new_list = []
    for index, value in enumerate(mylist):
        print(index, value)
    if index + 1 == len(mylist):
        pass
    else:
        diff = mylist[index + 1] - mylist[index]
        new_list.append(diff)
    return new_list


# print(change_per_period(mylist))


# wheat challenge answers
wheat = compound_by_period(1, 1, 63)
# print(wheat)

total_wheat = sum(wheat)
# print(total_wheat)

# print(wheat)
# total_wheat = sum(wheat)
# print(total_wheat)

# compound_by_period

# balance=1
# rate=1

# wheat = compound_by_period(1,1,63)
# total_wheat= sum(wheat)
# compound_by_period
