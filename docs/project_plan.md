# Detailed step-by-step project plan

## Goal

Solve and explain the photo deblurring inverse problem for synthetically motion-blurred colorful landscape images. The project should demonstrate the forward model, ill-posedness, one standard method, one sparse method, and one recent method, with clear evaluation and references.

## Step 1 - Confirm scope and data (2026-06-18 to 2026-06-19)

1. Select 3-5 public or self-owned colorful landscape images.
2. Store originals locally in `data/raw/` but do not commit large images.
3. Resize/crop images to a consistent size, for example 512 x 512.
4. Implement or verify a motion-blur point-spread function (PSF): length and angle.
5. Generate blurred images for several blur severities and optional Gaussian noise levels.
6. Save generation settings in `configs/default.yaml`.

Expected output:
- Clean/blurred image examples.
- A small table of blur lengths, angles, and noise levels.

## Step 2 - Forward model and ill-posedness (2026-06-19 to 2026-06-22)

1. Write the model `y = Kx + eta`, with `K` as convolution by the motion PSF.
2. Analyze the Fourier magnitude of the PSF. Motion blur creates frequencies close to zero, so direct inversion amplifies noise.
3. Compute condition-number proxies:
   - minimum/maximum nonzero Fourier response,
   - number of near-zero frequencies below chosen thresholds,
   - visual inverse-filter noise amplification.
4. Create report plots:
   - PSF image,
   - log Fourier magnitude,
   - frequency-response or singular-value proxy.

Expected output:
- Figure explaining why motion deblurring is ill-posed.
- Short paragraph connecting the plots to inverse-problem theory.

## Step 3 - Standard baseline with parameter optimization (2026-06-22 to 2026-06-25)

Recommended baseline: **Wiener/Tikhonov deconvolution**.

1. Implement frequency-domain deconvolution:
   `x_hat = conj(H) / (|H|^2 + lambda) * y_hat`.
2. Sweep `lambda` over a logarithmic grid.
3. Select the best parameter by PSNR/SSIM on synthetic validation images.
4. Inspect visual quality to avoid relying only on metrics.
5. Record runtime.

Alternative if easier: Richardson-Lucy with iteration count as parameter.

Expected output:
- Best `lambda` or iteration count per noise/blur setting.
- PSNR/SSIM table.
- Clean/blurred/restored comparison figure.

## Step 4 - Sparse method (2026-06-25 to 2026-06-28)

Recommended sparse method: **TV-regularized deconvolution**.

1. Formulate optimization:
   `min_x 0.5 ||Kx - y||_2^2 + alpha TV(x)`.
2. Implement with a primal-dual, ADMM, or available image-processing solver.
3. Sweep `alpha` and choose it by validation PSNR/SSIM.
4. Compare edge preservation, ringing, and staircase artifacts against Wiener/Tikhonov.

Fallback sparse method: wavelet-L1 deconvolution if TV implementation becomes too time-consuming.

Expected output:
- Parameter sweep for `alpha`.
- Quantitative comparison to the standard baseline.
- Figure showing where sparse regularization helps or fails.

## Step 5 - Recent method comparison (2026-06-28 to 2026-07-01)

Preferred recent method: **plug-and-play/deep-denoiser prior**, for example DPIR.

1. Check implementation feasibility and dependency size.
2. Use the same blurred inputs and PSFs as the other methods.
3. If DPIR is feasible, run it as the modern comparison method.
4. If GPU/model setup is not feasible, use a smaller plug-and-play ADMM variant and explain the limitation.
5. Compare quality, artifacts, runtime, and robustness.

Expected output:
- At least one modern-method result on the main test image.
- Discussion of whether modern priors outperform the model-based baselines.

## Step 6 - Final experiments and figures (2026-07-01 to 2026-07-03)

1. Freeze a small final benchmark: for example 3 images x 2 blur settings x 2 noise settings.
2. Run all selected methods with tuned parameters.
3. Export plots and images to `report/figures/`.
4. Create final PSNR/SSIM and runtime tables.
5. Write interpretation, not just numbers.

Expected output:
- Final figures and tables ready for the report.

## Step 7 - Report and presentation (2026-07-03 to 2026-07-05)

1. Complete the report draft in `report/short_report_draft.md` or convert it to LaTeX if required.
2. Ensure every method has equations, parameters, and references.
3. Add limitations: boundary effects, non-blind assumption, kernel mismatch, and noise sensitivity.
4. Proofread and verify reproducibility instructions.
5. Create the final source zip named according to Moodle instructions.
6. Book/confirm presentation slot for **2026-07-08** or **2026-07-15**.

## Two-person responsibility split

| Area | Owner | Reviewer |
| --- | --- | --- |
| Forward model and blur generation | Person A | Person B |
| Ill-posedness plots | Person A | Person B |
| Standard method and tuning | Person A | Person B |
| Sparse method | Person B | Person A |
| Recent method | Person B | Person A |
| Literature and references | Person B | Person A |
| Final report integration | Both | Both |
| Final zip/presentation check | Both | Both |
