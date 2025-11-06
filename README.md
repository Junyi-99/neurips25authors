# NeurIPS 2025 Statistics

---

## File Structure

- `raw/`: Data fetching and processing scripts
  - `1. fetch.py`: Fetch paper lists in `oral/spotlight/poster` format
  - `2. get_author_ids.py`: Extract unique `authorids` from paper JSON
  - `3. data_info.py`: Output basic data statistics
  - `4. fetch profile.py`: Fetch author profiles via OpenReview API
  - `5. author_papers.py`: Count author-paper mapping and each author's submission count
  - `6. convert_author_to_csv.py`: Convert author profiles to CSV
  - `data/`: Data output directory (generated after running scripts, containing JSON/CSV files)

## Environment Requirements

- Python 3.9+

```bash
pip install pandas tqdm openreview requests
```

## Run the scripts (in `raw/` directory)

1) Fetch paper lists in `oral/spotlight/poster` format (can switch `VENUE` at the top of the script)

```bash
python "1. fetch.py"  # VENUE = "poster" by default, will generate data/neurips2025_poster.json
# Change VENUE to "oral" or "spotlight" in the script and run again
```

Output:
- `data/neurips2025_oral.json`
- `data/neurips2025_spotlight.json`
- `data/neurips2025_poster.json`

2) Extract unique author IDs from paper JSON

```bash
python "2. get_author_ids.py"
```

Output: `data/neurips2025_author_ids.json`

3) View basic statistics (optional)

```bash
python "3. data_info.py"
```

4) Fetch author profiles (time-consuming, supports resuming, and automatically skips existing files)

```bash
python "4. fetch profile.py"
```

Output: `data/authors/{author_id}.json` (if not exists, write error information)

5) Count author-paper mapping and each author's submission count (by venue, change `VENUE` in the script)

```bash
python "5. author_papers.py"
```

Output:
- `data/neurips2025_{VENUE}_author_papers.json`
- Print author submission count Top list in terminal

6) Summarize author profiles to CSV

```bash
python "6. convert_author_to_csv.py"
```

Output:
- If not exists, generate `data/author_map.json`
- Generate `data/neurips25_author_profiles.csv`

