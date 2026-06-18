# Short project plan for Moodle submission

**Topic:** Photo deblurring

**Team size:** 2 members

## Problem

We study non-blind photo deblurring for colorful landscape images. Clean images `x` will be degraded by synthetic motion blur and optional Gaussian noise according to

```text
y = Kx + eta,
```

where `K` is a convolution operator defined by a motion-blur point-spread function. The task is to reconstruct `x` from the blurred image `y` and known or estimated blur kernel.

## Planned methods

1. **Ill-posedness analysis:** inspect the Fourier response of the motion-blur kernel and show that small or near-zero frequencies make direct inversion unstable.
2. **Standard method:** implement Wiener/Tikhonov deconvolution, with the regularization parameter selected by validation PSNR/SSIM.
3. **Sparse method:** implement TV-regularized deconvolution, with the TV weight selected by a parameter sweep.
4. **Recent method:** compare a plug-and-play/deep-denoiser prior method such as DPIR if feasible; otherwise compare a simpler plug-and-play ADMM variant and explain the implementation constraint.

## Evaluation

We will generate a small benchmark of 3-5 landscape images, several blur lengths/angles, and at least two noise levels. Since the clean images are known, we will report PSNR and SSIM, plus visual comparisons and runtime. The report will include figures for the PSF, Fourier spectrum, restored images, and error/zoom crops.

## Work split

- **Person A:** data generation, forward model, ill-posedness analysis, standard baseline, metrics.
- **Person B:** sparse method, recent method comparison, literature review, report draft.
- **Both:** final result interpretation, report proofreading, and submission packaging.

## Schedule

- 2026-06-18 to 2026-06-21: finalize data, forward model, short plan.
- 2026-06-22 to 2026-06-25: implement standard baseline and parameter optimization.
- 2026-06-25 to 2026-06-28: implement sparse method.
- 2026-06-28 to 2026-07-01: run recent-method comparison.
- 2026-07-01 to 2026-07-05: final experiments, report, and source zip.
