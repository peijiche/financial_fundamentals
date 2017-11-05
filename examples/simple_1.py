import pandas as pd
import financial_fundamentals.accounting_metrics as ff

date_range = pd.date_range('2012-1-1', '2013-12-31')
required_data = pd.DataFrame(columns=['MSFT', 'GOOG', 'YHOO', 'IBM'], index=date_range)

eps = ff.earnings_per_share(required_data)
print eps
