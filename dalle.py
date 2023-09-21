import openai
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


response = openai.Image.create(
    prompt = 'Rnaseq',
    n = 1 ,
    size = '512x512'
)

print(response)
