# monthly-sales

#https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/monthly-sales-reporting/README.md
cd /Users/Rishi/Documents/GitHub/monthly-sales

conda create -n sales-env python=3.7 # (first time only)
conda activate sales-env
pip install pandas # (only if you're using pandas to parse the CSV files)
python reporter.py