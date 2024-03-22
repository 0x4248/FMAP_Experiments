# FMAP Experiments
# A collection of experiments to test the FMAP audio file format.
# GitHub: https://www.github.com/lewisevans2007/FMAP_Experiments
# License: GNU General Public License v3.0
# By: Lewis Evans

PYTHON=python3
PIP=pip3
SRC=src
OUT=out

all: init generate

init:
	pip install -r requirements.txt
	bash setup.sh
	mkdir -p $(OUT)

generate:
	$(PYTHON) $(SRC)/equations.py
	$(PYTHON) $(SRC)/trig.py
	mv *.FMAP $(OUT)/
	$(PYTHON) -m FMAP $(OUT)/cos_cos.FMAP $(OUT)/cos_sin.wav
	$(PYTHON) -m FMAP $(OUT)/sin_tan.FMAP $(OUT)/sin_tan.wav
	$(PYTHON) -m FMAP $(OUT)/sqrt_x.FMAP $(OUT)/sqrt_x.wav
	$(PYTHON) -m FMAP $(OUT)/x_squared.FMAP $(OUT)/x_squared.wav

clean:
	rm -rf $(OUT)
	rm -rf *.FMAP
	rm -rf *.wav
	rm -rf FMAP

.PHONY: all init generate clean