### Docker env for CTF
```bash
IMAGE_NAME=<image name> CONTAINER_NAME=<container name>
docker build -f Dockerfile.<version> -t $$IMAGE_NAME . 
docker run -it -v $(pwd):/tmp --privileged --name=$IMAGE_NAME $CONTAINER_NAME /bin/bash
```
