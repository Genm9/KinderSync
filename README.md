# KinderSync
## AI-Assisted Multi-Camera Kindergarten Graduation Video Editing Pipeline

KinderSync is a semi-automated video editing pipeline designed to help kindergarten teachers create graduation highlight videos from four camera angles with minimal effort and high ethical standards.

### Features
- **Audio-Based Sync**: Automatically aligns four camera recordings.
- **AI Recommendation**: Rule-based camera selection.
- **Human-in-the-Loop**: Mandatory human review of all editing decisions (EDL).
- **Automated Rendering**: Assembles final video with titles, credits, and transitions using MoviePy.

### Project Structure
- `data/`: Raw video and audio footage.
- `synchronization/`: Audio alignment logic.
- `analysis/`: Event detection and camera selection rules.
- `edl/`: Editing Decision List generation and human review tool, and display EDL.json.
- `renderer/`: MoviePy-based video assembly.
- `outputs/`: Display final video.
- `main.py`: Main pipeline orchestrator.

### Prerequisites
- Python 3.9 or higher (developed and tested with Python 3.13)
- [ffmpeg](https://ffmpeg.org/download.html) installed and available on your system PATH 
  (required by `moviepy` and `ffmpeg-python` for video encoding/decoding)
- ImageMagick installed if you encounter `TextClip` rendering errors on MoviePy v1.x 
  (MoviePy v2.x uses Pillow by default)
  
### How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place MP4 files in `data/videos/`.
3. Run the pipeline:
   ```bash
   python main.py
   ```
4. Review the generated `edl/edl.json` and approve via the prompt.
5. Find the final video in `outputs/`.

### Ethical Compliance
This project adheres to Malaysia's PDPA 2010 and responsible AI principles:
- **Local Processing**: No footage is uploaded to the cloud. All video and audio 
  processing—synchronization, analysis, and rendering—runs entirely on local hardware. 
  No footage or metadata is ever sent to third-party APIs or external cloud services.
- **Human Oversight**: Every cut is reviewed by a human editor.
- **Privacy by Design**: No facial recognition or child identification.
- **Sample Data Disclaimer**: The sample video/audio files included in this repository 
  (e.g. `graduation_highlight.mp4`, `Camera1_mp4__sample_.txt`) are provided for 
  demonstration purposes only. Before using this pipeline with real footage, users 
  must independently obtain explicit consent from the parents/guardians of every 
  child appearing in the recordings, in accordance with local child protection and 
  privacy regulations.
