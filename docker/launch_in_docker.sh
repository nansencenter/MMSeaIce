#docker run --gpus all --rm -it -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce mmseaice bash
#python quickstart.py configs/sic_mse/sic_mse_maud_02.py --wandb-project mmseaice_02 --work-dir workdir_02 --resume-from workdir_02/best_model_workdir.pth

docker run --gpus all --rm -it -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_01.py --wandb-project mmseaice_01 --work-dir workdir_01
# --resume-from workdir_02/best_model_workdir.pth

docker run --gpus all --rm -it -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_02.py --wandb-project mmseaice_02 --work-dir workdir_02 --resume-from workdir_02/best_model_workdir_02.pth

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_03.py --wandb-project mmseaice_03 --work-dir workdir_03 --resume-from workdir_01/best_model_workdir_01.pth

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_01a.py --wandb-project mmseaice_01a --work-dir workdir_01a

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_03a.py --wandb-project mmseaice_03a --work-dir workdir_03a  --resume-from workdir_01a/best_model_workdir_01a.pth

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_01b.py --wandb-project mmseaice_01b --work-dir workdir_01b

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sic_mse/sic_mse_maud_02a.py --wandb-project mmseaice_02a --work-dir workdir_02a   --resume-from workdir_01c/best_model_workdir_01c.pth

docker run --gpus all --rm -v /Home/antonk:/Home/antonk -v /Data/sat/downloads/sentinel1:/Data/sat/downloads/sentinel1 -w $HOME/py/MMSeaIce -e WANDB_API_KEY=e0912e764420c974191dc9a23c71fed3d683b2b9 mmseaice python quickstart.py configs/sir_is2/sir_is2_01.py --wandb-project sir_is2_01 --work-dir sir_is2_01
