from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models import ComparisonRequest
from app.utils import get_country_data, generate_comparison_table, generate_comparison_chart

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/compare")
async def compare(request: Request, countries: str = Form(...)):
    country_list = [country.strip() for country in countries.split(',')]
    comparison_request = ComparisonRequest(countries=country_list)
    
    country_data = [get_country_data(country) for country in comparison_request.countries]
    comparison_table = generate_comparison_table(country_data)
    comparison_chart = generate_comparison_chart(country_data)
    
    return templates.TemplateResponse("comparison.html", {
        "request": request,
        "comparison_table": comparison_table,
        "comparison_chart": comparison_chart
    })
