FROM python:3.10-slim
WORKDIR /app
COPY tests/ ./tests/
RUN pip install pytest selenium
RUN apt-get update && apt-get install -y chromium chromium-driver && rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/lib/chromium:/usr/lib/chromium-browser/:$PATH"
CMD ["pytest", "-q"]
