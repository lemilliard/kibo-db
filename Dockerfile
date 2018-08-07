FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8500 8500

WORKDIR ./src/
CMD [ "python", "./main.py" ]