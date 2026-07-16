"""
Company data model.

This module will represent a public company and its
financial statements, market data, and valuation metrics.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Company:
    """
    Represents a publicly listed company.
    """

    ticker: str
    name: str

    exchange: Optional[str] = None
    currency: Optional[str] = None
    country: Optional[str] = None

    sector: Optional[str] = None
    industry: Optional[str] = None

    website: Optional[str] = None
    business_summary: Optional[str] = None

    current_price: Optional[float] = None
    market_cap: Optional[float] = None
    enterprise_value: Optional[float] = None

    beta: Optional[float] = None

    shares_outstanding: Optional[int] = None

    pe_ratio: Optional[float] = None

    dividend_yield: Optional[float] = None