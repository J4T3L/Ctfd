# Pure Python 3.11-slim Production Container (Ultra-Fast <5s Build Time)
FROM python:3.11-slim
WORKDIR /app

RUN useradd -m -u 1000 ctf

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/
COPY handout/ /app/handout/
COPY handout/ /handout/

COPY flag.txt /flag.txt 2>/dev/null || true
COPY flag.txt /app/flag.txt 2>/dev/null || true
RUN chown -R ctf:ctf /app /handout 2>/dev/null || true

USER ctf

EXPOSE 8000

CMD ["python", "app.py"]
