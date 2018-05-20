
work_days_N = int(input())
average_day_earnings_M = float(input())
usd_to_bgl = float(input())

monthly_earnings = work_days_N * average_day_earnings_M
yearly_earnings = monthly_earnings * 12 + monthly_earnings * 2.5
tax = 0.25 * yearly_earnings
final_yearly_earnings = yearly_earnings - tax
yearly_earnings_in_bgl = final_yearly_earnings * usd_to_bgl

final_day_earnings = yearly_earnings_in_bgl / 365

print("%.2f" % final_day_earnings)
