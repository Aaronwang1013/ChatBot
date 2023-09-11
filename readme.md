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