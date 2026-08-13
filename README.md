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
- `edl/`: Editing Decision List generation and human review tool.
- `renderer/`: MoviePy-based video assembly.
- `output/`: Display final video & EDL.
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

### Ethical Compliance
This project adheres to Malaysia's PDPA 2010 and responsible AI principles:
- **Local Processing**: No footage is uploaded to the cloud.
- **Human Oversight**: Every cut is reviewed by a human editor.
- **Privacy by Design**: No facial recognition or child identification.
