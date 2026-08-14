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
- `output/`: Display final video.
- `main.py`: Main pipeline orchestrator.

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

Audio alignment (supplementing or backing up audalign)

scipy — cross-correlation for computing sync offsets; useful as a fallback if audalign misbehaves
librosa or soundfile — reading audio tracks, feature extraction
pydub — audio slicing and format conversion (needs ffmpeg)

Video processing

imageio + imageio-ffmpeg — moviepy's underlying writer dependencies; listing them explicitly is more reliable
Pillow — frame-level image work, watermarks, subtitle overlays
scikit-image — frame differencing and similarity comparison, if you're doing visual sync or transition detection

Workflow and usability

tqdm — progress bars for long renders
matplotlib — waveform and correlation plots; these go straight into your report
pyyaml or python-dotenv — pull paths and parameters out into a config file
loguru — logging that's easier to write than print statements

If there's an AI shot-selection or subject-tracking component

ultralytics (YOLO) or mediapipe — person detection, auto-framing
scikit-learn — shot clustering, scene segmentation

Development and quality (relevant to your BTSE2113 coursework)

pytest — unit testing
black, flake8, or ruff — formatting and static analysis

One practical warning: pin your versions, especially moviepy. The API changed substantially between 1.x and 2.x (moviepy.editor was removed in 2.x), so an unpinned file will break on a different machine. Either moviepy==1.0.3 or moviepy>=2.0 is fine, but be explicit about which.

Want me to generate a grouped, commented, version-pinned requirements.txt for you?




### Ethical Compliance
This project adheres to Malaysia's PDPA 2010 and responsible AI principles:
- **Local Processing**: No footage is uploaded to the cloud.
- **Human Oversight**: Every cut is reviewed by a human editor.
- **Privacy by Design**: No facial recognition or child identification.
