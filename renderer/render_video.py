from moviepy import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import moviepy.video.fx as vfx
import json
import os

class VideoRenderer:
    def __init__(self, edl_path="edl/edl.json", video_dir="data/videos", sync_path="data/sync_data.json"):
        self.edl_path = edl_path
        self.video_dir = video_dir
        self.sync_path = sync_path
        self.output_dir = "outputs"
        os.makedirs(self.output_dir, exist_ok=True)

    def load_sync_data(self):
        if not os.path.exists(self.sync_path):
            return {}
        with open(self.sync_path, 'r') as f:
            return json.load(f)

    def load_edl(self):
        if not os.path.exists(self.edl_path):
            raise FileNotFoundError(f"EDL file not found: {self.edl_path}")
        with open(self.edl_path, 'r') as f:
            return json.load(f)

    def create_caption(self, seg, duration):
        """
        Creates a bottom-aligned caption for each segment.
        """
        try:
            # Format: SEG X  camera_name
            # Reason text on second line
            header = f"SEG {seg.get('seg_id', '?')}  {seg['camera']}"
            reason = seg['reason']
            
            caption_text = f"{header}\n{reason}"
            
            caption = TextClip(
                text=caption_text,
                font_size=24,
                color='white',
                bg_color='black',
                size=(1280, 120),
                method='caption'
            ).with_duration(duration).with_position(('center', 'bottom')).with_opacity(0.6)
            
            return caption
        except Exception as e:
            print(f"Error creating caption: {e}")
            return None

    def render(self, output_name="graduation_highlight.mp4"):
        edl_data = self.load_edl()
        sync_offsets = self.load_sync_data()
        
        if edl_data.get('status') != 'approved':
            print("Warning: EDL is not approved. Rendering blocked for ethical compliance.")
            return None

        # 1. Prepare Master Audio (aligned to Camera1_Left)
        master_audio_path = os.path.join(self.video_dir, "Camera1_Left.mp4")
        master_audio = None
        if os.path.exists(master_audio_path):
            print("Loading Master Audio from Camera1_Left...")
            master_audio = VideoFileClip(master_audio_path).audio

        clips = []
        
        # Add Opening Title
        try:
            title_text = "Kindergarten Graduation Ceremony\n2026\n\nMulti-Camera Highlight"
            title = TextClip(text=title_text, font_size=60, color='white', size=(1680, 750), bg_color='black').with_duration(5)
            clips.append(title)
        except Exception as e:
            print(f"Skipping Title Clip: {e}")

        for seg in edl_data['segments']:
            video_path = os.path.join(self.video_dir, f"{seg['camera']}.mp4")
            offset = sync_offsets.get(seg['camera'], 0.0)
            
            if os.path.exists(video_path):
                # Calculate sync-aligned file start/end
                # Master Time = File Time + Offset -> File Time = Master Time - Offset
                actual_start = seg['start'] - offset
                actual_end = seg['end'] - offset
                
                print(f"Processing {seg['camera']}: Master {seg['start']}-{seg['end']} -> File {actual_start:.1f}-{actual_end:.1f} (Offset: {offset})")
                
                # Check if the requested segment exists in the file
                if actual_start < 0:
                    print(f"Warning: Segment starts before {seg['camera']} recording began. Adjusting start.")
                    actual_start = 0
                
                clip = VideoFileClip(video_path).subclipped(actual_start, actual_end)
                
                # Remove individual clip audio to use master audio instead
                if master_audio:
                    clip = clip.without_audio()
                
                # Apply transition (simplified)
                if seg['transition'] == 'fade':
                    clip = clip.with_effects([vfx.FadeIn(0.5), vfx.FadeOut(0.5)])
                
                # Add caption overlay
                caption = self.create_caption(seg, clip.duration)
                if caption:
                    clip = CompositeVideoClip([clip, caption])
                
                clips.append(clip)
            else:
                print(f"Clip not found: {video_path}. Skipping segment.")

        # Add Closing Credits
        try:
            credits_text = (
                "Recorded using a four-camera setup.\n"
                "Synchronized via audio onset cross-correlation.\n\n"
                "Edited utilizing a machine-readable Edit Decision List (EDL), \n"
                "with every cut meticulously reviewed and approved by a human editor.\n"
                "Produced through a semi-automated pipeline to ensure quality control, rather than full automation.\n\n"
                "All footage was processed entirely offline; no video data was uploaded to any cloud service.\n"
                "Recorded and shared with the explicit consent of all participants and their guardians."
            )
            credits = TextClip(text=credits_text, font_size=30, color='white', size=(1680, 750), bg_color='black').with_duration(8)
            clips.append(credits)
        except Exception as e:
            print(f"Skipping Credits Clip: {e}")

        if not clips:
            print("No clips to render.")
            return None

        final_video = concatenate_videoclips(clips, method="compose")
        
        # Attach Master Audio (simplified alignment)
        if master_audio:
            # We assume the master audio duration covers the timeline
            final_audio = master_audio.subclipped(0, final_video.duration)
            final_video = final_video.with_audio(final_audio)

        output_path = os.path.join(self.output_dir, output_name)
        
        # Write the final video file
        print(f"Rendering final video to: {output_path}...")
        final_video.write_videofile(output_path, codec="libx264", fps=24)
        
        # Explicitly close clips
        final_video.close()
        if master_audio: master_audio.close()
        for clip in clips:
            clip.close()
        
        return output_path

if __name__ == "__main__":
    renderer = VideoRenderer()
    renderer.render()
