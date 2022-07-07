FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements/requirements_app.txt .

RUN pip install --upgrade pip && pip install -r requirements_app.txt

COPY api/initializer.sh .
COPY api/app api/app
COPY api/main.py api/main.py
COPY model/model.pkl model/model.pkl

# give permission to initializer.sh
RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]