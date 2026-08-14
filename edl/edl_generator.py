import json
import os

def generate_edl(recommendations, output_path="edl/edl.json"):
    """
    Saves the camera recommendations to a structured EDL file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    edl_data = {
        "project": "KinderSync Graduation 2026",
        "version": "1.0",
        "status": "pending_review",
        "segments": recommendations
    }
    
    with open(output_path, 'w') as f:
        json.dump(edl_data, f, indent=4)
    
    print(f"EDL generated and saved to {output_path}")
    return output_path

def load_edl(file_path="edl/edl.json"):
    """
    Loads the EDL data for review or rendering.
    """
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    # Mock recommendations for testing
    mock_recommendations = [
        {"start": 0, "end": 10, "camera": "camera1", "reason": "Speech", "transition": "fade"},
        {"start": 10, "end": 20, "camera": "camera3", "reason": "Applause", "transition": "cut"}
    ]
    generate_edl(mock_recommendations)
