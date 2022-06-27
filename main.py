import matplotlib.pyplot
import data

REFERENCE_YEAR = 2000

incomeyears = data.INCOME.keys()
cpiyears = data.CPI.keys()
incomeamounts = [amount / data.INCOME[REFERENCE_YEAR] for amount in data.INCOME.values()]
cpiamounts = [amount / data.CPI[REFERENCE_YEAR] for amount in data.CPI.values()]
ratioyears = [year for year in incomeyears if year in cpiyears]
referenceratio = data.CPI[REFERENCE_YEAR] / data.INCOME[REFERENCE_YEAR]
ratios = [cpi / data.INCOME[year] / referenceratio for year, cpi in data.CPI.items() if year in incomeyears]

matplotlib.pyplot.plot(incomeyears, incomeamounts, label=f"income (ratio to year {REFERENCE_YEAR})", color='black', linewidth=1)
matplotlib.pyplot.plot(cpiyears, cpiamounts, label=f"cpi (ratio to year {REFERENCE_YEAR})", color='red', linewidth=1)
matplotlib.pyplot.plot(ratioyears, ratios, label=f"cpi divided by weekly income (ratio to year {REFERENCE_YEAR})", color='green', linewidth=4)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

