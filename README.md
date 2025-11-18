# ***FFT Analysis Tool (made by beginner)***

This is my first public Python analysis code as a beginner researcher.

I'm studying thermal convection, and I wrote this script to find dominant frequencies

from time-series data (such as K(t)) using FFT.

I'm not an expert programmer, but I wanted to share this code so that

**lab members and future students can learn from it and use it as a reference.**


## **📘 Notes**

- This code includes Japanese comments.
- This is not optimized code.
- There may be cleaner or faster ways to write the same analysis.
- I will improve this step by step as I learn more.
- ***Feedback is always welcome!***


## **🔧Recommended Usage**

### You are **recommended to run this script in Jupyter Lab / Jupyter Notebook** 
because it allows easy visualization and interactive analysis.

> (You can also run it from the command line using `python fft_analysis.py`.)

**Requirements**
> 
> - numpy
> - matplotlib
> - scipy
> 
> Install (if needed):
> 
> ```bash
> pip install numpy matplotlib scipy
> ```
> 


## 📝How to Use

When you run the script, you will be asked to input:

1. **Path to your data file (.txt)**

2. **Frequency range to display (fmin fmax)**

Example:

```bash
0 400
```

If the plot does not look correct, change the range and run again.


### **Example input file format**

The input file should contain two columns:

```bash
0.0001  0.0123
0.0002  0.0131
0.0003  0.0140
```

- 1st column: time
- 2nd column: signal value (e.g., K(t))


## 📊Example Output

Here is an example of the FFT result plotted using this script

(using one of the sample data files):

![周波数.png](322c06c0-fd05-453e-a702-f54baee270d1.png)

![解析結果図.png](%E8%A7%A3%E6%9E%90%E7%B5%90%E6%9E%9C%E5%9B%B3.png)

The figure shows:

- The input time-series signal
- The power spectrum after removing the DC component
- The dominant frequency peak(s)

## 📂Sample Data

This repository also includes several sample data files stored in the `sample_data` folder.

These files contain example time-series data (periodic and non-periodic cases)

so you can practice using the script without preparing your own data.

Feel free to try analyzing these files first.
