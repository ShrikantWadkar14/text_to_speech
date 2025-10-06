import torch, soundfile as sf, numpy as np
import librosa, os
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_id = "ai4bharat/indic-parler-tts"
model = ParlerTTSForConditionalGeneration.from_pretrained(model_id).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_id)
desc_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

def analyze_voice(wav_path):
    y, sr = librosa.load(wav_path, sr=16000, mono=True)
    y = librosa.util.normalize(y)
    pitch = librosa.yin(y, fmin=50, fmax=400, sr=sr)
    pitch = pitch[np.isfinite(pitch)]
    f0 = float(np.median(pitch)) if pitch.size else 175.0
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    rms = float(np.mean(librosa.feature.rms(y=y)))
    pitch_desc = "low" if f0 < 140 else ("high" if f0 > 220 else "moderate")
    speed_desc = "slow" if tempo < 85 else ("fast" if tempo > 115 else "moderate")
    energy_desc = "soft" if rms < 0.05 else ("strong" if rms > 0.12 else "balanced")
    desc = (
        f"A speaker with an Indian accent, {energy_desc} energy, {speed_desc} speaking rate, "
        f"{pitch_desc} pitch, natural prosody, close microphone, studio-quality, minimal background noise."
    )
    return desc

def synth(text, description, out_path):
    d = desc_tokenizer(description, return_tensors="pt").to(device)
    p = tokenizer(text, return_tensors="pt").to(device)
    gen = model.generate(
        input_ids=d.input_ids, attention_mask=d.attention_mask,
        prompt_input_ids=p.input_ids, prompt_attention_mask=p.attention_mask
    )
    audio = gen.cpu().numpy().squeeze()
    sf.write(out_path, audio, model.config.sampling_rate)

if __name__ == "__main__":
    voice_path = "SHUBHAM VO_MARATHI.wav"
    if not os.path.exists(voice_path):
        print("Please place your sample as 'voice_sample.wav'.")
        exit(1)
    voice_desc = analyze_voice(voice_path)
    print("Derived description:", voice_desc)
    i = 1
    print("Type text (any language) and press Enter. Ctrl+C to exit.")
    while True:
        try:
            text = input("> ").strip()
            if not text: continue
            out_file = f"tts_{i}.wav"
            synth(text, voice_desc, out_file)
            print(f"Saved {out_file}. Playing...")
            os.system(f'start wmplayer "{out_file}"')  # Windows Media Player playback
            i += 1
        except KeyboardInterrupt:
            break
