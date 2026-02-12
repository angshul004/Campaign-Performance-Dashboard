# Marketing Campaign Performance Dashboard

A small Flask web application to manage and analyze marketing campaign performance using manually entered data.
## Screenshots
<img width="1919" height="853" alt="image" src="https://github.com/user-attachments/assets/e674d408-7802-4103-b17f-7820fdc024d0" />
<img width="1902" height="856" alt="image" src="https://github.com/user-attachments/assets/5a5b252c-3790-4fcc-ab4a-3dd294ea0e1b" />



## Overview
This project provides a simple business dashboard for tracking campaign outcomes across platforms (such as Google, Instagram, and Email).

Core capabilities:
- Add campaign data
- View all campaigns in a list
- See KPI summaries
- Visualize performance with charts

## Tech Stack
- Backend: Python, Flask
- Database: SQLite with Flask-SQLAlchemy
- Frontend: HTML, CSS, minimal JavaScript
- Charts: Chart.js

## Project Structure
```text
marketing analysis project/
+-- app/
¦   +-- static/
¦   ¦   +-- css/
¦   ¦       +-- style.css
¦   +-- templates/
¦   ¦   +-- add_campaign.html
¦   ¦   +-- base.html
¦   ¦   +-- campaigns.html
¦   ¦   +-- dashboard.html
¦   ¦   +-- home.html
¦   +-- __init__.py
¦   +-- extensions.py
¦   +-- models.py
¦   +-- routes.py
+-- instance/
¦   +-- marketing.db
+-- config.py
+-- requirements.txt
+-- run.py
+-- README.md
```

## Features
- Home page (`/`) with summary cards and recent campaigns
- Add campaign page (`/add`) for manual data entry
- Campaign list page (`/campaigns`) with tabular records
- Dashboard page (`/dashboard`) with:
  - KPI cards:
    - Total campaigns
    - Total leads
    - Total conversions
    - Conversion rate
  - Bar chart: Clicks vs Conversions
  - Pie chart: Platform-wise performance

## Database Model
Single table: `Campaign`

Fields:
- `id`
- `campaign_name`
- `platform`
- `budget`
- `impressions`
- `clicks`
- `leads`
- `conversions`
- `start_date`
- `end_date`

## Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/angshul004/Campaign-Performance-Dashboard
cd "marketing analysis project"
```

### 2. Create and activate virtual environment
Windows (PowerShell):
```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python run.py
```

### 5. Open in browser
Visit:
- `http://127.0.0.1:5000/`

## How to Use
1. Go to `/add` and enter campaign data.
2. Open `/campaigns` to review saved records.
3. Open `/dashboard` to view KPI cards and charts.

Example placeholders:
- Home page
- Add campaign form
- Campaign list
- Dashboard (KPIs + charts)

## Notes
- Data is stored locally in SQLite (`instance/marketing.db`).
- No authentication is included.
- No external APIs are used.
