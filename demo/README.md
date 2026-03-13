# VLLiNet Demo

This directory contains demonstration code for VLLiNet inference.

## ⚠️ Important Notice

**Model weights are NOT included** during journal review. This demo shows:
- Network architecture interface
- Inference pipeline structure
- Input/output format

## Usage

```python
from models import VLLiNet
from demo.inference_demo import load_model, inference

# Load model (without weights)
model = load_model()

# Run inference (requires RGB image, LiDAR points, and calibration)
pred_mask = inference(model, rgb_image, lidar_points, calib)
```

## Expected Performance

When using the full pretrained model:
- **MaxF**: 96.32%
- **FPS**: 55 (RTX 4060 Ti)
- **Parameters**: 14.04M

Full code and weights will be released upon journal acceptance.
