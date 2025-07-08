# GlowCare Gambia E-commerce Platform

This repository contains a minimal skeleton for **GlowCare Gambia**, an e-commerce project built with FastAPI and Next.js.

## Backend

The backend resides in `glowcare_gambia/` and uses FastAPI with SQLAlchemy.

```bash
pip install -r glowcare_gambia/requirements.txt
uvicorn glowcare_gambia.app.main:app --reload
```

The API exposes product and category endpoints and seeds the database with sample skincare products on startup.

## Frontend

The frontend lives in `glowcare_frontend/` and is a Next.js app styled with TailwindCSS.

```bash
cd glowcare_frontend
npm install
npm run dev
```

The home page displays the GlowCare Gambia branding.

***

This is a starting point for the GlowCare Gambia application.
