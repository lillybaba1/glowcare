# Uni-One Social Network

This repository contains a prototype for **Uni-One**, a mobile-first Pan-African social networking platform built with FastAPI and Next.js.

## Backend

The backend lives in `backend/` and uses FastAPI. Install dependencies and run with:

```bash
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

## Frontend

The frontend lives in `frontend/` and is a minimal Next.js app. Install dependencies and run with:

```bash
cd frontend
npm install
npm run dev
```

## Features

- User, post and group endpoints in FastAPI
- Simple React pages as a starting point

This is a starting point for the Uni-One application.
