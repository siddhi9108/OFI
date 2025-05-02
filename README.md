# OFI

# Order Flow Imbalance (OFI) Feature Engineering

This repository contains a complete implementation of four Order Flow Imbalance (OFI) features, developed as part of a trial task for a quantitative research role. The code is designed to be modular, readable, and directly executable in Google Colab.

## Dataset

- **Input:** `first_25000_rows.csv`  
  A Level-2 limit order book (LOB) dataset containing timestamped bid/ask quotes and sizes for multiple assets.

---

## Implemented Features

### 1. Best-Level OFI
OFI computed using only the top-of-book (Level 1) bid and ask prices/sizes, following the methodology of Cont et al. (2014).

### 2. Multi-Level OFI
Extends OFI computation to levels 2 through 9 of the order book to capture deeper liquidity shifts.

### 3. Integrated OFI
A single compressed OFI feature generated using PCA on the multi-level OFIs, preserving the first principal component.

### 4. Cross-Asset OFI
Captures cross-impact between assets by modeling the return of a target asset (e.g., AAPL) as a function of OFIs from other assets using Lasso regression.

---

## Environment

Developed and tested in:
- **Google Colab (Python 3.10+)**
- Key Libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib` (optional for visualization)

---


