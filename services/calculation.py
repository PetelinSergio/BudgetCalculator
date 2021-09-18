import datetime
from typing import List
from dateutil.relativedelta import relativedelta


def diff_month(date_1: datetime.date, date_2: datetime.date) -> int:
    '''Returns number of month between date_2 and date_1'''
    
    if date_1.year == date_2.year:
        return date_2.month - date_1.month + 1
    elif date_2.year -  date_1.year == 1:
        return (12 - date_1.month) + date_2.month
    else:
        return (12 - date_1.month) + date_2.month + (date_2.year -  date_1.year - 1) * 12
    
def budget_calc(start_date: datetime.date, final_date: datetime.date, income: float, cost: float) -> list:
    '''Returns list with calculated budget by month'''

    calc_period = diff_month(start_date, final_date)
    current_calc_date = start_date

    years_list = list()
    month_list = list()
    income_list = list()
    cost_list = list()
    diff_list = list()
    money_accumulation_list = list()
    debt_list = list()

    years_list.append(start_date.year)
    month_list.append(start_date.month)
    income_list.append(income)
    cost_list.append(cost)
    diff = income - cost
    diff_list.append(diff)
    if diff >= 0:
        money_accumulation_list.append(diff)
        debt_list.append(0)
    else:
        money_accumulation_list.append(0)
        debt_list.append(-1 * diff)

    current_calc_date += relativedelta(months=1)

    for i_month in range(1, calc_period):
        years_list.append(current_calc_date.year)
        month_list.append(current_calc_date.month)
        income_list.append(income)
        cost_list.append(cost)
        diff = income - cost
        diff_list.append(diff)

        if debt_list[i_month - 1] > 0:
            debt_list.append(debt_list[i_month - 1] - diff)
            if debt_list[i_month] < 0:
                money_accumulation_list.append(debt_list[i_month])
                debt_list[i_month] = 0
            else:
                money_accumulation_list.append(0)
        else:                
            money_accumulation_list.append(money_accumulation_list[i_month - 1] + diff)
            if money_accumulation_list[i_month] < 0:
                debt_list.append(-1 * money_accumulation_list[i_month])
                money_accumulation_list[i_month] = 0
            else:
                debt_list.append(0)
                
        current_calc_date += relativedelta(months=1)

    budget = [list(range(calc_period)), 
        years_list, 
        month_list, 
        income_list,
        cost_list,
        diff_list,
        money_accumulation_list,
        debt_list]

    return budget
