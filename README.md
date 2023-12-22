# (Forked) Federated Edge Learning with Misaligned Over-The-Air Computation

This repository is the experimental implementation of paper [Federated Edge Learning with Misaligned Over-The-Air Computation](https://arxiv.org/abs/2102.13604)
(forked from original)


## Case: Misaligned channel, with symbol misalignment, phase misalignment, and AWGN

Please run
```train
python main_fed_snr.py --Aligned 1 --maxDelay 0.9 --phaseOffset 0 --Estimator 1
```
> where maxDelay is in range (0,1); phaseOffset can be 0 (no phase misalignment), 1 (maximum phase offset = pi/2),  2 (maximum phase offset = 3pi/4), 3 (maximum phase offset = pi); Estimator can be 1 (aligned sample estimator), 2 (ML estimator), 3 (SP-ML estiamtor)


