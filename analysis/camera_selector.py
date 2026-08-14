import pandas as pd

class CameraSelector:
    def __init__(self):
        # 更新为用户定义的机位名称
        self.rules = {
            "wide": "Camera3",
            "performance": "Camera1_Left",
            "close_up": "Camera2_Right",
            "side_view": "Camera4"
        }

    def detect_events(self, duration):
        """
        模拟 10 个分段的事件检测。
        确保每个分段的 end > start，并且在对应相机的有效时长内。
        """
        base_time = 239.0
        
        events = [
            {"start": 239.0, "end": 249.0, "event": "close_up",    "reason": "Front-Right camera establishes the opening scene with a steady view of the stage entrance."},
            {"start": 249.0, "end": 270.0, "event": "performance", "reason": "Switching to the left-side angle to capture the performers' movement from a new perspective."},
            {"start": 270.0, "end": 280.0, "event": "close_up",    "reason": "Returning to the main front-right camera view to provide a clear, balanced look at the group choreography."},
            {"start": 280.0, "end": 290.0, "event": "performance", "reason": "Left-side framing highlights the detail of the performance as the children move across the stage."},
            {"start": 290.0, "end": 321.0, "event": "wide",        "reason": "Maintaining the front camera master angle for consistent coverage of the main routine."},
            {"start": 321.0, "end": 327.0, "event": "close_up",    "reason": "Switch to the right side to emphasize the energy and rhythm of the drum section."},
            {"start": 327.0, "end": 336.0, "event": "side_view",   "reason": "Front angle captures the full synchronised sequence with maximum clarity."},
            {"start": 336.0, "end": 342.0, "event": "performance", "reason": "Left-side perspective focuses on the performers' expressions during this emotional segment."},
            {"start": 342.0, "end": 360.0, "event": "close_up",    "reason": "Right camera establishes the full stage and scale of the hall for the grand finale."},
            {"start": 360.0, "end": 364.0, "event": "performance", "reason": "Left angle puts the audience in the foreground, showing the performance in its setting for the closing."},
        ]
        return events

    def recommend_cameras(self, events):
        """
        根据检测到的事件推荐机位，完全模拟 10 个分段的结构。
        所有时间均为 Master Timeline 时间（以 Camera1_Left 启动）。
        """
        recommendations = []
        for i, event in enumerate(events):
            seg_id = i + 1
            # 根据用户指定的 10 个分段机位顺序进行映射
            mapping = {
                1: "Camera2_Right",
                2: "Camera1_Left",
                3: "Camera2_Right",
                4: "Camera1_Left",
                5: "Camera3",
                6: "Camera2_Right",
                7: "Camera4",
                8: "Camera1_Left",
                9: "Camera2_Right",
                10: "Camera1_Left",
            }
            
            camera = mapping.get(seg_id, "Camera1_Left")
            
            # 设置转场逻辑：开头、中间衔接和结尾使用 fade，其余使用 cut
            transition = "cut"
            if seg_id in [1, 3, 6, 8, 10]:
                transition = "fade"
                
            recommendations.append({
                "seg_id": seg_id,
                "start": event["start"],
                "end": event["end"],
                "camera": camera,
                "reason": event["reason"],
                "transition": transition
            })
        return recommendations

if __name__ == "__main__":
    selector = CameraSelector()
    mock_events = selector.detect_events(60)
    recommendations = selector.recommend_cameras(mock_events)
    
    df = pd.DataFrame(recommendations)
    print("AI Recommended EDL:")
    print(df)
