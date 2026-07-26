# Hybrid Anomaly Intelligence Engine

## Overview
The **Hybrid Anomaly Intelligence Engine** combines multiple independent, modular anomaly detectors into a single **Hybrid Anomaly Score [0.0, 1.0]**.

## Architecture & Detectors
1. **Statistical Detector** (`statistical_detector.py`): Modified Z-scores, IQR, rolling mean, std dev.
2. **Isolation Forest Detector** (`isolation_forest_detector.py`): Unsupervised Scikit-Learn IsolationForest model.
3. **Peer Group Detector** (`peer_group_detector.py`): Cohort distance & baseline similarity.
4. **Behaviour Drift Detector** (`drift_detector.py`): Moving window shift (7-day vs 30-day vs 90-day).
5. **Sequence Behaviour Detector** (`sequence_detector.py`): Markov Chain event transition probability.

## Score Fusion
Detectors output scores in `[0.0, 1.0]`. The `ScoreFusionEngine` computes the weighted ensemble score and records individual detector contributions.
