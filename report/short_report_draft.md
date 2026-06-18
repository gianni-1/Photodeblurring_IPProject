# Photo Deblurring as an Inverse Problem

> Draft report skeleton. Replace placeholders with final figures, tables, and conclusions after experiments.

## 1. Introduction

The aim of this project is to reconstruct sharp colorful landscape images from synthetically motion-blurred observations. The project follows the Phase B photo deblurring task: generate blurred images by applying different motion-blur kernels and then compare inverse-problem reconstruction methods.

## 2. Forward model

Let `x` denote the unknown clean RGB image and `y` the observed blurred image. We model the degradation as

```text
y = Kx + eta,
```

where `K` is a convolution matrix corresponding to a motion-blur point-spread function (PSF), and `eta` is optional additive noise. For a spatially invariant blur, the convolution can be analyzed efficiently in the Fourier domain.

## 3. Ill-posedness

Motion blur suppresses image frequencies perpendicular to the motion direction. In the Fourier domain, deconvolution would divide by the blur transfer function `H`. If `|H|` is very small, direct inversion strongly amplifies noise and numerical errors. We will quantify this by plotting:

- the PSF,
- `log(|H|)`,
- the distribution of near-zero frequencies,
- example direct-inverse reconstructions showing noise amplification.

## 4. Standard method: Wiener/Tikhonov deconvolution

The first baseline solves a regularized least-squares problem:

```text
min_x 0.5 ||Kx - y||_2^2 + 0.5 lambda ||x||_2^2.
```

For convolution with periodic boundary assumptions, the solution can be computed in the Fourier domain:

```text
x_hat = conj(H) / (|H|^2 + lambda) * y_hat.
```

The regularization parameter `lambda` will be selected by a logarithmic grid search using validation PSNR and SSIM.

## 5. Sparse method: TV-regularized deconvolution

Natural images are approximately sparse in their gradients. We therefore compare the standard method with a total-variation model:

```text
min_x 0.5 ||Kx - y||_2^2 + alpha TV(x).
```

The parameter `alpha` controls the balance between data fidelity and edge-preserving regularity. We will evaluate whether TV reduces ringing/noise amplification compared with Wiener/Tikhonov deconvolution.

## 6. Recent method comparison

As a modern comparison, we plan to use a plug-and-play/deep-denoiser prior method such as DPIR. These methods keep the physical degradation model but replace an explicit hand-written regularizer with a powerful denoising prior. If the full DPIR setup is too heavy for the project environment, we will use a smaller plug-and-play ADMM variant and state the limitation clearly.

## 7. Experiments

Planned benchmark:

- 3-5 landscape images,
- motion-blur lengths such as 9, 17, and 31 pixels,
- angles such as 0, 30, 60, and 90 degrees,
- Gaussian noise levels such as 0, 0.01, and 0.03,
- metrics: PSNR, SSIM, and runtime.

Final report figures should include clean, blurred, and reconstructed images for all compared methods.

## 8. Expected discussion points

- Larger blur kernels create stronger loss of high-frequency information.
- Direct inverse filtering is unstable because of near-zero Fourier coefficients.
- Standard regularization is fast and interpretable, but may oversmooth or ring.
- Sparse TV regularization can preserve edges but may create staircase artifacts.
- Modern denoiser priors may produce visually better images but require more dependencies and may be less transparent.

## References

- W. H. Richardson, "Bayesian-Based Iterative Method of Image Restoration," Journal of the Optical Society of America, 1972. https://ui.adsabs.harvard.edu/abs/1972JOSA...62...55R/abstract
- L. B. Lucy, "An iterative technique for the rectification of observed distributions," The Astronomical Journal, 1974.
- L. Rudin, S. Osher, and E. Fatemi, "Nonlinear total variation based noise removal algorithms," Physica D, 1992. https://web.eecs.utk.edu/~hqi/ece692/references/noise-TV-PhysicaD92.pdf
- A. Beck and M. Teboulle, "A fast iterative shrinkage-thresholding algorithm for linear inverse problems," SIAM Journal on Imaging Sciences, 2009.
- S. H. Chan, X. Wang, and O. A. Elgendy, "Plug-and-Play ADMM for Image Restoration: Fixed-Point Convergence and Applications," 2016. https://arxiv.org/abs/1605.01710
- K. Zhang et al., "Plug-and-Play Image Restoration with Deep Denoiser Prior," IEEE TPAMI, 2022. https://doi.org/10.1109/TPAMI.2021.3088914
