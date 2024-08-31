---
layout: default
title: Álvaro Menéndez - My Portfolio 
---

# Alvaro Menendez | [My Blog](/blog/)

[Gmail](mailto:alvaro.mrgr@gmail.com) | [LinkedIn](https://www.linkedin.com/in/alvaromenendezros/) | [GitHub](https://github.com/DKeAlvaro)

---

## Summary

I recently gratduated with a `BSc Data Science & AI` from `Maastricht University`. I am currently looking for a `job` in the field. If you are interested in contributing with me, send me an email using the form at the bottom of this page.

I am occasionally writing on [my Blog](/blog/)


---

## Education

### BSc Data Science & AI - Maastricht University
 _Sep 2021_ - _Jun 2024_
- Relevant Coursework: Machine learning, Data analysis, Natural Language Processing, Data structures & algorithms, Recommender Systems

---

## Skills

- Technical Skills: [Java](https://www.java.com/es/), [Python](https://www.python.org/), [SQL](https://en.wikipedia.org/wiki/SQL), [Matlab](https://www.mathworks.com/products/matlab.html)
- I can use most well known python libraries such as [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [SKlearn](https://scikit-learn.org/stable/), [Keras](https://keras.io/), [Matplotlib](https://matplotlib.org/)
- I have hands-on experience with [OpenAI api](https://openai.com/blog/openai-api).

---

## Projects

- ### Fair Feedback Systems for Academic Assessment using LLMs
We performed a project together with Dutch company [Ans](https://ans.app/landing) in which we aimed to help teachers grade exams by assesing how well a student's answer matched the rubric criteria for that question. We tried several state-of-the-art Large Language Models (*LLM's*) for this task such as [BERT](https://huggingface.co/docs/transformers/model_doc/bert), [LLama2](https://huggingface.co/blog/llama2), [Gemini](https://deepmind.google/technologies/gemini/), [GPT-3.5](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates) and evaluated them on *The Stanford Question Answering Dataset* ([SQUAD](https://rajpurkar.github.io/SQuAD-explorer/)). The final product was displayed on a simple GUI that can be seen below:

<div style="text-align: center;">
  <img src="assets/ANS/screenshotOfGUI.jpg" alt="GUI" width="500">
</div>

&nbsp;
We made a (non-published) paper about it and can be downloaded here:
<a href="assets\ANS\Project_3_1.pdf" download="Ans_project.pdf" style="display: inline-block; text-decoration: none; color: white; background-color: #3d3787; padding: 10px 20px; border-radius: 5px; font-size: 12px;">Download </a>

We also had to present our product to an audience! Here are two pictures from the event:
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="assets\ANS\ans_presentation_1.jpg" class="d-block w-100" style="max-width: 600px; height: auto; display: block; margin-left: auto; margin-right: auto;">
    </div>
    <div class="carousel-item">
      <img src="assets\ANS\ans_presentation_2.jpg" class="d-block w-100" style="max-width: 600px; height: auto; display: block; margin-left: auto; margin-right: auto;">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

&nbsp;
- ### Reinforcement Learning applied to Normal Form Games
Reinforcement learning is an AI technique widely used in scenarios where agents must learn to make a sequence of decisions to maximize their rewards through trial and error, such as in games [(AlphaGo)](https://deepmind.google/technologies/alphago/) or autonomous robotics [(Boston Dynamics)](https://bostondynamics.com/blog/starting-on-the-right-foot-with-reinforcement-learning/).

In this project, I learned the basics of Reinforcement Learning, like policies, rewards, or the `Q-learning` algorithm. Most importantly, we implemented and compared basic agents in simple Normal form games in `Java`.


&nbsp;
More detail here: <a href="assets\RL\MARL.pdf" download="MARL.pdf" style="display: inline-block; text-decoration: none; color: white; background-color: #3d3787; padding: 10px 20px; border-radius: 5px; font-size: 12px;">Download </a>



&nbsp;
- ### Genetic algorithms applied to the 0-1 Knapsack problem and Travelling Salesman Problem (TSP)
Imagine you want to travel a specific set of cities in the world, but have limited gas. How would you determine the path that visits all those cities and minimises the total distance traveled so you spend as little gas as possible? This is called the Travelling Salesman Problem, and together with the Knapsack problem, we implemented a solution using Genetic Algorithms. Below you can see how our algorithm slowly finds the (near) optimal solution.

<p align="center">
  <img src="assets\GA\TSP_random.gif" alt="Random Graph" width="48%">
  <img src="assets\GA\TSP.gif" alt="Circle Graph" width="48%">
</p>
We made a (non-published) paper about it and can be downloaded here:
<a href="assets\GA\Genetic_algorithm.pdf" download="GA_project.pdf" style="display: inline-block; text-decoration: none; color: white; background-color: #3d3787; padding: 10px 20px; border-radius: 5px; font-size: 12px;">Download </a>
The colab notebook with all the code can be accessed [here](https://colab.research.google.com/drive/1EfrB5LxqBYcX6lAu41kiUujfb2cawYmm?usp=sharing)

&nbsp;
- ### Sentiment Analysis of inmates Last Statements using Natural language processing (NLP)
We performed a study to analyze the Last Statements from Inmates executed in texas since 1984 using NLP techniques and models such as [BERT](https://huggingface.co/docs/transformers/model_doc/bert) or [N-Gram frequency analysis](https://en.wikipedia.org/wiki/N-gram). The data is publicly available and can be seen [here](https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html). A wordcloud of the last statements can be seen below.

<div style="text-align: center;">
  <img src="assets/NLP/wordcloud.png" alt="wordcloud">
</div>

&nbsp;
We made a (non-published) paper about it and can be downloaded here:
<a href="assets\NLP\NLP_Project-2.pdf" download="NLP_project.pdf" style="display: inline-block; text-decoration: none; color: white; background-color: #3d3787; padding: 10px 20px; border-radius: 5px; font-size: 12px;">Download </a>


&nbsp;
- ### 3D golf project from scratch and developing a bot that made hole in one's!
We developed a 3D mini-golf project using [LibGDX](https://libgdx.com/) for the GUI, then using [Runge-Kutta methods](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) to estimate the position of the ball at every moment. The problem of finding a hole in one can be seen as minimizing a 2D function where the dependent variable is the final distance of the shot given the initial x and y velocities. For this we used hill climbing and gradient descent to find the global minima of this function (see image below for the function to minimize). This turned out to be very useful as it is widely used in Machine Learning.
<p align="center">
  <img src="assets\GOLF\golf_video.gif" alt="GUI demonstration" width="48%">
  <img src="assets\GOLF\Distance_Graph.png" alt="Distance Graph" width="48%">
</p>
The github repository for this project can be accessed [here](https://github.com/DKeAlvaro/Project-1.2)


&nbsp;
## Projects Under developement
- ### [JOINclusion project](https://dke.maastrichtuniversity.nl/JOINclusion/)
I am currrenlty working on a project that aims to foster the social inclusion of ALL children primary school students (with particular attention to those with a migrant background) through the use of a collaborative mobile application group of partners from different background experiences (IT, pedagogy, psychology, artificial intelligence, etc.

The project has a large group of partners from different background experiences (IT, pedagogy, psychology, artificial intelligence, etc.) and countries(Greece, Italy and the Netherlands). [See our team](https://dke.maastrichtuniversity.nl/JOINclusion/partnership/)

&nbsp;
## Languages

- Spanish: Native speaker
- English: Fluent

Finally, a pdf version of my CV can be downloaded here:
<a href="assets\CV\Alvaro_Menendez_CV.pdf" download="cv.pdf" style="display: inline-block; text-decoration: none; color: white; background-color: #3d3787; padding: 10px 20px; border-radius: 5px; font-size: 12px;">Download CV</a>

- ## Send me an E-mail
<div class="form-container">
  <form action="https://formspree.io/f/mdoqewgw" method="POST">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" placeholder="Your name"><br>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="_replyto" placeholder="Your email"><br>
    <label for="message">Message:</label><br>
    <textarea id="message" name="message" placeholder="Your message here"></textarea><br>
    <button type="submit">Send</button>
  </form>
</div>
