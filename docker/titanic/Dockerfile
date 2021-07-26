FROM python:3.8.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

RUN useradd --user-group --shell /bin/false titanic  
USER titanic

EXPOSE 8000

ENV MODEL "baseline.v1"

CMD ["bash", "start.sh"]

