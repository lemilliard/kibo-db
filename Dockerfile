FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install virtualenv
RUN virtualenv venv
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN . venv/bin/activate
ENV FLASK_APP='/usr/src/app/src/main.py'

EXPOSE 8500 8500

WORKDIR ./src/
CMD [ "python", "-m", "flask", "run" ]