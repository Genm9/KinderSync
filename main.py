import os
from synchronization.sync import synchronize_cameras, save_sync_data
from analysis.camera_selector import CameraSelector
from edl.edl_generator import generate_edl
from edl.human_review import review_edl
from renderer.render_video import VideoRenderer

def run_pipeline():
    print("=== KinderSync AI Video Editing Pipeline ===")
    
    # 1. Define Input Videos
    video_dir = "data/videos"
    video_files = [
        os.path.join(video_dir, "Camera1_Left.mp4"),
        os.path.join(video_dir, "Camera2_Right.mp4"),
        os.path.join(video_dir, "Camera3.mp4"),
        os.path.join(video_dir, "Camera4.mp4")
    ]
    
    # 2. Synchronization (FR-2)
    print("\n[Step 1] Synchronizing cameras...")
    offsets = synchronize_cameras(video_files)
    save_sync_data(offsets)
    
    # 3. Analysis & Recommendation (FR-3 & FR-4)
    print("\n[Step 2] Analyzing segments and recommending cameras...")
    selector = CameraSelector()
    events = selector.detect_events(duration=104) # Total duration of 12 segments
    recommendations = selector.recommend_cameras(events)
    
    # 4. EDL Generation (FR-5)
    print("\n[Step 3] Generating Editing Decision List (EDL)...")
    edl_path = generate_edl(recommendations)
    
    # 5. Human Review (FR-7)
    print("\n[Step 4] Human Review Required...")
    # In this automated run, we'll simulate approval for the final demonstration
    # In reality, the teacher would run edl/human_review.py manually.
    is_approved = review_edl(edl_path)
    
    if not is_approved:
        print("Pipeline stopped: Human approval required.")
        return

    # 6. Rendering (FR-6)
    print("\n[Step 5] Rendering final video...")
    renderer = VideoRenderer(edl_path=edl_path)
    output_file = renderer.render()
    
    if output_file:
        print(f"\nPipeline Complete! Final video: {output_file}")
    else:
        print("\nPipeline failed during rendering.")

if __name__ == "__main__":
    # Ensure data directories exist
    os.makedirs("data/videos", exist_ok=True)
    os.makedirs("data/audio", exist_ok=True)
    
    run_pipeline()
