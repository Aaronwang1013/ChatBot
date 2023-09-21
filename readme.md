## Create python env:
python3 -m venv fastapienv
source fastapienv/bin/activate

## upgrade pip:
python3 -m pip install --upgrade pip

## install dependencies:
pip install fastapi
pip install "uvicorn[standard]"

## uvicorn books:app --reload:
books is coming from the name of the python file, wher our app is living
--reload mean that everytime we change the code, the server will automatically reload  

## review the current api list:
 link 127.0.0.1:8000/docs, this include the information of all API, and can use UI to try to get the reutrn of API.


## path parameters:
passing in something in the URL that we're converting to our parameter in our function with a query parameter
## query parameters:
filter data based on url provided
fastAPI automatically knows that, anything that is passed after books, that is not a dynamic path parameter, We want to convert into whatever parameters we have here within our function.

## Post request method:
uesd to create data, Post can have a body that has additional information that GET doest not have.
## Put request method
used to update data 
put can have a body that has additional information (LIKE POST) that GET does not have

## delete request method
use to delete data

## Note :
make sure the smakker api endpoint are always in the front of the file, because if not, it could get consumed by a longer endpoint that takes in more variables



## OpenAI
pip install openai

## remember to export api path first

## OpenAI prompt

system prompt can dictate the direction of ther reponse that we are getting for our users.
System prompt vs assistant prompt vs user prompt:
system dicates the behavior while the assistant is the history of the chat. User input is your prompt you are asking chat bot.


## Temperature
Temperature is all about randomness
In general words, the lower the temperature the more likely the model will choose with a higher probability of occurrence.

higher temperature, more creative (a story, I think is not suitable for GenomiceBot)

Scale the temperature from 0 to 2

## How to keep chat log?
Chat log


## User system
store all log in specific user, if not login, log will not be stored

## how to deal with outlook 生資詢問？
要train資料集，或是直接把資料的問答當作chatlog?



## create requirement for aws lambda
pip freeze > requirement.txt
# remove the embedded requirement, keep the required, and change fastapi to v.0.99.1

pip3 install -t dependencies -r requirement.txt
# this will create a directory with all the dependencies that we just did

(cd dependencies; zip ../aws_lambda_artifact.zip -r .)
zip aws_lambda_artifact.zip -u main.py