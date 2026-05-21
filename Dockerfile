FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p reports/screenshots reports/logs reports/videos

CMD ["pytest", "-n", "auto", "--browser", "chromium", \
     "--html=reports/report.html", "--self-contained-html"]
