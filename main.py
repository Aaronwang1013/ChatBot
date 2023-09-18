import openai
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# make a fastapi application

app = FastAPI()
templates = Jinja2Templates(directory='templates')
chat_response = []
@app.get("/" , response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse('home.html', {"request": request,"chat_responses": chat_response})

chatLog = [{'role': 'system', 
            'content': 'You are a professional bioinformatican'}]



# Annotated[datastructures , 'hint']
@app.post("/",response_class=HTMLResponse)
async def chat(request:Request , userInput: Annotated[str , Form()]):
        chatLog.append({'role' : 'user' , 'content' : userInput})
        chat_response.append(userInput)
        
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = chatLog,
            temperature = 0.6
        )
    
        bot_response = response['choices'][0]['message']['content']

        chatLog.append({'role' :'assistant', 'content' : bot_response})
        chat_response.append(bot_response)
        return templates.TemplateResponse("home.html" , {'request':request , "chat_responses":chat_response})
    
    
    
@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):

    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})