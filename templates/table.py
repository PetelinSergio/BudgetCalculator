def generate_table(budget: list) -> str:
    '''Input budget list and return string for table generating for html'''
    table = ''

    for i in range(len(budget[0])):
        table += f'<tr><td>{budget[0][i]}</td> \
        <td>{budget[1][i]}</td> \
        <td>{budget[2][i]}</td> \
        <td>{budget[3][i]}</td> \
        <td>{budget[4][i]}</td> \
        <td>{budget[5][i]}</td> \
        <td>{budget[6][i]}</td> \
        <td>{budget[7][i]}</td></tr>'


    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Калькулятор бюджета</title>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>>
        </head>
        <body>
            <table border="1">
            <caption>Таблица бюджета</caption>
            <tr>
                <th>№</th>
                <th>Год</th>
                <th>Месяц</th>
                <th>Доход</th>
                <th>Расход</th>
                <th>Итог</th>
                <th>Накопление</th>
                <th>Долг</th>
            </tr>
            {table}
            </table>
        </body>
    </html>
    '''