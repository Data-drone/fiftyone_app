# A Docker container for the Fifty One App

See: https://github.com/voxel51/fiftyone
for more details

A docker setup for the fiftyone app
Base image is based on this one: 
https://github.com/Data-drone/dl_toolkit/tree/master/deeplearn_minimal

which is also here:
https://hub.docker.com/layers/168611945/datadrone/deeplearn_minimal/cuda-11.1-base/images/sha256-b92578223603bbdb17d023874d5e4d899d0583c1ee3767efb2de9f80ee9225a4?context=repo


## Docker Build

```{bash}

docker build -t fiftyone_app:v0.1 ./docker

```

Note it's probably fine to switch in a python3 base image rather than the custom nvidia one with jupyter that I have it set to
## Start Server

```{bash}

docker run -it -d --gpus all -p 8082:8082 fiftyone_app:v0.1

```

This will then listen on `0.0.0.0:8082`


