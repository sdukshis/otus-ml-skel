# First stage - train model
FROM python:3.8.11-slim AS trainer

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

RUN ./scripts/train_save_model.py -m make_baseline_model -o baseline.v1 -d ./train.csv -v

# Second stage - create service and get model from previous stage
FROM python:3.8.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

COPY --from=trainer /usr/src/app/models/baseline.v1.joblib ./models/

RUN useradd --user-group --shell /bin/false titanic  
USER titanic

EXPOSE 8000

ENV MODEL "baseline.v1"

CMD ["bash", "start.sh"]

