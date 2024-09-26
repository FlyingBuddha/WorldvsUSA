import pandas as pd
import plotly.graph_objects as go
from app.models import CountryData

def get_country_data(country: str) -> CountryData:
    # In a real application, this would fetch data from a database or API
    # For this example, we'll return dummy data
    return CountryData(
        name=country,
        avg_monthly_salary=3000,
        cost_of_living=1500,
        combined_monthly_rent=1000,
        avg_home_price=300000,
        avg_monthly_mortgage=1500,
        monthly_food_expenses=400,
        transport_expenses=200,
        car_insurance=100,
        healthcare_costs_with_insurance=200,
        healthcare_costs_without_insurance=1000,
        monthly_health_insurance=300,
        cost_of_university=10000,
        crime_rate=5,
        high_school_graduation_rate=85,
        pisa_score=500,
        freedom_score=80,
        economic_freedom=75,
        press_freedom=70,
        political_divide=60,
        protests_per_100k=10
    )

def generate_comparison_table(country_data: list[CountryData]) -> str:
    df = pd.DataFrame([country.__dict__ for country in country_data])
    return df.to_html(classes="table table-striped table-responsive")

def generate_comparison_chart(country_data: list[CountryData]) -> str:
    fig = go.Figure()
    for country in country_data:
        fig.add_trace(go.Bar(
            x=list(country.__dict__.keys())[1:],
            y=list(country.__dict__.values())[1:],
            name=country.name
        ))
    fig.update_layout(
        title="Country Comparison",
        xaxis_title="Metrics",
        yaxis_title="Values",
        barmode='group'
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')
