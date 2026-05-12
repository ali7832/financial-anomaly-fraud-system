# Deployment Guide

## Local Run

```bash
pip install .[dev]
uvicorn fraud_system.api:app --reload
```

## Docker

```bash
docker build -t fraud-system .
docker run -p 8000:8000 fraud-system
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```
