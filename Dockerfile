FROM python:3.9
WORKDIR /app

# COPY requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt

RUN pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8501
COPY . /app

COPY ./config/config.prod.py /app/config/config.py

ENTRYPOINT ["streamlit", "run", "main.py"]

# CMD ["main.py"]