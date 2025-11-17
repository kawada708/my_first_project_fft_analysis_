# FFT Analysis Tool (made by beginner)

This is my first public Python analysis code as a beginner researcher. 
I'm studying thermal convection, 
and I wrote this script to extract dominant frequencies from time-series data K(t) using FFT. 
I'm not an expert programmer, but I wanted to share my learning process and keep my research scripts organized publicly.

## Notes from a beginner 
- This is not optimized code. 
- There may be cleaner or faster ways to write the same analysis. 
- I will improve this step by step as I learn more. 
- Feedback is always welcome!


## Requirements

```
numpy  
matplotlib  
scipy
```

Install:
```
pip install -r requirements.txt
```

## How to Use

Run the script:
```
python fft_analysis.py
```

You will be asked to input:

1. **Path to your data file (.txt)**
2. **Frequency range to display (fmin fmax)**  
   - Press Enter to use the default: `0.01 400`

Example input file format:
```
0.0001  0.0123
0.0002  0.0131
0.0003  0.0140
```
