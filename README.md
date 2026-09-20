# Photobooth

This repository contains a Django API and a Vue.js frontend.

## Requirements

- Python 3.12 or newer
- Node.js 20 or newer and npm

## Run the Django project

From the repository root:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

The Django development server runs at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Keep this terminal running while using the Vue application.

## Run the Vue project

Open a second terminal and change into the Vue project directory:

```bash
cd frontend
npm install
npm run dev
```

Vite will print the frontend URL in the terminal, usually [http://localhost:5173/](http://localhost:5173/).

If the frontend needs to call the Django API, make sure its API base URL points to:

```text
http://127.0.0.1:8000
```

## Common Django commands

Activate the virtual environment before running these commands:

```bash
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

## Windows activation

On Windows PowerShell, activate the virtual environment with:

```powershell
venv\Scripts\Activate.ps1
```

## Run with Docker Compose

Make sure Docker and Docker Compose are installed, then run this command from the repository root:

```bash
cp .env.example .env
docker compose up --build
```

The Django API is available at [http://localhost:8000/](http://localhost:8000/) and the Vue application is available at [http://localhost:5173/](http://localhost:5173/).

To stop the services, press `Ctrl+C` or run:

```bash
docker compose down
```
