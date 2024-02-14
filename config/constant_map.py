# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps
from aigc_zoo.constants.define import (TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING)

__all__ = [
    "TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING",
    "MODELS_MAP"
]

MODELS_MAP = {
############## internlm2
    'internlm2-7b': {
        'model_type': 'internlm2',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm2-7b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm2-7b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm2-7b',
    },
    'internlm2-20b': {
        'model_type': 'internlm2',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm2-20b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm2-20b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm2-20b',
    },

    'internlm2-base-7b': {
        'model_type': 'internlm2',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm2-base-7b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm2-base-7b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm2-base-7b',
    },
    'internlm2-base-20b': {
        'model_type': 'internlm2',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm2-base-20b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm2-base-20b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm2-base-20b',
    },


}

# 按需修改
# TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING


