FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP='./src/main.py'

EXPOSE 8500 8500
EXPOSE 5000 5000

CMD [ "python", "-m", "flask", "run" ]
