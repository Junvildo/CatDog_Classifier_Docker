# CatDog_Classifier_Docker
# Installation
```
docker build -f Dockerfile -t <container_name> .
```
# Run
```
docker run -v ./docker_data:<where/to/mount> -p <host_machine_port>:5000 -ti <container_name> /bin/bash -c "source activate ml && cd <where/to/mount> && python app.py"
```
# API Endpoint
```
localhost:<host_machine_port>/predict?image_path=<local_image_path_or_online_image_links>
```
