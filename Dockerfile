# Stage 1: Build React Production Frontend
FROM node:20-slim AS frontend-builder
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python Flask Production Container
FROM python:3.11-slim
WORKDIR /app

RUN useradd -m -u 1000 ctf

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/
COPY --from=frontend-builder /frontend/dist /frontend/dist

COPY flag.txt /flag.txt
COPY flag.txt /app/flag.txt
RUN chmod 444 /flag.txt /app/flag.txt && chown root:root /flag.txt /app/flag.txt

RUN chown -R ctf:ctf /app

USER ctf

EXPOSE 8000

CMD ["python", "app.py"]
