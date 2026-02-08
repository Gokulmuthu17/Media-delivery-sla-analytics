"""
====================================================
MEDIA DELIVERY OPERATIONS – SYNTHETIC DATA GENERATOR
====================================================

Generates realistic CSV datasets for:
- partners
- content_master
- artwork
- project_media (delivery logs)
- error_logs

Used for analytics dashboards & SLA analysis.

Author: Gokul Muthu
"""

import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from pathlib import Path

# ---------------------------
# CONFIG
# ---------------------------

OUTPUT_DIR = Path("../data")
OUTPUT_DIR.mkdir(exist_ok=True)

NUM_PARTNERS = 40
NUM_CONTENT = 1500
NUM_ASSETS = 2500
NUM_DELIVERIES = 12000
NUM_ERRORS = 3000

START_DATE = datetime(2019, 1, 1)
END_DATE = datetime(2024, 12, 31)

random.seed(42)
np.random.seed(42)

# ---------------------------
# MASTER DATA
# ---------------------------

REGIONS = ["NA", "EU", "LATAM", "APAC", "MEA"]

FORMATS = ["JPEG", "PNG", "TIFF", "MP4", "MOV"]
GENRES = ["Drama", "Comedy", "Action", "Kids", "Sports", "Documentary"]

RESOLUTIONS = ["HD", "4K", "8K"]

ERROR_TYPES = [
    "Metadata mismatch",
    "Checksum failure",
    "Invalid codec",
    "Artwork resolution issue",
    "Missing subtitles",
]

SEVERITY = ["Low", "Medium", "High"]


# ---------------------------
# UTILS
# ---------------------------

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))


# ---------------------------
# PARTNERS
# ---------------------------

partners = []

for i in range(1, NUM_PARTNERS + 1):
    partners.append({
        "partner_id": i,
        "partner_name": f"Partner_{i:02d}",
        "region": random.choice(REGIONS),
    })

partners_df = pd.DataFrame(partners)


# ---------------------------
# CONTENT MASTER
# ---------------------------

content_rows = []

for i in range(1, NUM_CONTENT + 1):
    content_rows.append({
        "content_id": i,
        "title": f"Title_{i:04d}",
        "genre": random.choice(GENRES),
        "release_date": random_date(
            datetime(2015, 1, 1),
            datetime(2024, 1, 1)
        ).date(),
    })

content_df = pd.DataFrame(content_rows)


# ---------------------------
# ARTWORK / ASSETS
# ---------------------------

artwork_rows = []

for i in range(1, NUM_ASSETS + 1):
    artwork_rows.append({
        "asset_id": i,
        "content_id": random.randint(1, NUM_CONTENT),
        "format": random.choice(FORMATS),
        "resolution": random.choice(RESOLUTIONS),
        "approved_flag": random.choices([1, 0], weights=[0.75, 0.25])[0],
    })

artwork_df = pd.DataFrame(artwork_rows)


# ---------------------------
# DELIVERY LOGS
# ---------------------------

delivery_rows = []

for i in range(1, NUM_DELIVERIES + 1):

    sla = random.choice([24, 36, 48, 72])

    actual = max(
        4,
        np.random.normal(loc=sla, scale=sla * 0.35)
    )

    status = random.choices(
        ["SUCCESS", "FAILED"],
        weights=[0.9, 0.1]
    )[0]

    delivery_rows.append({
        "delivery_id": i,
        "content_id": random.randint(1, NUM_CONTENT),
        "partner_id": random.randint(1, NUM_PARTNERS),
        "asset_id": random.randint(1, NUM_ASSETS),
        "delivery_date": random_date(START_DATE, END_DATE).date(),
        "sla_hours": sla,
        "actual_hours": round(actual, 2),
        "status": status,
    })

project_media_df = pd.DataFrame(delivery_rows)


# ---------------------------
# ERROR LOGS
# ---------------------------

error_rows = []

failed_ids = project_media_df[
    project_media_df["status"] == "FAILED"
]["delivery_id"].tolist()

for i in range(1, NUM_ERRORS + 1):

    error_rows.append({
        "error_id": i,
        "delivery_id": random.choice(failed_ids),
        "error_type": random.choice(ERROR_TYPES),
        "severity": random.choice(SEVERITY),
    })

error_logs_df = pd.DataFrame(error_rows)


# ---------------------------
# SAVE TO CSV
# ---------------------------

partners_df.to_csv(OUTPUT_DIR / "partners.csv", index=False)
content_df.to_csv(OUTPUT_DIR / "content_master.csv", index=False)
artwork_df.to_csv(OUTPUT_DIR / "artwork.csv", index=False)
project_media_df.to_csv(OUTPUT_DIR / "project_media.csv", index=False)
error_logs_df.to_csv(OUTPUT_DIR / "error_logs.csv", index=False)

print("✅ Synthetic media delivery datasets created:")
print(" - partners.csv")
print(" - content_master.csv")
print(" - artwork.csv")
print(" - project_media.csv")
print(" - error_logs.csv")
print(f"\n📁 Output directory: {OUTPUT_DIR.resolve()}")
