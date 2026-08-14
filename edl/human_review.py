import json
import os

def review_edl(file_path="edl/edl.json"):
    """
    Simulates the human review process.
    In a real app, this would be a UI where the user clicks 'Approve'.
    """
    if not os.path.exists(file_path):
        print(f"Error: EDL file {file_path} not found.")
        return False
    
    with open(file_path, 'r') as f:
        edl_data = json.load(f)
    
    print("--- HUMAN REVIEW STEP ---")
    print(f"Project: {edl_data.get('project')}")
    print(f"Current Status: {edl_data.get('status')}")
    print("\nSegments to Review:")
    for i, seg in enumerate(edl_data.get('segments', [])):
        print(f"[{i}] {seg['start']}s - {seg['end']}s | Cam: {seg['camera']} | Reason: {seg['reason']}")
    
    # Simulate approval
    confirm = input("\nDo you approve these edits? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        edl_data['status'] = 'approved'
        with open(file_path, 'w') as f:
            json.dump(edl_data, f, indent=4)
        print("EDL Approved! Proceeding to rendering...")
        return True
    else:
        print("EDL Rejected. Please modify the JSON file manually and try again.")
        return False

if __name__ == "__main__":
    # For demonstration, we'll auto-approve if running in a non-interactive environment
    # but the logic remains for the user to see.
    review_edl()
