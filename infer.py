import argparse
import json
import random
import os
import os.path as osp
import shutil
from icecream import ic
import pathlib
import warnings

import numpy as np
import torch
from tqdm import tqdm  # Progress bar
from mmcv import Config

from functions import create_train_validation_and_test_scene_list, get_model, load_model
from loaders import get_variable_options, AI4ArcticChallengeDataset, AI4ArcticChallengeTestDataset
from utils import colour_str


def parse_args():
    parser = argparse.ArgumentParser(description='Train Default U-NET segmentor')

    # Mandatory arguments
    parser.add_argument('config', type=pathlib.Path, help='train config file path',)
    parser.add_argument('--cnn-path', type=pathlib.Path, default=None, help='trained CNN path')
    parser.add_argument('--out-dir', type=pathlib.Path, default=None, help='trained CNN path')
    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    ic(args.config)
    cfg = Config.fromfile(args.config)
    train_options = cfg.train_options
    # Get options for variables, amsrenv grid, cropping and upsampling.
    train_options = get_variable_options(train_options)
    create_train_validation_and_test_scene_list(train_options)
    #print(train_options)
    #print(args)
    #print(train_options['validate_list'])
    if torch.cuda.is_available():
        print(colour_str('GPU available!', 'green'))
        print('Total number of available devices: ',
              colour_str(torch.cuda.device_count(), 'orange'))

        # Check if NVIDIA V100, A100, or H100 is available for torch compile speed up
        if train_options['compile_model']:
            gpu_ok = False
            device_cap = torch.cuda.get_device_capability()
            if device_cap in ((7, 0), (8, 0), (9, 0)):
                gpu_ok = True

            if not gpu_ok:
                warnings.warn(
                    colour_str("GPU is not NVIDIA V100, A100, or H100. Speedup numbers may be lower than expected.", 'red')
                )

        # Setup device to be used
        device = torch.device(f"cuda:{train_options['gpu_id']}")

    net = get_model(train_options, device)
    if train_options['compile_model']:
        net = torch.compile(net)
    _ = load_model(net, args.cnn_path)
    print(net)

if __name__ == '__main__':
    main()
