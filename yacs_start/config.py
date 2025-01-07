from yacs.config import CfgNode as CN

_cfg = CN()

_cfg.SYSTEM = CN()
_cfg.SYSTEM.NUM_GPUS = 8
_cfg.SYSTEM.NUM_WORKERS = 4

_cfg.TRAIN = CN()
_cfg.TRAIN.HYPERPARAMETER_1 = 0.1
_cfg.TRAIN.SCALES = (2, 4, 8, 16)

_cfg.merge_from_file('yacs_start/experimental.yaml')
print(_cfg)