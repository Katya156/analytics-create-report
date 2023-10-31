import pandas as pd
import numpy as np
import datetime

statement_122 = pd.read_excel("./Выписки/Выписка122.xls")
statement_123 = pd.read_excel("./Выписки/Выписка123.xls")
uni = pd.read_csv("uni.csv", sep = ';', encoding='latin-1')

statements = pd.concat([statement_122, statement_123], axis = 0)
statements['Код авторизации'] = statements['Код авторизации'].replace("'", "")

authcode_id = dict(zip(np.array(uni['AuthCode']), np.array(uni['OrderID'])))
statements.insert(9, 'orderID', statements['Код авторизации'].map(authcode_id))

current_time = datetime.datetime.now()
current_time = current_time.strftime('%d.%m.%Y %H:%M')
statements.insert(9, "Время обработки", current_time)

statements.insert(11, "Комиссия", round(statements['Сумма операции'] * 0.0125, 2))

statements.insert(12, "Сумма к переводу", round(statements['Сумма операции'] - statements["Комиссия"], 2))

statements.to_excel('Итоговый_отчет.xlsx', index=False)



