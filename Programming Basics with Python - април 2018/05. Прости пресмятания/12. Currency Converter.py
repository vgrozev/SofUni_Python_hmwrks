
bgn_const = 1
usd_const = 1.79549
eur_const = 1.95583
gbp_const = 2.53405

amount = float(input())

from_currency = input()
to_currency = input()


###########################################
# convert everything to BGN as a first step

if from_currency == 'USD':
    bgn_step = amount * usd_const

elif from_currency == 'EUR':
    bgn_step = amount * eur_const

elif from_currency == 'GBP':
    bgn_step = amount * gbp_const

else:
    bgn_step = amount


###########################################
# convert from BGN to output currency

if to_currency == 'USD':
    converted_amount = bgn_step / usd_const

elif to_currency == 'EUR':
    converted_amount = bgn_step / eur_const

elif to_currency == "GBP":
    converted_amount = bgn_step / gbp_const

else:
    converted_amount = bgn_step / bgn_const

print(round(converted_amount, 2), to_currency)




