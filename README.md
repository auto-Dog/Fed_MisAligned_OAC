# (Forked) Federated Edge Learning with Misaligned Over-The-Air Computation

This repository is the experimental implementation of original paper [Federated Edge Learning with Misaligned Over-The-Air Computation](https://arxiv.org/abs/2102.13604)
(forked from original), and a wiener estimator is added based on paper [Misaligned Over-The-Air Computation of Multi-Sensor Data with Wiener-Denoiser Network](https://arxiv.org/abs/2409.00738)


## Case: Misaligned channel, with symbol misalignment, phase misalignment, and AWGN

Please run
```train
python main_fed_snr.py --Aligned 1 --epochs 101 --short 1 --Estimator 4 --EsN0dB 0 --phaseOffset 3
```
>  phaseOffset can be 0 (no phase misalignment), 1 (maximum phase offset = pi/2),  2 (maximum phase offset = 3pi/4), 3 (maximum phase offset = pi); Estimator can be 1 (aligned sample estimator), 2 (ML estimator), 3 (SP-ML estiamtor), 4 (our wiener estimator)


