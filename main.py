from src.data.market_data import MarketDataService

service = MarketDataService()

company = service.get_company("AAPL")

print("=" * 50)
print(f"Company: {company.name}")
print(f"Ticker: {company.ticker}")
print(f"Sector: {company.sector}")
print(f"Industry: {company.industry}")
print(f"Current Price: {company.current_price}")
print(f"Market Cap: {company.market_cap}")
print(f"PE Ratio: {company.pe_ratio}")
print("=" * 50)