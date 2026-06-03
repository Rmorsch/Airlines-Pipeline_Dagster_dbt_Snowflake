# airlines-pipeline\src\airlines_pipeline\defs\assets\stock_prices.py
import dagster as dg
import os
from dagster_snowflake import SnowflakeResource
import finnhub
from datetime import datetime
import requests


@dg.asset()
def aal_stock_price(
    context: dg.AssetExecutionContext,
    snowflake: SnowflakeResource
):
    """"
        Fetches the current stock price of American Airlines (AAL) using the Finnhub API.
    """
    client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))
    stock_price = client.quote("AAL")["c"]

    context.log.info(f"Current AAL stock price: {stock_price} at {datetime.now()}")

    query = f"""
        INSERT INTO RAW.AAL_STOCK_PRICES (COMPANY, STOCK_PRICE)
        VALUES ('AAL', {stock_price})
    """

    with snowflake.get_connection() as conn:
        conn.cursor().execute(query)

@dg.asset()
def ual_stock_price(
    context: dg.AssetExecutionContext,
    snowflake: SnowflakeResource
):
    """"
        Fetches the current stock price of United Airlines (UAL) using the Alpha Vantage API.
    """
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    company = "UAL"
    
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={company}&apikey={os.getenv("ALPHA_VANTAGE_API_KEY")}'
    r = requests.get(url)
    data = r.json()

    context.log.info(f"INFO - What the json data looks like: {data}")

    stock_price = data["Global Quote"]["05. price"]

    context.log.info(f"INFO - Current UAL stock price: {stock_price} at {datetime.now()}")

    query = f"""
        INSERT INTO RAW.UAL_STOCK_PRICES (COMPANY, STOCK_PRICE)
        VALUES ('UAL', {stock_price})
    """

    with snowflake.get_connection() as conn:
        conn.cursor().execute(query)