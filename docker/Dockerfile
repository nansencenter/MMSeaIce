FROM continuumio/miniconda3
LABEL maintainer="Anton Korosov <anton.korosov@nersc.no>"
LABEL version="0.1"

RUN apt-get update && apt-get install -y libgl1-mesa-glx libegl1 libopengl0 g++ gcc
RUN conda install -y -c conda-forge opencv pytorch
RUN pip install mmcv-full xarray h5netcdf matplotlib tqdm scikit-learn icecream wandb torchmetrics segmentation-models-pytorch