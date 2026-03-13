# VLLiNet Architecture

## Overview

VLLiNet (Vision-LiDAR Lightweight Integration Network) is designed for real-time road segmentation on resource-constrained devices. The architecture consists of four main components:

1. **Dual-Stream Encoder**
2. **Multi-Scale Fusion Module (MSFM)**
3. **LargeKernelBridge**
4. **U-Net Decoder with Deep Supervision**

## 1. Dual-Stream Encoder

### RGB Branch
- **Backbone**: MobileNetV3-Large (5.4M parameters)
- **Pretrained**: ImageNet weights
- **Output**: Multi-scale features at 1/4, 1/8, 1/16, 1/32 resolution

### LiDAR Branch
- **Input**: ADI (Altitude Difference Image) - single-channel grayscale
- **Architecture**: Lightweight depthwise separable convolutions (0.12M parameters)
- **Design**: Matches RGB feature dimensions at each scale

## 2. Multi-Scale Fusion Module (MSFM)

Cross-modal attention mechanism that fuses RGB and LiDAR features at multiple scales.

**Key Components** (details omitted during review):
- Cross-attention between modalities
- Gated fusion mechanism
- Multi-scale feature aggregation

## 3. LargeKernelBridge

Replaces Transformer with efficient large kernel convolution:
- **Kernel Size**: 7×7
- **Complexity**: O(HW) vs O(H²W²) for self-attention
- **Purpose**: Capture global context without quadratic complexity

## 4. Decoder

U-Net style decoder with:
- Skip connections from encoder
- Deep supervision at multiple scales (training only)
- Final 1×1 convolution for binary classification

## Parameter Distribution

| Component | Parameters | Percentage |
|-----------|-----------|------------|
| RGB Encoder | 5.4M | 38.5% |
| LiDAR Encoder | 0.12M | 0.9% |
| Fusion Module | 3.8M | 27.1% |
| Bridge | 4.4M | 31.3% |
| Decoder | 0.32M | 2.2% |
| **Total** | **14.04M** | **100%** |
