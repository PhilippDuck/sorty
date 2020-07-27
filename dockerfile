FROM python:3

ADD /scripts /scripts

RUN mkdir /mymedia

#set locale
RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_US.UTF-8

RUN pip3 install hachoir

CMD [ "python3", "./scripts/sorty.py" ]