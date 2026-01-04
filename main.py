from fastapi import FastAPI
from selenium import webdriver


app = FastAPI(
    title="Selenium FastAPI Example",
    description="An example FastAPI application that uses Selenium WebDriver.",
    version="1.0.0"
)
