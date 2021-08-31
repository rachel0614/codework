# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:43:02 2021

@author: hp
"""

import wandb
run = wandb.init()
artifact = run.use_artifact('rachelwang/YOLOv5/run_2ib4btom_model:v0', type='model')
artifact_dir = artifact.download()