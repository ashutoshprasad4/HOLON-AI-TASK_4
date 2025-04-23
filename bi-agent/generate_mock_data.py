import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Define the date range: 365 days starting from January 1, 2025
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

# Simulate realistic data with trends
base_sessions = 1000
weekly_pattern = np.sin(np.linspace(0, 2 * np.pi * 365 / 7, 365)) * 200

data = {
    "date": dates,
    "sessions": [int(base_sessions + pattern + np.random.normal(0, 100)) for pattern in weekly_pattern],
    "users": [int(s * np.random.uniform(0.8, 0.9)) for s in [base_sessions + pattern + np.random.normal(0, 100) for pattern in weekly_pattern]],
    "pageviews": [int(s * np.random.uniform(2, 3)) for s in [base_sessions + pattern + np.random.normal(0, 100) for pattern in weekly_pattern]],
    "bounce_rate": np.random.uniform(0.25, 0.40, 365),
    "pagePath": np.random.choice(["/home", "/product", "/about", "/contact", "/blog"], 365),
    "source": np.random.choice(["google", "direct", "facebook", "twitter", "bing"], 365),
    "medium": np.random.choice(["organic", "(none)", "cpc", "referral", "social"], 365),
    "deviceCategory": np.random.choice(["desktop", "mobile", "tablet"], 365),
    "eventCount": [int(np.random.randint(300, 700)) for _ in range(365)],
    "activeUsers": [int(s * np.random.uniform(0.85, 0.95)) for s in [base_sessions + pattern + np.random.normal(0, 100) for pattern in weekly_pattern]],
    "avgSessionDuration": np.random.randint(100, 200, 365)
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure positive values
df["sessions"] = df["sessions"].clip(lower=100)
df["users"] = df["users"].clip(lower=80)
df["pageviews"] = df["pageviews"].clip(lower=200)
df["activeUsers"] = df["activeUsers"].clip(lower=80)

# Format bounce_rate to 2 decimal places
df["bounce_rate"] = df["bounce_rate"].round(2)

# Save to CSV
df.to_csv("mock_ga_data.csv", index=False)

# Print first few rows for verification
print("Generated Mock Data Sample:")
print(df.head())