FIGS = energy_drift energy_partition Free_Energy NVE thermodynamic_properties numerical_stability

.PHONY: all

all : $(addsuffix .eps, $(FIGS))

%.eps: %.py
	python $^
