# CatDog_Classifier_Docker
# Installation
```
docker build -f Dockerfile -t <container_name> .
```
# Run
```
docker run -p <host_machine_port>:5000 -ti <container_name> python app.py
```
# API Endpoint
localhost:<host_machine_port>/predict?image_path=<local_image_path or online_image_links>