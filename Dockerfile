FROM python:3.6.9-alpine3.9
RUN apk add alpine-sdk
RUN pip3 install vibora

CMD ["vibora"]
