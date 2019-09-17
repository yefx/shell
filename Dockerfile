FROM registry.cn-chengdu.aliyuncs.com/images_k8s_hub/jdk8:alpine
MAINTAINER baxk"yefuxiong@live.com"
WORKDIR workspace
COPY jar /data/webapps/
EXPOSE 7072
ENTRYPOINT ["/data/run.sh"]
