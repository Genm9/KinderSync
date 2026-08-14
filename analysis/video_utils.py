import os
import cv2

def get_video_metadata(file_path):
    """
    Extracts metadata from a video file.
    """
    if not os.path.exists(file_path):
        return {"error": f"File {file_path} does not exist."}
    
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        return {"error": f"Could not open video file {file_path}."}
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    cap.release()
    
    return {
        "file_name": os.path.basename(file_path),
        "resolution": f"{width}x{height}",
        "fps": round(fps, 2),
        "duration": round(duration, 2),
        "frame_count": frame_count
    }

def validate_videos(video_paths):
    """
    Validates multiple video files and returns their metadata.
    """
    results = []
    for path in video_paths:
        results.append(get_video_metadata(path))
    return results

if __name__ == "__main__":
    # Example usage
    test_videos = [
        "data/videos/Camera1_Left.mp4",
        "data/videos/Camera2_Right.mp4",
        "data/videos/Camera3.mp4",
        "data/videos/Camera4.mp4"
    ]
    # Note: These files might not exist yet in the sandbox environment
    print(validate_videos(test_videos))
