FROM python:3
ENV PYTHONUNBUFFERED 0
ENV TZ="/usr/share/zoneinfo/Asia/Seoul"
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh
CMD [ "./wait-for-it.sh" ]