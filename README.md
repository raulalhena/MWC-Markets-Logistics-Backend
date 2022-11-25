```bash
python3 -m venv venv  
source venv/bin/activate 
pip install -r requirements.txt


docker-compose up -d


python3 -m uvicorn main:app --reload --port 50000
```


```bash
docker cp raw/* hackathon:/
docker exec -ti hackathon /bin/bash

psql --username postgres
\copy centers FROM 'center_info.csv' DELIMITER ',' CSV
\copy orders FROM 'weekly_demand.csv' DELIMITER ',' CSV

```
Deploying