FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

COPY models/baseline.v1.joblib models/
EXPOSE 8000

ENV MODEL "baseline.v1"

ENTRYPOINT ["uvicorn", "service.main:app", "--host", "0.0.0.0"]

