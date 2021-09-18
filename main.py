from datetime import date
from fastapi import FastAPI, Form
from fastapi.responses import Response
import services.calculation
import templates.table


app = FastAPI()


@app.get("/")
def index_page():
    with open('templates/index.html', 'r') as f:
        index_page = f.read()
    return Response(index_page, media_type="text/html")

@app.post("/budget")
def budget_calc(
    income: float = Form(...), 
    cost: float = Form(...), 
    start_date: date = Form(...), 
    final_date: date = Form(...)):
    
    table_page = templates.table.generate_table(services.calculation.budget_calc(start_date, final_date, income, cost))
    
    with open('test.html', 'w') as f:
        f.writelines(table_page)

    return Response(table_page, media_type="text/html")
