#!/usr/bin/env python3
"""
Common logger configuration for Advent of Code 2024
"""

import os
from loguru import logger

def setup_logger():
    """Setup loguru logger with common configuration"""
    # Remove default logger
    logger.remove()
    
    # Configure based on environment variables
    if os.getenv("DISABLE_LOGS", "false").lower() == "true":
        # Disable all logs
        logger.add(lambda msg: None)
    elif os.getenv("LOG_LEVEL"):
        # Set specific log level
        log_level = os.getenv("LOG_LEVEL").upper()
        logger.add(lambda msg: print(msg, end=""), 
                   format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
                   level=log_level)
    else:
        # Default configuration with colors and timestamps
        logger.add(lambda msg: print(msg, end=""), 
                   format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
                   level="INFO")

def get_logger():
    """Get the configured logger instance"""
    return logger
