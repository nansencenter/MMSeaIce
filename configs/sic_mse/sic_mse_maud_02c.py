#!/usr/bin/env python
# -*-coding:utf-8 -*-
from functions import f1_metric


_base_ = ['../_base_/base.py']

SCENE_VARIABLES = [
    # -- Sentinel-1 variables -- #
    'nersc_sar_primary',
    'nersc_sar_secondary',
    #'sar_incidenceangle',

    # -- Geographical variables -- #
    #'distance_map',

    # -- AMSR2 channels -- #
    # 'btemp_6_9h', 'btemp_6_9v',
    # 'btemp_7_3h', 'btemp_7_3v',
    # 'btemp_10_7h', 'btemp_10_7v',
    'btemp_18_7h', 'btemp_18_7v',
    # 'btemp_23_8h', 'btemp_23_8v',
    'btemp_36_5h', 'btemp_36_5v',
    # 'btemp_89_0h', 'btemp_89_0v',

    # -- Environmental variables -- #
    #'u10m_rotated', 'v10m_rotated',
    #'t2m',
    # 'skt',
    #'tcwv', 'tclw',

    # -- Auxilary Variables -- #
    #'aux_time',
    #'aux_lat',
    #'aux_long'
]


train_options = {
    'train_variables': SCENE_VARIABLES,
    'path_to_train_data': 'new_to_train2',
    'path_to_test_data': 'new_to_train2',
    'test_path_gt_embedded_json': 'datalists/testset.json',
    'compute_classwise_f1score': True,
    'plot_confusion_matrix': True,

    'optimizer': {
        'type': 'SGD',
        'lr': 0.001,  # Optimizer learning rate.
        'momentum': 0.9,
        'dampening': 0,
        'nesterov': False,
        'weight_decay': 0.01
    },

    'scheduler': {
        'type': 'CosineAnnealingWarmRestartsLR',  # Name of the schedulers
        'EpochsPerRestart': 20,  # Number of epochs for the first restart
        # This number will be used to increase or descrase the number of epochs to restart after each restart.
        'RestartMult': 1,
        'lr_min': 0,  # Minimun learning rate
    },

    'batch_size': 16,
    'num_workers': 0,  # Number of parallel processes to fetch data.
    'num_workers_val': 0,  # Number of parallel processes during validation.
    'patch_size': 256,
    'down_sample_scale': 2,

    'data_augmentations': {
        'Random_h_flip': 0.5,
        'Random_v_flip': 0.5,
        'Random_rotation_prob': 0.5,
        'Random_rotation': 90,
        'Random_scale_prob': 0.,
        'Random_scale': (1., 1.),
        'Cutmix_beta': 1.0,
        'Cutmix_prob': 0.,
    },
    # -- Model selection -- #
    'model_selection': 'unet_regression_sir',  # Either 'swin' or 'unet
    'unet_conv_filters': [32, 32, 64, 64],
    'epochs': 500,  # Number of epochs before training stop.
    'epoch_len': 500,  # Number of batches for each epoch.
    # Size of patches sampled. Used for both Width and Height.
    'patch_size': 256,
    # Which train set is going to be used
    'train_list_path': 'datalists/ntt2_trn.json',
    # Which validation set is going to be used
    'val_path': 'datalists/ntt2_val.json',
    'task_weights': [1],
    'charts': ['SIR02'],
    'chart_loss': {  # Loss for the task
        'SIR02': {
            'type': 'CrossEntropyLoss',
            'ignore_index': 255,
        },
    },
    'n_classes': {  # number of total classes in the reference charts, including the mask.
        'SIR02': 7,
    },
    'class_fill_values': {  # Mask value for class/reference data.
        'SIR02': 255,
    },

    # -- Validation options -- #
    'chart_metric': {  # Metric functions for each ice parameter and the associated weight.
        'SIR02': {
            'func': f1_metric,
            'weight': 1,
        },
    },
}
