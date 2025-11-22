Create Virtual Environment  python -m venv venv_chromadb
Activate Virtual environment .\venv_chromadb\Scripts\activate
Set enviroment
$env:PYTHONDONTWRITEBYTECODE=1
Install Required Packages added in requirements pip install -r requirements.txt
write logic main.py 6.Run app cd.. uvicorn app.main:app --reload 7 Access in Browser http://localhost:8000/