# official
FROM python:3.8-slim

# workdir
WORKDIR /app

# copy local project to work directory
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# start docker
CMD ["python", "./matrix-multiplication/main.py"]
