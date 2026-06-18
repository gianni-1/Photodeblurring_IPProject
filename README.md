# Photodeblurring_IPProject

Two-person project for the Inverse Problems Exercises 2026s Phase B assignment.

Chosen topic: **photo deblurring**. We synthesize motion blur on colorful landscape images and reconstruct the sharp images with inverse-problem methods.

## Deliverables

- Short plan due **2026-06-21**: `docs/short_plan_for_submission.md`
- Final answer due **2026-07-05**
- Presentation slot on **2026-07-08** or **2026-07-15**
- Report draft/source: `report/short_report_draft.md`

## Planned methods

1. Standard method: Wiener/Tikhonov deconvolution or Richardson-Lucy.
2. Sparse method: TV-regularized or wavelet-L1 deconvolution.
3. Recent method: plug-and-play/deep-denoiser prior such as DPIR, if feasible.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Main folders

- `docs/` - assignment summary, literature notes, project plan.
- `src/photodeblur/` - reusable implementation code.
- `scripts/` - reproducible experiment scripts.
- `report/` - report draft and final figures.
- `data/` - local data and generated outputs, not committed except placeholders.
