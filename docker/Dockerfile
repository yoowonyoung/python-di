FROM python:3.7.3-stretch

#install dependency
RUN apt-get update && \
    apt-get install -y vim libjansson-dev libyaml-dev libxml2-dev git autoconf make gcc automake musl-dev default-jre unzip

# Set Timezone KST
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set display port to avoid crash
ENV DISPLAY=:99

#p4python install
#RUN ln -nfs /usr/lib/x86_64-linux-gnu/libssl.so.1.0.2 /usr/lib/x86_64-linux-gnu/libssl.so
#RUN pip3 install p4python==2018.2.1743033

COPY [".", "/root/data_refinery"]
WORKDIR /root/data_refinery
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-test.txt

# SET CONFIG FILE
ENV PYTHONPATH "${PYTHONPATH}:/root/data_refinery"

CMD ["/bin/bash"]
