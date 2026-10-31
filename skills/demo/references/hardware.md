# Machine constraints

User-confirmed hardware, verified locally on 2026-10-31: Apple M3, arm64, 8 GiB unified memory. Treat this as the default machine profile for future runs. Recheck the actual target if the user chooses a different machine; do not apply this machine's constraints to a remote worker without inspecting it.

Blender is optional. Its published requirements list 8 GB as minimum and 32 GB recommended. That makes light work plausible, not heavy scenes or long Cycles renders reliably comfortable. This explainer is a 2D composition and does not need Blender. If the user explicitly wants 3D, first try a minimal scene in Workbench or Eevee, simple materials, modest geometry and low-resolution single-frame/short-segment tests. Record actual results; do not guarantee support from RAM alone. Avoid fluid/smoke simulations, large texture sets, dense geometry, subdivision and GPU rendering assumptions. Escalate to simpler 2D or an authorized stronger machine if measured resource limits require it.

## Local budget

- One heavy stage at a time: synthesize, release the model/process, align, release that model, then render. Do not keep ASR, TTS, Blender and a rendering browser resident together.
- Prefer a cached small local voice and small English/multilingual ASR model appropriate to the language. Start transcription on CPU with supported quantization if needed. Do not assume CUDA or Metal support in a Python package merely because the Mac has an Apple GPU.
- A 540×960 30fps draft is one-quarter the pixels of 1080×1920. Final 1080p remains the goal only when tests support it; low memory is not a reason to silently upscale a 540p render and label it native 1080p.
- Keep textures small and reuse vector shapes. Avoid large live blurs, noise canvases, huge SVG filter regions and simultaneous videos. Use existing supported lightweight grain/effect assets or skip decorative effects.
- Prefer streamed encoding over lossless frame sequences when supported. Estimate scratch usage from measured sample bytes per frame × total frames plus audio, final encode and downloads. Check the actual free space at the output filesystem, leaving headroom for macOS swap. At setup this machine had about 16 GiB free; that is an observation, not a permanent capacity guarantee.
- Do not delete the user's caches, models or unrelated files to make room. Remove only scratch files created by this run after preserving final evidence and editable sources. Record paths so cleanup can be scoped safely.

## Sources to recheck when choosing software

- [Blender requirements](https://www.blender.org/download/requirements/)
- [Blender macOS installation](https://docs.blender.org/manual/en/latest/getting_started/installing/macos.html)
- [Kokoro local TTS](https://github.com/hexgrad/kokoro)
- [faster-whisper requirements and quantization](https://github.com/SYSTRAN/faster-whisper)

Tool availability and hardware support must be verified at invocation time. No Blender or model runtime is installed merely by installing this skill.
