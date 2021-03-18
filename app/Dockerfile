FROM python

EXPOSE 5000

WORKDIR /app

COPY templates/ /app/templates
COPY js/ /app/js
COPY static/ /app/static
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py