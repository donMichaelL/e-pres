IMAGE="donmichael/e-pres"
# docker ps | grep $IMAGE | awk '{print $1}' | xargs docker stop
sudo docker pull $IMAGE
sudo docker run -d $IMAGE
