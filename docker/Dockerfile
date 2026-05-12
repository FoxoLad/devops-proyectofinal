# =========================
# Builder Stage
# =========================

FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# =========================
# Final Stage
# =========================

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
