from models import model_helper
import os
import sys
import tensorflow as tf

from FLAGS import PARAM
from utils import dataset_utils
from utils import misc_utils

def train():
  pass

def main(exp_dir,
         log_dir,
         summary_dir,
         ckpt_dir,
         log_file):  # train
  # model_creator = model_helper.get_model_creator()
  # gmd : graph, model, dataset
  # train_gmd = model_helper.build_train_model(log_file, model_creator, PARAM.scope)
  # eval_gmd = model_helper.build_eval_model(log_file, model_creator, PARAM.scope)

  # Preload data for sample decoding.
  # dev_src_file = "%s.%s" % (PARAM.dev_prefix, PARAM.src)
  # dev_tgt_file = "%s.%s" % (PARAM.dev_prefix, PARAM.tgt)
  # sample_src_data = dataset_utils.load_data(dev_src_file)
  # sample_tgt_data = dataset_utils.load_data(dev_tgt_file)

  # TensorFlow Model
  # config_proto = misc_utils.get_session_config_proto()

  pass







if __name__ == '__main__':
  main(*misc_utils.ini_task('train'))
