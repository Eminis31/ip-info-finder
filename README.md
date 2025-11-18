# IP Info Finder (Python)

A small Flask-based web app to look up geolocation and other basic information for an IP address. This repository provides a simple UI, an API-backed lookup utility in `utils/ip_lookup.py`, and tests to validate functionality.

**Features**
- Web UI to enter an IP and see its information (`templates/index.html`, `templates/results.html`).
- Lookup helper utility in `utils/ip_lookup.py`.
- Static assets in `static/` (CSS & JS).
- Unit tests in the `tests/` folder.

**Requirements**
- Python 3.8+ (install from python.org or your package manager)
- The Python packages listed in `requirements.txt`

**Setup (Windows PowerShell)**

Open PowerShell in the project root and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Running the app (development)**

Start the Flask app with:

```powershell
python app.py
```

Then open a browser and visit `http://127.0.0.1:5000/` to use the UI.

**Running tests**

Run the test suite with:

```powershell
python -m pytest -q
```

**Project structure**

- `app.py` — Application entrypoint (Flask app).
- `requirements.txt` — Python dependencies.
- `templates/` — HTML templates (`index.html`, `results.html`).
- `static/` — Static files (`css/styles.css`, `js/main.js`).
- `utils/ip_lookup.py` — IP lookup utility used by the app.
- `tests/` — Unit tests (e.g. `test_ip_lookup.py`).

**Notes & Next steps**

- If you plan to deploy, set up a proper WSGI server (Gunicorn/Waitress) and configure environment variables for production.
- If the app uses a third-party IP geolocation API, ensure you store any API keys securely (environment variables or secrets manager) and update the README with usage limits or attribution required by the provider.

**Contributing**

Contributions are welcome. Fork the repo, create a feature branch, and open a pull request. Add tests for new functionality.

**License**

licensed under the MiT 
