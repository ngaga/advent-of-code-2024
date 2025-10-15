# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy pyproject.toml first for better caching
COPY pyproject.toml .

# Copy utils first as it's needed for the package installation
COPY utils/ ./utils/

# Install dependencies
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -e ".[dev]"

# Copy the application code
COPY day1/ ./day1/
COPY day2/ ./day2/
COPY day3/ ./day3/
COPY day4/ ./day4/

# Set the default command to run the main script
CMD ["python", "day1/day1.py"]
