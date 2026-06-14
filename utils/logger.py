"""Logging utility"""

import logging

def setup_logger(name, log_file='logs/trading.log'):
    """Setup logging configuration"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
