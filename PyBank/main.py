


fp = open("PyBank/Resources/budget_data.csv")
lines = [entry.strip().split(',') for entry in fp.readlines()][1:]
total_months = len(lines)
total = 0

change = [0 for i in range(total_months)]
for i in range(1, total_months):
    profit = int(lines[i][1])
    profit_1  = int(lines[i-1][1])
    change[i] = profit - profit_1

    total += profit_1


total += int(lines[-1][1])
average_change = 0

profit_inc_month_change = 0
profit_dec_month_change = 0
profit_inc_month_date = ''
profit_dec_month_date = ''

for i in range(total_months):
    average_change += change[i]
    if(profit_inc_month_change <= change[i]):
        profit_inc_month_change = change[i]
        profit_inc_month_date = lines[i][0]
    if(profit_dec_month_change >= change[i]):
        profit_dec_month_change = change[i]
        profit_dec_month_date = lines[i][0]

print(f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${average_change / total_months: 0.2f}
Greatest Increase in Profits: {profit_inc_month_date} (${profit_inc_month_change})
Greatest Decrease in Profits: {profit_dec_month_date} (${profit_dec_month_change})

""")