# Copilot Instructions for AI Agents

## Project Overview
This project is a simple data collection and analysis script written in Python. The main script is `analise.py`.

- **Purpose:**
  - Fetches the latest CDI rate from the Brazilian Central Bank API.
  - Appends timestamped CDI data to `taxa-cdi.csv`.
  - Performs analysis using the `cybor` library and generates an HTML report.

## Key Files
- `analise.py`: Main script for data collection, CSV management, and report generation.
- `taxa-cdi.csv`: Output file storing collected CDI rates (created at runtime).
- `relatorio_cdi.html`: Generated HTML report (created at runtime).

## Data Flow
1. Fetches data from `https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados`.
2. Appends new data rows to `taxa-cdi.csv` (creates file with header if missing).
3. Loads the CSV with pandas for analysis.
4. Uses `cybor.analyze(df)` to generate a report, then saves it as HTML.

## Developer Workflows
- **Run the script:**
  ```powershell
  python analise.py
  ```
- **Dependencies:**
  - `pandas`, `cybor`, `requests` (install with `pip install pandas cybor requests`)
- **Output files** are overwritten/updated on each run.

## Project Conventions
- All output files are written to the project root.
- Data is always appended to `taxa-cdi.csv` unless the file is missing (then header is written).
- The script expects the `cybor` library to provide `.analyze()` and `.summary()` methods on the analysis result.

## Integration Points
- **External API:** Brazilian Central Bank (BCB) for CDI rates.
- **External Libraries:** `cybor` for analysis, `pandas` for data handling, `requests` for HTTP.

## Example Pattern
```python
relatorio = cb.analyze(df)
print(relatorio.summary())
relatorio.to_html("relatorio_cdi.html")
```

## Notes
- No build system or test framework is present.
- No project-specific configuration files detected.
- All logic is in a single script; no modularization.

---
If you add new scripts or workflows, update this file to document new conventions or patterns.
