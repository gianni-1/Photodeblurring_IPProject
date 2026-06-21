# Detailed step-by-step project plan (Group 1: Pietro & Gianni)

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

1. Write the model `g = Af + epsilon`, with `A` as convolution by the motion PSF.
2. Analyze the Fourier magnitude of the PSF. Motion blur creates frequencies close to zero, so direct inversion amplifies noise.
3. Apply SVD and analyze the condition number in order to gain information about how stable the inversion would be
4. Compute condition-number proxies:
   - minimum/maximum nonzero Fourier response,
   - number of near-zero frequencies below chosen thresholds,
5. Create report plots:
   - PSF image,
   - Singular values
   - log Fourier magnitude,
   - frequency-response or singular-value proxy.

Expected output:
- Figure explaining why motion deblurring is ill-posed.
- Short paragraph connecting the plots to inverse-problem theory.

## Step 3 - Standard baseline with parameter optimization (2026-06-22 to 2026-06-25)

**Tikhonov deconvolution**.

1. Apply Tikhonov.
2. Use L-Curve concept to find the best lambda value.
3. Inspect visual quality to avoid relying only on metrics.
4. Record runtime.


Expected output:
- Best `lambda` or iteration count per noise/blur setting.
- Clean/blurred/restored comparison figure.

## Step 4 - Sparse method (2026-06-25 to 2026-06-28)

**Matching pursuit with Haar wavelet transformation matrix**.


1. Represent the image in the Haar wavelet basis: $$ g' = Af = A\Psi s = \Phi s, $$
where $\Psi$ is the transform into the sparse space (Haar wavelet matrix), and  $\Phi = A\Psi$.
2. Apply the Matching Pursuit algorithm to iteratively recover the sparse wavelet coefficients.
3. Signal processesing with zero padding in all dimensions 
4. Signal processesing with zero padding in one dimension



Expected output:
- Figure illustrating where sparse wavelet reconstruction improves or fails compared to Tikhonov.

## Step 5 - Recent method comparison (2026-06-28 to 2026-07-01)
(Here we want to look for methods that weren't presented in the lecture and are still open for new methods)

Preferred recent method: **plug-and-play/deep-denoiser prior**, for example DPIR (https://github.com/cszn/DPIR).

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
| Forward model and blur generation | Pietro | Gianni |
| Ill-posedness plots | Pietro | Gianni |
| Standard method and tuning | Pietro | Gianni |
| Sparse method | Gianni | Pietro |
| Recent method | Gianni | Pietro |
| Literature and references | Gianni | Pietro |
| Final report integration | Both | Both |
| Final zip/presentation check | Both | Both |
