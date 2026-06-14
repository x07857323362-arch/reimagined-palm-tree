# Trading Strategy Documentation

## Available Strategies

### 1. Momentum Strategy

Trades based on price momentum

**Configuration:**
- `lookback_period`: 20 (default)
- `threshold`: 0.02 (2% default)

**How it works:**
- Calculates momentum over lookback period
- Generates buy signal when momentum > threshold
- Generates sell signal when momentum < -threshold

### 2. Mean Reversion Strategy

Trades when prices deviate from mean

**Configuration:**
- `period`: 30 (default)
- `std_dev`: 2.0 (default)

**How it works:**
- Calculates Bollinger Bands
- Generates buy signal when price < lower band
- Generates sell signal when price > upper band

## Creating Custom Strategies

Extend the base strategy class and implement `generate_signal()` method.
