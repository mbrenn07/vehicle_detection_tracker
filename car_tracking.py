from VehicleDetectionTracker.VehicleDetectionTracker import VehicleDetectionTracker
from torch import torch

# Save original torch.load function
_original_torch_load = torch.load  

# Define a patched version
def patched_torch_load(*args, **kwargs):
    kwargs["weights_only"] = False  # Override default
    return _original_torch_load(*args, **kwargs)

# Apply the patch
torch.load = patched_torch_load

video_path = "./dashcam.mp4"
vehicle_detection = VehicleDetectionTracker()
result_callback = lambda result: print({
    "number_of_vehicles_detected": result["number_of_vehicles_detected"],
    "detected_vehicles": [
        {
            "vehicle_id": vehicle["vehicle_id"],
            "vehicle_type": vehicle["vehicle_type"],
            "detection_confidence": vehicle["detection_confidence"],
            "color_info": vehicle["color_info"],
            "model_info": vehicle["model_info"],
            "speed_info": vehicle["speed_info"]
        }
        for vehicle in result['detected_vehicles']
    ]
})
vehicle_detection.process_video(video_path, result_callback)