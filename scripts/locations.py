# Single source of truth for which places the pipeline covers. Both
# fetch_series.py and analyze_series.py import this list, so adding a place
# is one new entry here -- no other code change. Le Mans keeps the original
# file names so earlier paths (and the delivery checklist) stay valid.
LOCATIONS = [
    {
        "slug": "le-mans",
        "name": "Le Mans",
        "lat": 48.0061, "lon": 0.1996,
        "hemisphere": "Northern",
        "csv": "data/series.csv",
        "json": "docs/data/series_analysis.json",
    },
    {
        "slug": "sydney",
        "name": "Sydney",
        "lat": -33.8688, "lon": 151.2093,
        "hemisphere": "Southern",
        "csv": "data/series_sydney.csv",
        "json": "docs/data/series_analysis_sydney.json",
    },
]
