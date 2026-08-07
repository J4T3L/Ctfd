FROM python:3.11-slim

# Prevent Python from writing .pyc files & buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create non-root ctf user
RUN useradd -m -u 1000 ctf

# Install dependencies
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ /app/

# Copy flag file to root /flag.txt and /app/flag.txt
COPY flag.txt /flag.txt
COPY flag.txt /app/flag.txt
RUN chmod 444 /flag.txt /app/flag.txt && chown root:root /flag.txt /app/flag.txt

# Set ownership of app directory
RUN chown -R ctf:ctf /app

USER ctf

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
