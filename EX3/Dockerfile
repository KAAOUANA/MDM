FROM python:3.7
COPY Code/* /test_mdm/
WORKDIR /test_mdm
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "/test_mdm/main.py" ]