"""
VLLiNet Inference Demo
Demonstrates the inference interface (weights not included)
"""
import torch
from models import VLLiNet
from utils import generate_adi

def load_model(checkpoint_path=None):
    """
    Load VLLiNet model.

    Note: Pretrained weights are not publicly available during journal review.
    This demo shows the inference interface only.
    """
    model = VLLiNet(num_classes=2, pretrained=False)

    if checkpoint_path:
        # Placeholder - weights not included
        print("⚠️  Pretrained weights not available during journal review")

    model.eval()
    return model

def inference(model, rgb_image, lidar_points, calib):
    """
    Run inference on RGB image and LiDAR point cloud.

    Args:
        model: VLLiNet model
        rgb_image: RGB image [H, W, 3]
        lidar_points: LiDAR point cloud [N, 4]
        calib: Camera calibration

    Returns:
        pred_mask: Binary road segmentation [H, W]
    """
    # Generate ADI from LiDAR
    adi = generate_adi(lidar_points, calib, rgb_image.shape[:2])

    # Preprocess inputs
    rgb_tensor = torch.from_numpy(rgb_image).permute(2, 0, 1).unsqueeze(0).float()
    adi_tensor = torch.from_numpy(adi).unsqueeze(0).unsqueeze(0).float()

    # Inference
    with torch.no_grad():
        output = model(rgb_tensor, adi_tensor)
        pred_mask = torch.argmax(output, dim=1).squeeze().cpu().numpy()

    return pred_mask

if __name__ == "__main__":
    print("VLLiNet Inference Demo")
    print("=" * 50)
    print("⚠️  This is a demonstration of the inference interface.")
    print("⚠️  Model weights are not included during journal review.")
    print("=" * 50)

    # Example usage
    model = load_model()
    print(f"Model parameters: {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M")
