from forex_python.converter import CurrencyRates
c= CurrencyRates()
r= c.convert("USD","BDT",1)
print(r)