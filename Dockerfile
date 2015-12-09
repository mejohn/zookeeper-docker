FROM centos:latest
MAINTAINER Meaghan Johnson <mejohn10@ncsu.edu>

RUN yum y update && yum install y java1.7.0openjdk java1.7.0openjdkdevel wget tar
RUN wget q O  http://apache.mirrors.pair.com/zookeeper/zookeeper3.4.6/zookeeper3.4.6.tar.gz | tar xzf  C /opt \
    && mv /opt/zookeeper3.4.6 /opt/zookeeper \
    && cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \
    && mkdir p /tmp/zookeeper

ENV JAVA_HOME /usr/lib/jvm/java1.7.0openjdk

EXPOSE 2181 2888 3888

WORKDIR /opt/zookeeper

VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]

ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]
CMD ["startforeground"]