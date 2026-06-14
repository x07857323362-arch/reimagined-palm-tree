# Trading System Repository

一个专业的交易系统仓库，用于管理交易策略、数据分析和 AI 调用接口。

## 📁 仓库结构

```
.
├── README.md                 # 项目文档
├── config/                   # 配置文件
│   ├── trading_config.json   # 交易配置
│   ├── api_config.json       # API 配置
│   └── symbols.json          # 交易品种配置
├── strategies/               # 交易策略
│   ├── momentum.py           # 动量策略
│   ├── mean_reversion.py     # 均值回归策略
│   └── __init__.py
├── data/                     # 数据存储
│   ├── market_data/          # 市场数据
│   ├── historical/           # 历史数据
│   └── cache/                # 缓存数据
├── models/                   # 机器学习模型
│   ├── price_predictor.py    # 价格预测模型
│   ├── risk_analyzer.py      # 风险分析模型
│   └── weights/              # 模型权重
├── api/                      # API 接口
│   ├── trader_api.py         # 交易 API
│   ├── market_api.py         # 市场数据 API
│   └── analysis_api.py       # 分析 API
├── analysis/                 # 数据分析
│   ├── portfolio_analysis.py # 投资组合分析
│   ├── performance.py        # 绩效分析
│   └── reports/              # 分析报告
├── monitoring/               # 监控系统
│   ├── alerts.py             # 告警系统
│   ├── health_check.py       # 健康检查
│   └── logs/                 # 日志文件
├── tests/                    # 单元测试
│   ├── test_strategies.py    # 策略测试
│   ├── test_api.py           # API 测试
│   └── test_models.py        # 模型测试
├── utils/                    # 工具函数
│   ├── market_utils.py       # 市场工具
│   ├── math_utils.py         # 数学工具
│   └── logger.py             # 日志工具
├── docs/                     # 文档
│   ├── API.md                # API 文档
│   ├── STRATEGY.md           # 策略文档
│   └── SETUP.md              # 设置说明
├── requirements.txt          # 依赖
├── setup.py                  # 安装配置
└── .gitignore                # Git 忽略文件
```

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置系统
编辑 `config/trading_config.json` 配置交易参数

### 3. 运行交易
```python
from api.trader_api import TradingAPI

trader = TradingAPI()
trader.start_trading(strategy='momentum')
```

## 🤖 AI 调用接口

### 获取市场数据
```python
from api.market_api import MarketAPI

market = MarketAPI()
data = market.get_price('BTC/USDT')
data = market.get_ohlcv('ETH/USDT', timeframe='1h')
```

### 执行交易
```python
from api.trader_api import TradingAPI

trader = TradingAPI()
order = trader.place_order(symbol='BTC/USDT', side='buy', amount=1.0, price=45000)
```

### 分析策略
```python
from api.analysis_api import AnalysisAPI

analysis = AnalysisAPI()
result = analysis.backtest_strategy('momentum', start_date='2024-01-01')
```

## 📊 关键模块

- **Strategies**: 交易策略实现
- **Models**: 机器学习模型
- **API**: 对外接口
- **Analysis**: 数据分析和报告
- **Monitoring**: 系统监控和告警

## 📝 许可证

MIT License
