#!/usr/bin/env python3
"""Minimal test — deploy marker 8bdc7e3b"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"version":"minimal-8bdc7e3b","status":"ok"}

@app.get("/health")
async def health():
    return {"status":"ok","version":"minimal-8bdc7e3b"}
