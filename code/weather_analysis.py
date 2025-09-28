# Weather rainfall comparison (Seattle, St. Louis, NYC) 2018-2022
# Outputs a PNG to reports/monthly_rainfall_2018_2022.png and prints monthly means.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

def load_csv(filename: str) -> pd.DataFrame:
    """Read a CSV with DATE parsed and return a DataFrame."""
    path = DATA / filename
    return pd.read_csv(path, parse_dates=["DATE"])

def to_inches(df: pd.DataFrame, city: str) -> pd.DataFrame:
    """
    Ensure precipitation is in inches.
    Course CSVs (Seattle) and your NYC file are in inches.
    St. Louis (NOAA export) is often in millimeters, so convert mm -> inches.
    """
    out = df.copy()
    if city.lower().startswith("stl"):
        out["PRCP_IN"] = out["PRCP"].astype(float) / 25.4  # mm -> inches
    else:
        out["PRCP_IN"] = out["PRCP"].astype(float)         # already inches
    return out

def monthly_totals(df: pd.DataFrame) -> pd.Series:
    return df.set_index("DATE")["PRCP_IN"].resample("M").sum()

def main():
    seattle = to_inches(load_csv("seattle_rain.csv"), "seattle")
    stl     = to_inches(load_csv("stl_rain.csv"), "stl")
    nyc     = to_inches(load_csv("nyc_rain_4132986.csv"), "nyc")

    s = monthly_totals(seattle)
    t = monthly_totals(stl)
    n = monthly_totals(nyc)

    print("Monthly mean precipitation (inches):")
    print(f"  Seattle   : {s.mean():.2f}")
    print(f"  St. Louis : {t.mean():.2f}")
    print(f"  NYC       : {n.mean():.2f}")

    ax = s.plot(figsize=(12,6), label="Seattle")
    t.plot(ax=ax, label="St. Louis")
    n.plot(ax=ax, label="New York City")
    ax.set_title("Monthly Rainfall Totals (2018–2022)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Precipitation (inches)")
    ax.legend()
    plt.tight_layout()

    out_path = REPORTS / "monthly_rainfall_2018_2022.png"
    plt.savefig(out_path, dpi=150)
    print(f"Saved figure to: {out_path}")

if __name__ == "__main__":
    main()
