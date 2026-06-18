# AGENTS.md - Photo Deblurring Inverse Problems Project

## Project context

This repository is for the Inverse Problems Exercises 2026s Phase B project.

Chosen topic: **Photo deblurring**

Assignment summary from `IP_Exercises_phaseB.pdf`:
- Data: apply different motion blur kernels to colorful landscape photos.
- Task: deblur the output images.
- Evaluate how severely the problem is ill-posed.
- Include one standard method with parameter optimization.
- Include one sparse method.
- Compare one recently developed technique.
- Search relevant literature and cite it.
- Produce one clearly organized report with references.
- Short plan due: **2026-06-21**.
- Final answer due: **2026-07-05**.
- Presentation slot: **2026-07-08** or **2026-07-15**.

## Team setup

This is a two-person student project, not a large ML challenge repository. Keep the workflow lightweight.

Suggested split:

- **Person A - modelling and experiments:** blur simulation, forward operator, ill-posedness analysis, standard baseline, metrics, experiment scripts.
- **Person B - sparse/recent methods and report:** sparse regularization method, recent-method comparison, literature notes, report writing, final figures.
- **Both:** review the final results, final report, zip contents, and presentation story.


## Repository structure

Use this simple structure:

```text
project-root/
├── AGENTS.md
├── README.md
├── requirements.txt
├── configs/              # Small YAML/JSON experiment settings
├── data/                 # Local-only data and generated images, normally gitignored
│   ├── raw/              # Original landscape photos or data instructions
│   ├── processed/        # Generated blurred/noisy images
│   └── results/          # Restored images and result tables
├── docs/                 # Assignment summary, plan, literature notes
├── logs/agent_changes/   # Short daily notes for non-trivial agent changes
├── report/               # Report draft/source and final figures
│   └── figures/
├── scripts/              # Reproducible command-line scripts
├── src/photodeblur/      # Reusable Python code
└── tests/                # Lightweight tests/smoke checks
```

Do not make the structure more complicated unless the project clearly needs it.

## Technical direction

Use the degradation model

```text
y = Kx + eta
```

where `x` is the clean RGB image, `K` is a motion-blur convolution operator / point-spread function, and `eta` is optional additive noise.

Minimum method comparison:

1. **Standard method:** Wiener/Tikhonov deconvolution or Richardson-Lucy, with parameter optimization.
2. **Sparse method:** TV-regularized deconvolution or wavelet-L1 deconvolution, with parameter optimization.
3. **Recent method:** plug-and-play/deep-denoiser prior such as DPIR, or a simpler recent published alternative if setup time is limited.

Minimum evaluation:

- Ill-posedness: Fourier response of the blur kernel, near-zero frequencies, condition-number proxy, and noise amplification.
- Quantitative metrics: PSNR and SSIM on synthetic data where the clean image is known.
- Qualitative comparisons: clean, blurred, restored image, and preferably zoom/error crops.
- Runtime and parameter sensitivity for the main methods.

## Coding rules

- Use Python 3.
- Keep reusable code in `src/photodeblur/`.
- Keep executable experiments in `scripts/`.
- Keep notebooks exploratory; do not hide final pipeline logic in notebooks.
- Use fixed random seeds for reproducible synthetic blur/noise generation.
- Put experiment settings in `configs/`, not hardcoded inside scripts.
- Save generated images/results under `data/processed/`, `data/results/`, or `report/figures/`.
- Do not commit large generated data, model weights, caches, private data, or local machine paths.
- Use clear English names, comments, and documentation.
- Prefer small, readable functions over clever abstractions.

## Agent change logging

For non-trivial agent changes, append a short entry to:

```text
logs/agent_changes/YYYY-MM-DD.md
```

Include:
- time,
- files changed,
- what changed,
- why it changed,
- validation performed or why it was not run.

This is intentionally lighter than a full research-engineering log.

## Report expectations

The report should be understandable without reading the code. Include:

1. Problem statement and forward model.
2. Ill-posedness discussion with plots.
3. Standard method and parameter selection.
4. Sparse method and parameter selection.
5. Recent method and how it was applied.
6. Experimental setup, metrics, and results.
7. Discussion of strengths, weaknesses, artifacts, and limitations.
8. References.

## Submission checklist

Before creating `IP_2026s_{LastName}_{GroupName}.zip`:

- [ ] The short plan has been submitted by **2026-06-21**.
- [ ] Code runs from a clean checkout after installing `requirements.txt`.
- [ ] Data generation is reproducible from source images or documented input paths.
- [ ] Final report source and figures are included.
- [ ] No large generated caches, private files, or local absolute paths are included.
- [ ] Both team members checked the final report, plots, and presentation outline.
