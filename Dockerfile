# Pure Python 3.11-slim Production Container (Ultra-Fast <5s Build Time)
FROM python:3.11-slim
WORKDIR /app

RUN useradd -m -u 1000 ctf

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/
COPY handout/ /app/handout/

COPY flag.txt /flag.txt
COPY flag.txt /app/flag.txt
RUN chmod 444 /flag.txt /app/flag.txt && chown root:root /flag.txt /app/flag.txt

RUN chown -R ctf:ctf /app

USER ctf

EXPOSE 8000

CMD ["python", "app.py"]
