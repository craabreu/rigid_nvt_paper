TEX = pdflatex -synctex=1 -interaction=nonstopmode
BIB = bibtex
FIGDIR = Figures

.PHONY: all view figures

all : rigid_bodies.pdf view

view :
	evince rigid_bodies.pdf

figures:
	make -C $(FIGDIR)

rigid_bodies.pdf : rigid_bodies.tex figures rigid_bodies.bbl rigid_bodies.blg
	$(TEX) rigid_bodies.tex

rigid_bodies.bbl rigid_bodies.blg : rigid_bodies.bib rigid_bodies.aux
	$(BIB) rigid_bodies

rigid_bodies.aux : rigid_bodies.tex
	$(TEX) rigid_bodies.tex

rigid_bodies.bib : rigid_bodies.tex
	$(TEX) rigid_bodies.tex

