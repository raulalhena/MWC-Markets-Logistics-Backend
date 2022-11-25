```bash
python3 -m venv venv  
source venv/bin/activate 
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 50000
````