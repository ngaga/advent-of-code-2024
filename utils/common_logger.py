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
                   format="{message}",
                   level=log_level)
    else:
        # Default configuration - simple format without timestamp and level
        logger.add(lambda msg: print(msg, end=""), 
                   format="{message}",
                   level="INFO")

def get_logger():
    """Get the configured logger instance"""
    return logger
