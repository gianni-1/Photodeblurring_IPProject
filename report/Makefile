PDF=photo_deblurring_report.pdf

all: $(PDF)

$(PDF): main.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=photo_deblurring_report main.tex

clean:
	latexmk -C -jobname=photo_deblurring_report main.tex
	rm -f *.bbl *.blg *.run.xml *.bcf
