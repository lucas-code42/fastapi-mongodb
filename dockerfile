FROM python:3.11.3

WORKDIR /src
COPY requirements.txt ./
COPY . .
RUN pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "main.py" ]
