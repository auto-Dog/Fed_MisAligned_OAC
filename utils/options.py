#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import argparse

pth_root = './grads/'
running_root = './run'
def args_parser():
    parser = argparse.ArgumentParser()
    # federated arguments
    parser.add_argument('--short', type=float, default=0, help="short or long pkt")
    parser.add_argument('--Aligned', type=float, default=1, help="Aligned or not")
    parser.add_argument('--maxDelay', type=float, default=0.9, help="the maximum delay of the devices")
    parser.add_argument('--phaseOffset', type=float, default=0, help="phase offsets, can be 0->0; 1->2pi/4; 2->3pi/4; 3->pi")
    parser.add_argument('--EsN0dB', type=float, default=100.0, help="variance of the noise")
    parser.add_argument('--Estimator', type=float, default=1, help="1->aligned_sample,2->ML,3->SP-ML,4->Wiener")
    parser.add_argument('--epochs', type=int, default=100, help="rounds of training")
    parser.add_argument('--num_users', type=int, default=40, help="number of users: K")
    parser.add_argument('--frac', type=float, default=0.1, help="the fraction of clients: C")
    parser.add_argument('--local_ep', type=int, default=5, help="the number of local epochs: E")
    parser.add_argument('--local_bs', type=int, default=128, help="local batch size: B")
    parser.add_argument('--bs', type=int, default=128, help="test batch size")
    parser.add_argument('--lr', type=float, default=0.1, help="learning rate")
    parser.add_argument('--momentum', type=float, default=0.5, help="SGD momentum (default: 0.5)")
    parser.add_argument('--split', type=str, default='user', help="train-test split type, user or sample")

    # model arguments
    parser.add_argument('--model', type=str, default='cnn', help='model name')
    parser.add_argument('--kernel_num', type=int, default=9, help='number of each kind of kernel')
    parser.add_argument('--kernel_sizes', type=str, default='3,4,5',
                        help='comma-separated kernel size to use for convolution')
    parser.add_argument('--norm', type=str, default='batch_norm', help="batch_norm, layer_norm, or None")
    parser.add_argument('--num_filters', type=int, default=32, help="number of filters for conv nets")
    parser.add_argument('--max_pool', type=str, default='True',
                        help="Whether use max pooling rather than strided convolutions")

    # other arguments
    parser.add_argument('--dataset', type=str, default='cifar', help="name of dataset")
    parser.add_argument('--iid', action='store_true', help='whether i.i.d or not')
    parser.add_argument('--num_classes', type=int, default=10, help="number of classes")
    parser.add_argument('--num_channels', type=int, default=3, help="number of channels of imges")
    parser.add_argument('--gpu', type=int, default=0, help="GPU ID, -1 for CPU")
    parser.add_argument('--stopping_rounds', type=int, default=10, help='rounds of early stopping')
    parser.add_argument('--verbose', action='store_true', help='verbose print')
    parser.add_argument('--seed', type=int, default=1, help='random seed (default: 1)')
    parser.add_argument('--save_grad', action='store_true', help='save each client\'s gradient file, every 10 epoches')
    args = parser.parse_args()
    return args
