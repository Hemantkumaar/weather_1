# Weather Project

This project compares rainfall in **Seattle**, **St. Louis**, and **New York City** between 2018 and 2022.

## Project Structure
- `data/` — raw and processed CSVs
- `code/` — Jupyter notebooks and Python scripts
- `reports/` — generated charts and visualizations
- `requirements.txt` — project dependencies
- `README.md` — project documentation

## Purpose
The purpose of this project is to analyze and compare rainfall patterns between Seattle and two other U.S. cities (St. Louis and New York City) to explore weather variability across regions.

## Data Sources
- Seattle & St. Louis rainfall datasets: [Course GitHub Repository](https://github.com/)  
- New York City rainfall dataset: [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/search)  

## How to Run
1. Clone the repository and open it in VS Code.
2. Create and activate the virtual environment:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
