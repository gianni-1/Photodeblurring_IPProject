# Literature notes for photo deblurring

These notes are a starting point for the final report bibliography and method choice.

## Classical/standard deconvolution

- Richardson (1972) and Lucy (1974) introduced the iterative Richardson-Lucy method, a likelihood/Bayesian deconvolution algorithm often used when the PSF is known.
- Wiener/Tikhonov deconvolution is a simple standard baseline for spatially invariant blur. It is especially useful here because the convolution model is diagonalized by the Fourier transform, making the effect of small Fourier coefficients transparent.

## Sparse/variational deconvolution

- Rudin, Osher, and Fatemi (1992) introduced total variation regularization. For deblurring, TV regularization can be used as `0.5 ||Kx-y||_2^2 + alpha TV(x)`.
- TV is a good sparse method for this assignment because image gradients are sparse-ish and TV directly connects to inverse-problem regularization.

## Recent/model-based deep prior methods

- Plug-and-play ADMM replaces an explicit proximal map/regularizer with an image denoiser while keeping the physical forward model.
- Chan, Wang, and Elgendy (2016) discuss fixed-point convergence conditions for plug-and-play ADMM.
- Zhang et al. (2022) propose DPIR, a plug-and-play image restoration approach with a deep denoiser prior and experiments including deblurring.

## Practical choice for our project

Recommended final comparison:

1. Wiener/Tikhonov deconvolution as the standard baseline.
2. TV-regularized deconvolution as the sparse method.
3. DPIR or a smaller plug-and-play ADMM variant as the recent method.

This set covers the assignment requirements while staying feasible for a two-person team.

## Starter references

- W. H. Richardson, "Bayesian-Based Iterative Method of Image Restoration," Journal of the Optical Society of America, 1972. https://ui.adsabs.harvard.edu/abs/1972JOSA...62...55R/abstract
- L. B. Lucy, "An iterative technique for the rectification of observed distributions," The Astronomical Journal, 1974.
- L. Rudin, S. Osher, and E. Fatemi, "Nonlinear total variation based noise removal algorithms," Physica D, 1992. https://web.eecs.utk.edu/~hqi/ece692/references/noise-TV-PhysicaD92.pdf
- S. H. Chan, X. Wang, and O. A. Elgendy, "Plug-and-Play ADMM for Image Restoration: Fixed-Point Convergence and Applications," 2016. https://arxiv.org/abs/1605.01710
- K. Zhang et al., "Plug-and-Play Image Restoration with Deep Denoiser Prior," IEEE TPAMI, 2022. https://doi.org/10.1109/TPAMI.2021.3088914
