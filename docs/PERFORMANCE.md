# Performance Analysis

## KITTI Road Benchmark Results

### Official Test Set Performance

| Metric | Value |
|--------|-------|
| MaxF | 96.32% |
| AP | 95.87% |
| Precision | 96.79% |
| Recall | 95.85% |
| FPR | 3.21% |
| FNR | 4.15% |

### Validation Set Statistics

- **Mean MaxF**: 96.38%
- **Std Dev**: 2.14%
- **Best Image**: 99.12% F1
- **Worst Image**: 89.45% F1
- **Images**: 58 validation samples

## Efficiency Metrics

### Inference Speed (RTX 4060 Ti)

| Batch Size | FPS | Latency (ms) |
|------------|-----|--------------|
| 1 | 55 | 18.2 |
| 4 | 48 | 20.8 |
| 8 | 42 | 23.8 |

### Model Size

- **Parameters**: 14.04M
- **FLOPs**: 12.3G (at 1242×375 resolution)
- **Model File**: ~54 MB (FP32)

## Comparison with State-of-the-Art

### Accuracy vs Efficiency Trade-off

VLLiNet achieves the best balance between accuracy and efficiency:

- **vs Transformer methods**: 93.2% fewer parameters, 1.23% MaxF drop
- **vs LRDNet**: 28% fewer parameters, 5.5× faster, 0.55% MaxF drop
- **vs USNet**: 54% fewer parameters, 25% faster, 0.57% MaxF lower

### Key Advantages

1. **Lightweight**: Suitable for edge devices (Jetson, mobile platforms)
2. **Real-time**: 55 FPS enables autonomous driving applications
3. **High Precision**: 96.79% precision minimizes false positives
4. **Multi-modal**: Robust to lighting conditions via LiDAR fusion

## Failure Cases

Common failure modes (< 90% F1):
- Heavy shadows with similar road texture
- Unmarked rural roads with vegetation
- Extreme perspective distortion at image boundaries
