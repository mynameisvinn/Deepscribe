import torch
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration,Adafactor
import os
import numpy as np

def create_model():
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base', return_dict=True)


    optimizer = Adafactor(model.parameters(),lr=1e-4,
                          eps=(1e-30, 1e-3),
                          clip_threshold=1.0,
                          decay_rate=-0.8,
                          beta1=None,
                          weight_decay=0.0,
                          relative_step=False,
                          scale_parameter=False,
                          warmup_init=False)

    return model, tokenizer, optimizer