FROM python:3.8.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

RUN useradd --user-group --shell /bin/false titanic
RUN chown -R titanic models  
USER titanic

CMD ["./scripts/train_save_model.py", "-m", "make_baseline_model", "-o", "baseline.v1", "-v"]

