## My internship at ASML
Two weeks ago I finished my internship in Software/Data engineering at ASML. In this post I will talk about a few things: 
1. The "why" of my internship assignment
2. My solution to the problem, including some technical details
3. My overall experience, and things I learnt.

### The why
> Note: I have [another](https://dkealvaro.github.io/blog/An%20ASML%20intern%E2%80%99s%20thoughts%20after%20two%20months%20in/index.html) blog entry in which I cover my first 2 months of the internship - I explain the why also there. 


I joined a research department with engineers proficient in MATLAB. In my team there was this specific machine (called "BIT") to investigate how to improve ASML's EUV machines. The data from those experiments was important, but with **difficult acces**. The following image summarizes the old process of accessing that data:

Let me walk you through it. The BIT runs experiments daily. Each one generates ≈100gb .mat files  under a shared internal drive. This means, after physically running the experiment on the machine, a new folder with the **raw** .mat files pops up in a given folder address accessible by some employees. The "raw" term carries a lot of weight here: those .mat files are *useles* until they are preprocessed. And preprocessed experiments were stored ONLY in memory and could not be saved to avoid bloating disk space.

In practical terms it meant that when someone wanted to analyze a new BIT experiment, they would have to preprocess it on runtime using their custom Matlab code. 

In retrospect, storing the preprocessed experiments next to the raw data would have made things easier, but I took it as a hard requirement from the beginning.  

 


### What  I did
In one sentence: *I built a Python pipeline (with a small Flask UI) that uses MATLAB to downsample ~100 GB .mat experiments into .parquet files and generate HTML reports for offline visualization.*

### The request

### The architecture and how i got there

### Conclusions

Interestingly, after working on the same problem for a long time, you get to know the big picture in a deeper way: who is involved or gets affected by your results, what parts affect your implementation, and what is the best way to solve it. The "why" is the part you need to spend most time thinking about, not only to know why its useful what you are doing but also to reach a better solution. In tech the first reaction to a new problem is usually to use the hottest or most popular tool. It would have been easier for me to write a sophisticated Fastapi server to then face deployment issues due to strict company regulations. Or to write a fancy React Native app to then realize that the bottleneck is somewhere else, or that my team was not actually looking for that. I always prefer to start with the most non complicated stack, and only if it becomes the bottleneck, swap it by a more powerful stack.
