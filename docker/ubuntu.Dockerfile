FROM python
COPY . /pwbs
WORKDIR /pwbs
RUN pip install .
VOLUME /app
WORKDIR /app
ENTRYPOINT ["pwbs"]
