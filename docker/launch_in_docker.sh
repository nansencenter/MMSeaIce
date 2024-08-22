docker run --gpus all --rm -it -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce mmseaice bash
python quickstart.py configs/sic_mse/sic_mse_maud.py --wandb-project mmseaice1 --work-dir workdir
