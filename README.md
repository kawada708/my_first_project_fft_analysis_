# FFT Analysis Tool (made by begginer)

This is my first public Python analysis code as a beginner researcher. 
I'm studying thermal convection, 
and I wrote this script to find dominant frequencies from time-series data (such as K(t)) using FFT. 
I'm not an expert programmer, but I wanted to share this code so that lab members and future students can learn from it and use it as a reference.
## Notes from a beginner
- This code includes Japanese.
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
pip install numpy matplotlib scipy

```

## How to Use
You will be asked to input:

1. **Path to your data file (.txt)**
2. **Frequency range to display (fmin fmax)**  
   - Enter the frequency range (fmin fmax).　
   - If the plot does not look correct, change the range and run again.

Example input file format:
```
0.0001  0.0123
0.0002  0.0131
0.0003  0.0140
```
