import pandas as pd

income1 = pd.DataFrame({'Names': ['Stephen', 'Camilla', 'Tom'],
                'Salary':[100000, 70000, 60000]})

income2 = pd.DataFrame({'Names': ['Pete', 'April', 'Marty'],
                'Salary':[120000, 110000, 50000]})

income3 = pd.DataFrame({'Names': ['Victor', 'Victoria', 'Jennifer'],
                'Salary':[75000, 90000, 40000]})

income_sheets = {'Group1': income1, 'Group2': income2, 'Group3': income3}

for sheet_name in income_sheets.keys():
    income_sheets[sheet_name].to_excel('./income.xlsx', engine='xlsxwriter', sheet_name=sheet_name, index=False)
