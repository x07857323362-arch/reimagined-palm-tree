# Trading System API Documentation

## Overview

The Trading System provides three main API modules:
- **TradingAPI**: Order execution and position management
- **MarketAPI**: Real-time market data
- **AnalysisAPI**: Strategy backtesting and analysis

## TradingAPI

### Methods

#### place_order(symbol, side, amount, price=None)
Place a new order

**Parameters:**
- `symbol` (str): Trading pair (e.g., 'BTC/USDT')
- `side` (str): 'buy' or 'sell'
- `amount` (float): Order amount
- `price` (float, optional): Order price

**Returns:** Order details

#### get_positions()
Get all open positions

#### get_balance()
Get account balance

## MarketAPI

### Methods

#### get_price(symbol)
Get current price

#### get_ohlcv(symbol, timeframe='1h', limit=100)
Get OHLCV data

#### get_order_book(symbol, limit=20)
Get order book

## AnalysisAPI

### Methods

#### backtest_strategy(strategy_name, start_date, end_date=None)
Backtest a trading strategy

#### calculate_metrics(returns)
Calculate performance metrics
