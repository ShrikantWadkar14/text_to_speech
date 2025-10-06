# Text-to-Speech (Parler TTS) — Example CLI

This repository contains a simple example that uses the Parler TTS model to generate speech from text using a sample voice profile.

Files
- `parler_terminal_tts.py` — Main script. It analyzes a sample voice WAV to derive a short description, then synthesizes text input to WAV files using the `ai4bharat/indic-parler-tts` model.
- `requirements.txt` — Project dependencies (best-effort). See notes below about `torch` and `parler_tts`.
- `SHUBHAM VO_MARATHI.wav`, `tts_1.wav`, `tts_2.wav` — example audio files.

Quick features
- Analyze a sample WAV to infer pitch, tempo, and energy and form a descriptive prompt.
- Accept text input from the terminal and generate WAV files.
- Plays generated WAV files on Windows using Windows Media Player.

Requirements
- Python 3.10+ recommended.
- See `requirements.txt` for the main Python packages. Important notes:
  - `torch` often requires a specific wheel for CUDA; if you need GPU support, install the correct PyTorch wheel from https://pytorch.org first.
  - The code imports `parler_tts`. If that package is not available on PyPI, you may need to install it from source (GitHub). The `requirements.txt` contains a commented example for git+ installation.

Install (Windows, cmd.exe)
1. Create and activate a virtual environment (recommended):

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Upgrade pip and install packages:

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. If you need GPU-enabled torch, install it as instructed on PyTorch website. Example (CPU-only wheel):

```cmd
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

4. If `parler_tts` must be installed from GitHub, run (adjust URL if required):

```cmd
pip install git+https://github.com/ai4bharat/parler-tts.git#egg=parler-tts
```

Usage
1. Place a sample voice file named `SHUBHAM VO_MARATHI.wav` (or update `parler_terminal_tts.py` to point to your file).
2. Run the script:

```cmd
python parler_terminal_tts.py
```

3. Type any text and press Enter. The script will generate `tts_1.wav`, `tts_2.wav`, ... and play them via Windows Media Player.

Notes and troubleshooting
- If the script fails importing `parler_tts`, it means that package isn't installed. Try installing from GitHub or check the correct package name.
- If you have CUDA and want GPU inference, ensure `torch` with the correct CUDA version is installed and a compatible GPU is present.
- `librosa` may require a working C compiler and some system libraries for audio; on Windows, installing the wheels via pip usually suffices.

How to upload to GitHub (Windows cmd.exe)
1. Initialize repo (if not already):

```cmd
git init
git add .
git commit -m "Initial commit"
```

2. Add remote and push (replace URL and branch as needed):

```cmd
git remote add origin https://github.com/shrikantwadkar14/text_to_speech.git
git branch -M main
git push -u origin main
```

Replace `<username>` with your GitHub username. If prompted, provide credentials or use a personal access token.

License
This repository contains example code. Check third-party license terms for the models and libraries used.

Want me to also:
- Pin exact package versions based on a test environment?
- Create a small test that imports modules to validate the environment?
If yes, tell me which you'd like and I'll add it.
