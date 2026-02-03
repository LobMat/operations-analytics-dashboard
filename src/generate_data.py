import pandas as pd
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 30)

lines = ["Line A", "Line B", "Line C"]
shifts = ["Day", "Night"]

rows = []

current_date = start_date
while current_date <= end_date:
    for line in lines:
        for shift in shifts:
            base_output = random.randint(450, 650) if shift == "Day" else random.randint(350, 550)
            downtime = random.randint(0, 90) if shift == "Day" else random.randint(10, 120)

            # Simulate performance differences
            if line == "Line B":
                downtime += random.randint(10, 30)
            if line == "Line C":
                downtime = max(0, downtime - 15)

            units_produced = max(0, base_output - downtime // 2)

            defect_rate = random.uniform(0.01, 0.04) if shift == "Day" else random.uniform(0.02, 0.06)
            defective_units = int(units_produced * defect_rate)

            rows.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "production_line": line,
                "shift": shift,
                "units_produced": units_produced,
                "downtime_minutes": downtime,
                "defective_units": defective_units
            })

    current_date += timedelta(days=1)

df = pd.DataFrame(rows)
df.to_csv("operations-analytics-dashboard/data/raw/production_data.csv", index=False)
