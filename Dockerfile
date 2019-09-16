FROM img.yefxx.cn:5443/ops/jdk8:alpine
MAINTAINER baxk"yefuxiong@live.com"
WORKDIR workspace
COPY jar /data/webapps/
EXPOSE 7072
ENTRYPOINT ["/data/run.sh"]

