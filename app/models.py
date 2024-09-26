from pydantic import BaseModel
from typing import List

class CountryData(BaseModel):
    name: str
    avg_monthly_salary: float
    cost_of_living: float
    combined_monthly_rent: float
    avg_home_price: float
    avg_monthly_mortgage: float
    monthly_food_expenses: float
    transport_expenses: float
    car_insurance: float
    healthcare_costs_with_insurance: float
    healthcare_costs_without_insurance: float
    monthly_health_insurance: float
    cost_of_university: float
    crime_rate: float
    high_school_graduation_rate: float
    pisa_score: float
    freedom_score: float
    economic_freedom: float
    press_freedom: float
    political_divide: float
    protests_per_100k: float

class ComparisonRequest(BaseModel):
    countries: List[str]
