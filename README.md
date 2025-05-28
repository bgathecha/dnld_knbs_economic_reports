# 📊 KNBS Economic Survey Scraper

A Python-based web scraper for automatically downloading Economic Survey PDF reports from the [Kenya National Bureau of Statistics (KNBS)](https://www.knbs.or.ke/) website.

---

## 🚀 Features

- Scrapes Economic Survey reports from 1960 to present
- Recursively handles pagination
- Downloads only new files (skips existing)
- Parameterized for flexible use
- Easy to schedule for yearly automation

---

## 📁 Project Structure

```
knbs_scraper/
├── scraper.py           # Main scraping logic
├── test_scraper.py      # Unit tests
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/bgathecha/dnld_knbs_economic_reports.git
cd dnld_knbs_economic_reports
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python scraper.py --url "https://www.knbs.or.ke/all-reports/page/1/?filter_sub_category_7867=economic_surveys" --output-dir "datafiles/"
```

**Arguments:**
- `--url`: Start URL to scrape (required)
- `--output-dir`: Folder to store files (default: `datafiles/`)

---

## 🧪 Running Tests

```bash
python -m unittest test_scraper.py
```

---

## ✅ Ethical Considerations

- Abides by [robots.txt](https://www.knbs.or.ke/robots.txt)
- Does not overload the server (add sleep/delay if needed)
- Intended for educational and research use
- Always review the site's Terms of Service

---

## 📅 Automation Tip

To run this scraper annually, use:
- **Linux/macOS**: `cron`
- **Windows**: Task Scheduler
- **GitHub Actions**: for serverless automation

---

## 📌 TODO

- Add support for date filtering
- Enable logging instead of prints
- Add scraping rate limiter

---

## 👨‍💻 Author

- **Benson Muchoki** – [GitHub Repo](https://github.com/bgathecha/dnld_knbs_economic_reports)