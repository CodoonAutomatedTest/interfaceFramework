#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 上午11:04
# @File    : ParsUtil.py
import os
import yaml


def read_yaml_data(yaml_file):
    with open(str(get_project_path()) + '/data/' + yaml_file, encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


def read_config_yaml(name1, name2):
    """读取全局配置yaml文件"""
    with open(str(get_project_path()) + '/conf/config.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[name1][name2]


def read_extract_yaml(name1, name2):
    """读取全局配置yaml文件"""
    with open(str(get_project_path()) + '/conf/extract.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[name1][name2]


def get_project_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.dirname(current_dir)
    return root_dir