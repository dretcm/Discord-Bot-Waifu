@echo off

call conda activate base

python index.py

call conda deactivate

exit