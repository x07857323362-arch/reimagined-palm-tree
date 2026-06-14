# Setup Guide

## Installation

1. Clone the repository
```bash
git clone https://github.com/x07857323362-arch/reimagined-palm-tree.git
cd reimagined-palm-tree
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration

1. Edit `config/trading_config.json` to set trading parameters
2. Edit `config/api_config.json` to set API endpoints
3. Add your API keys to `config/api_keys.json` (not included in repo)

## Running the System

```python
from api.trader_api import TradingAPI

trader = TradingAPI()
trader.place_order('BTC/USDT', 'buy', 1.0, 45000)
```
