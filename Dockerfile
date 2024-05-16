FROM python:3.9

WORKDIR /dircode

COPY ./requirements.txt /dircode/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dircode/requirements.txt

COPY ./app /dircode/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]