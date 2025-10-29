# Hello DevOps (Python)

A tiny Python project for interview/demo purposes. It exposes a small function and a CLI entrypoint and includes tests, a Dockerfile, and a GitHub Actions pipeline.

Quick start (locally):

1. Create a virtual environment and install deps

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

2. Run the app

```powershell
python app.py <name>
```

3. Run tests

```powershell
pytest -q
```

Docker build:

```powershell
docker build -t hello-devops-py .
```

Run container:

```powershell
docker run --rm hello-devops-py
```
