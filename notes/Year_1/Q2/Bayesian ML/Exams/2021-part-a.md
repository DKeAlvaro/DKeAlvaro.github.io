
### Question 1
Which of the following statements are true?

* **1a** It is more appropriate to say "the likelihood of the parameters", than "the likelihood of the data".
    * a) true
    * b) false
* **1b** If X and Y are independent Gaussian distributed variables, then $Z=3X-XY$ is also a Gaussian distributed variable.
    * a) true
    * b) false
* **1c** For a given Linear Gaussian Dynamical System with observations $\{x_{t}\}$ and latent states $\{z_{t}\}$ the Kalman filter is a recursive solution to the inference problem $p(z_{t}|x_{1:t})$ based on a state estimate at the previous time step $p(z_{t-1}|x_{1:t-1})$ and a new observation $x_{t}.$
    * a) true
    * b) false
* **1d** In the context of parameter estimation, maximum likelihood estimation always selects the parameter values where the Bayesian posterior distribution is maximal.
    * a) true
    * b) false
* **1e** Bayes rule is inconsistent with the Method of Maximum Relative Entropy as a method of inference.
    * a) true
    * b) false

---

### Question 2
Let $x_{n}\in\mathbb{R}^{N}$ and $z_{n}\in\mathbb{R}^{M}$ with $M<<N.$ Given is a model

$$x_{n}=Wz_{n}+\epsilon_{n}$$
$$z_{n}\sim\mathcal{N}(0,I)$$
$$\epsilon_{n}\sim\mathcal{N}(0,\Psi)$$

where $\mathcal{N}(m,V)$ is a Gaussian distribution with mean m and covariance matrix V.

* **2a** Work out an equivalent expression for this model as a joint probability distribution over $x_{n}$ and $z_{n}$.
    * a) $p(x_{n},z_{n})=\frac{\mathcal{N}(x_{n}|Wz_{n},\epsilon_{n})}{\mathcal{N}(z_{n}|0,I)}$
    * b) $p(x_{n},z_{n})=\mathcal{N}(x_{n}|Wz_{n},\Psi)$
    * c) $p(x_{n},z_{n})=\mathcal{N}(x_{n}|Wz_{n},\epsilon_{n})\mathcal{N}(z_{n}|0,I)$
    * d) $p(x_{n},z_{n})=\mathcal{N}(x_{n}|Wz_{n},\Psi)\mathcal{N}(z_{n}|0,I)$
* **2b** Work out an expression for $p(x_{n})$
    * a) $p(x_{n})=\mathcal{N}(x_{n}|0,WW^{T}+\Psi)$
    * b) $p(x_{n})=\mathcal{N}(x_{n}|Wz_{n},WW^{T}+\Psi)$
    * c) $p(x_{n})=\mathcal{N}(x_{n}|0,W^{T}W+\Psi)$
    * d) $p(x_{n})=\mathcal{N}(x_{n}|Wz_{n},\epsilon_{n})$
* **2c** This model is known as a "factor analysis" model and is commonly used to compress observations $x_{n}$ into lower dimensional variables $z_{n}$. Before we can make use of this model, we will need to train the parameters W. Let's start by adding a prior $W\sim\mathcal{N}(0,I)$. Consider an observed data set $X=\{x_{n}|n=1,2,...,N\}$. How would you train the parameters W for this application?
    * a) Compute a posterior $p(W|\{x_{n}\},\{z_{n}\})$. This is easy because the joint is a Gaussian system so we can do this analytically with sum and product rules.
    * b) Compute a posterior $p(W|\{x_{n}\},\{z_{n}\})$. This is hard because $\{z_{n}\}$ is unobserved. Consider variational Bayesian approach.
    * c) Compute a posterior $p(W|\{x_{n}\})$. This is hard because both $\{z_{n}\}$ and W are unobserved. Consider a variational Bayesian approach.
    * d) Compute a posterior $p(W|\{x_{n}\})$ through Bayes rule. This is easy because the joint is a Gaussian system so we can do this analytically with sum and product rules.

---

### Question 3
You have a machine that measures property, the "orangeness" of liquids. You wish to discriminate between $C_{1}=$ 'Fanta' and $C_{2}=$ 'Orangina'. It is known that

$$p(x|C_{1})=\begin{cases}1&1.0\le x\le2.0\\ 0&otherwise\end{cases}$$
$$p(x|C_{2})=\begin{cases}2\cdot(x-1)&1.0\le x\le2.0\\ 0&otherwise\end{cases}$$

The probability that falls outside the interval [1.0, 2.0] is zero. The prior class probabilities $p(C_{1})=0.6$ and $p(C_{2})=0.4$ are also known from experience.

* **3a** We want to develop a Bayesian classifier. The discrimination boundary on the interval $x\in[1.0,2.0]$ is given by
    * a) $1=\frac{p(x|C_{2})}{p(x|C_{1})}\cdot\frac{p(C_{1})}{p(C_{2})}=\frac{1}{2(x-1)}\cdot\frac{0.4}{0.6}\Rightarrow x=5/3$
    * b) $1=\frac{p(x|C_{2})}{p(x|C_{1})}=\frac{1}{2(x-1)}\Rightarrow x=3/2$
    * c) $1=\frac{p(C_{2}|x)}{p(C_{1}|x)}=\frac{1.0.6}{2(x-1)\cdot0.4}\Rightarrow x=7/4$
* **3b** Compute $p(C_{1}|x=1.3)$
    * a) $p(C_{1}|x=1.3)=\frac{p(x=1.3|C_{1})p(C_{1})}{p(x=1.3|C_{2})p(C_{2})}=\frac{1.0.6}{2(1.3-1)\cdot0.4}$
    * b) $p(C_{1}|x=1.3)=p(x=1.3|C_{1})p(C_{1})=1\cdot0.6$
    * c) $p(C_{1}|x=1.3)=\frac{p(x=1.3|C_{1})p(C_{1})}{p(x=1.3)}=\frac{1.0.6}{1.0.6+2(1.3-1)\cdot0.4}$
* **3c** Let the discrimination boundary be given by $x=a$. Work out the total probability of a false classification:
    * a) $\int_{1.0}^{a}p(x|C_{2})p(C_{2})dx+\int_{a}^{2}p(x|C_{1})p(C_{1})dx$
    * b) $\int_{1.0}^{a}p(C_{1}|x)p(x)dx+\int_{a}^{2}p(C_{2}|x)p(x)dx$
    * c) $\int_{1.0}^{a}p(C_{2}|x)dx+\int_{a}^{2}p(C_{1}|x)dx$

