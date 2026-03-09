import pandas as pd
import random

incidents = [
    "Worker slipped on wet floor",
    "Employee tripped over loose cable",
    "Worker cut hand using sharp tool",
    "Employee fell from ladder",
    "Worker struck by falling object",
    "Trip hazard caused by debris",
    "Worker slipped on oil spill",
    "Poor lighting caused worker to fall",
    "Employee misused power drill",
    "Improper stacking of materials caused fall",
    "Worker hit by moving equipment",
    "Worker injured due to improper tool handling",
    "Employee slipped on spilled liquid",
    "Worker tripped on uneven surface",
    "Worker cut finger while using knife"
]

root_causes = [
    "Poor housekeeping",
    "Improper tool usage",
    "Inadequate workplace lighting",
    "Unsafe work practice",
    "Lack of training"
]

data = []

for i in range(1000):
    incident = random.choice(incidents)
    cause = random.choice(root_causes)

    data.append({
        "incident": incident,
        "root_cause": cause
    })

df = pd.DataFrame(data)

df.to_csv("data/incidents_dataset.csv", index=False)

print("Dataset generated with", len(df), "rows")
