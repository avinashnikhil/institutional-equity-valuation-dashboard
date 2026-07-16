import yfinance as yf

from src.models.company import Company


class MarketDataService:
    """
    Service responsible for fetching market data
    from Yahoo Finance.
    """

    def get_company(self, ticker: str) -> Company:
        """
        Fetch company information from Yahoo Finance.
        """

        stock = yf.Ticker(ticker)

        info = stock.info

        company = Company(
            ticker=ticker.upper(),
            name=info.get("longName", "Unknown Company"),
            exchange=info.get("exchange"),
            currency=info.get("currency"),
            country=info.get("country"),
            sector=info.get("sector"),
            industry=info.get("industry"),
            website=info.get("website"),
            business_summary=info.get("longBusinessSummary"),
            current_price=info.get("currentPrice"),
            market_cap=info.get("marketCap"),
            enterprise_value=info.get("enterpriseValue"),
            beta=info.get("beta"),
            shares_outstanding=info.get("sharesOutstanding"),
            pe_ratio=info.get("trailingPE"),
            dividend_yield=info.get("dividendYield"),
        )

        return company