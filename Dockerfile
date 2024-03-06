FROM python:3.12-alpine

RUN pip install poetry

CMD ["poetry", "install"]
