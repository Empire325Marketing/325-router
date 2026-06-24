FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["325", "--help"]
