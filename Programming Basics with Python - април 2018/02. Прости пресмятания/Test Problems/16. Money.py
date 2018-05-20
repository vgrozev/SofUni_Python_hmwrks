num_btc = int(input())
num_cny = float(input())
fee = float(input())

btc_to_bgl = num_btc * 1168
cny_to_usd = num_cny * 0.15
usd_to_bgl = cny_to_usd * 1.76
total_bgl = btc_to_bgl + usd_to_bgl
total_eur = total_bgl / 1.95
total_fee = total_eur * (fee / 100)

final_amount = total_eur - total_fee

print("%.2f" % final_amount)

