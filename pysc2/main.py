import numpy as np
import collections
from copy import deepcopy
import torch as th
from Gen_utils.logging import get_logger
import yaml

from pysc2.tests import run as Run

logger = get_logger()


def my_main(_run, _config, _log):
    # Setting the random seed throughout the modules
    config = config_copy(_config)
    np.random.seed(1234)
    th.manual_seed(1234)
    config['env_args']['seed'] = 1234

    # run the framework
    Run.run(_run, config, _log)


def config_copy(config):
    if isinstance(config, dict):
        return {k: config_copy(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [config_copy(v) for v in config]
    else:
        return deepcopy(config)


def recursive_dict_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = recursive_dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


default_config = None

config_dir = '{0}/{1}'
config_dir2 = '{0}/{1}/{2}'

with open(config_dir.format('config', "{}.yaml".format('default')), "r") as f:
    try:
        default_config = yaml.load(f)
    except yaml.YAMLError as exc:
        assert False, "default.yaml error: {}".format(exc)

env_config = None

with open(config_dir2.format('config','envs', "{}.yaml".format('sc2')), "r") as f:
    try:
        config_dict = yaml.load(f)
    except yaml.YAMLError as exc:
        assert False, "{}.yaml error: {}".format('sc2', exc)
    env_config = config_dict


alg_config = None

with open(config_dir2.format('config','algs', "{}.yaml".format('coma')), "r") as f:
    try:
        config_dict2 = yaml.load(f)
    except yaml.YAMLError as exc:
        assert False, "{}.yaml error: {}".format('sc2', exc)
    alg_config = config_dict2

final_config_dict = recursive_dict_update(default_config, env_config)
final_config_dict = recursive_dict_update(final_config_dict, alg_config)

if __name__ == '__main__':
    my_main(logger, final_config_dict, logger)