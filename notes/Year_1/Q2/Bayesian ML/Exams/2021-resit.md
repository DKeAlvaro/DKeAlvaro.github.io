## Question 1: Probabilities of drawing objects from a box
Box 1 contains 4 apples and 8 oranges. Box 2 contains 10 apples and 2 oranges. Boxes are chosen with equal probability. You make one draw.

**1a** What is the probability of choosing an apple?
a) *(Option a not shown)*
b) $\frac{6}{12}$
c) *(Option c not shown)*
d) *(Option d not shown)*

**1b** If an apple is chosen, what is the probability that it came from box 1?
a) *(Option a not shown)*
b) *(Option b not shown)*
c) $\frac{1}{3}$
d) *(Option d not shown)*

Instead of one draw, we now take two draws without replacement. Again, we can draw from either box at each draw, and boxes are chosen with equal probabilities.

**1c** If you know that your second draw will be an orange from box 2, what is now the probability of drawing an apple at the first draw?
a) $7/12$
b) $41/66$
c) $7/11$
d) The correct answer is not shown.

---

## Question 2: Model comparison
A model $m_1$ is described by a single parameter $\theta$, with $0 \le \theta \le 1$. The system can produce data $x \in \{0,1\}$. 
The sampling distribution $p(x|\theta,m_1)$ and prior $p(\theta|m_1)$ are given by:
$p(\theta|m_1) = 6\theta(1-\theta)$
$p(x|\theta,m_1) = \theta^x(1-\theta)^{1-x}$

**2a** Determine the evidence $p(x=1|m_1)$
a) $2/3$
b) $1/6$
c) $1/3$
d) $1/2$

**2b** Determine the posterior probability $p(\theta|x=1,m_1)$
a) $6\frac{\theta^2}{1-\theta}$
b) $12\theta^2(1-\theta)$
c) $6\theta^2(1-\theta)$
d) $12\frac{\theta^2}{1-\theta}$

Consider a second model $m_2$ with the following sampling distribution and prior on $0 \le \theta \le 1$:
$p(\theta|m_2) = 1$
$p(x|\theta,m_2) = (1-\theta)^x\theta^{1-x}$

The model priors are given by $p(m_1) = 2/3$ and $p(m_2) = 1/3$.

**2c** Determine the ratio of posterior model probabilities $\frac{p(m_1|x=1)}{p(m_2|x=1)}$.
a) $1/3$
b) $1/2$
c) $2/3$
d) $2$

---

## Question 3: Recursive Bayesian Filtering
We observe a process $x_t = \theta + \epsilon_t$ with $\epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$.
We are interested in recursively updating estimates for $\theta$ from observations $x_1, x_2, \dots$. The estimate for $\theta$ after $k$ observations $D_k = \{x_1, x_2, \dots, x_k\}$ is written as:
$p(\theta|D_k) = \mathcal{N}(\theta|\mu_k, \sigma_k^2)$.
The prior for $\theta$ (after zero observations) is given by $p(\theta) = p(\theta|D_0) = \mathcal{N}(\theta|\mu_0, \sigma_0^2)$.

**3a** Which is a correct expression for the likelihood $p(x_k|\theta)$?
a) $p(x_k|\theta) = \mathcal{N}(x_k|\mu_k, \sigma_\epsilon^2 + \sigma_\theta^2)$
b) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\epsilon^2)$
c) $p(x_k|\theta) = \mathcal{N}(x_k|0, \sigma_\epsilon^2 + \sigma_\theta^2)$
d) $p(x_k|\theta) = \mathcal{N}(x_k|\theta, \sigma_\theta^2)$

**3b** Next, you are asked to work out the recursive update formula for posterior $p(\theta|D_k) = \mathcal{N}(\theta|\mu_k, \sigma_k^2)$. Basically this is a derivation of a very simple Kalman filter.
In this derivation you may want to use the formula for Gaussian multiplication:
$\mathcal{N}(x|\mu_a, \sigma_a^2)\mathcal{N}(x|\mu_b, \sigma_b^2) \propto \mathcal{N}(x|\mu_c, \sigma_c^2)$ with $\frac{1}{\sigma_c^2} = \frac{1}{\sigma_a^2} + \frac{1}{\sigma_b^2}$ and $\frac{1}{\sigma_c^2}\mu_c = \frac{1}{\sigma_a^2}\mu_a + \frac{1}{\sigma_b^2}\mu_b$.

I will start the derivation here:
$p(\theta|D_k) = p(\theta|x_k, D_{k-1})$
$\propto p(\theta, x_k|D_{k-1})$
$= p(x_k|\theta)p(\theta|D_{k-1})$
$= \dots$

Now you complete this and derive expressions for $\mu_k$ and $\sigma_k^2$:

a)
$\begin{cases} K_k &= \frac{\sigma_\epsilon^2}{\sigma_{k-1}^2+\sigma_\epsilon^2} \\ \mu_k &= \mu_{k-1} + K_k\cdot(x_k-\mu_{k-1}) \\ \sigma_k^2 &= (1-K_k)\cdot\sigma_{k-1}^2 + \sigma_\epsilon^2 \end{cases}$

b)
$\begin{cases} K_k &= \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2} \\ \mu_k &= \mu_{k-1} + K_k\cdot(x_k-\mu_{k-1}) \\ \sigma_k^2 &= \sigma_{k-1}^2 + K_k\cdot(\sigma_\epsilon^2-\sigma_{k-1}^2) \end{cases}$

c)
$\begin{cases} K_k &= \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2} \\ \mu_k &= \frac{1}{2}\mu_{k-1} + \frac{1}{2}K_k\cdot(x_k-\mu_{k-1}) \\ \sigma_k^2 &= (1-K_k)\cdot\sigma_{k-1}^2 + \sigma_\epsilon^2 \end{cases}$

d)
$\begin{cases} K_k &= \frac{\sigma_{k-1}^2}{\sigma_{k-1}^2+\sigma_\epsilon^2} \\ \mu_k &= \mu_{k-1} + K_k\cdot(x_k-\mu_{k-1}) \\ \sigma_k^2 &= (1-K_k)\cdot\sigma_{k-1}^2 \end{cases}$

**3c** What happens for $k \rightarrow \infty$ (# observations goes to infinity).
a) $\sigma_k^2 \rightarrow \sigma_{k-1}^2$
b) $\mu_k \approx \mu_{k-1}$ (stationarity)
c) $\sigma_k^2 \rightarrow \sigma_\epsilon^2$
d) $K_k \rightarrow 1$

---

## Question 4: Comprehension

**4a** Which of the following statements is most consistent with Friston's Free Energy Principle?
a) Actions aim to minimize the free energy of future states of the world.
b) Actions aim to minimize the complexity of future states of the world.
c) Intelligent decision making requires minimization of a functional of beliefs about future states of the world.
d) Intelligent decision making requires minimization of a cost function of future states of the world.

**4b** Which of the following statements is most accurate about Bayesian vs Maximum Likelihood-based estimation?
a) The ML estimate tends to become a better approximation to the Bayesian estimate as the data size grows, since the prior distribution in Bayesian estimation tends to become wider with more data.
b) The ML estimate tends to become a worse approximation to the Bayesian estimate as the data size grows, since both the likelihood function and prior distribution tend to become wider with more data.
c) The ML estimate tends to become a better approximation to the Bayesian estimate as the data size grows, since the likelihood function tends to become wider with more data while the prior distribution in Bayesian estimation does not depend on the data set size.
d) The ML estimate tends to become a better approximation to the Bayesian estimate as the data size grows, since the likelihood function tends to become narrower with more data while the prior distribution in Bayesian estimation does not depend on the data set size.

**4c** A Bayesian sticks a microphone in the air and records a signal $x = (x_1, x_2, \dots, x_T)$. She is interested in retrieving a speech signal $s = (s_1, s_2, \dots, s_T)$ from the recording. How might she proceed?
a) She describes the recorded signal by a model $p(x,s,z) = p(s|x,z)p(x,z)$ where $z$ is a set of latent states and model parameters. Then, she will proceed to infer her beliefs about $s$ by computing $p(s|x) \propto \int p(s|x,z)dz$.
b) She describes the recorded signal by a model $p(x,s,z) = p(s|x,z)p(x,z)$ where $z$ is a set of latent states and model parameters. Then, she will proceed to infer her beliefs about $s$ by computing $p(s|x) \propto \int p(s|x,z)p(x,z)dz$.
c) She describes the recorded signal by a joint model $p(x,s,z) = p(x|s,z)p(s,z)$ where $z$ is a set of latent states and model parameters. Then, she will proceed to infer her beliefs about $s$ by computing $p(s|x,z) = \frac{p(x|s,z)p(s,z)}{p(x,z)}$.
d) She describes the recorded signal by a joint model $p(x,s,z) = p(x|s,z)p(s,z)$ where $z$ is a set of latent states and model parameters. Then, she will proceed to infer her beliefs about $s$ by computing $p(s|x) \propto \int p(x|s,z)p(s,z)dz$.

**4d** Consider a data set $\{x_n|n=1,2,\dots,N\}$ with $x_n \in \mathbb{R}^M$ and a set of latent one-hot coded variables $z_n = (z_{n1}, z_{n2}, \dots, z_{nK})$ i.e., $z_{nk} \in \{0,1\}$ and $\Sigma_{k=1}^K z_{nk} = 1$. Which of the following is a correct specification for a Gaussian Mixture Model?
a) $p(x_n, z_n) = \prod_{k=1}^K(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k))^{z_n}$
b) $p(x_n, z_n) = \prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)^{z_{nk}}$
c) $p(x_n, z_n) = \prod_{k=1}^K \pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k)$
d) $p(x_n, z_n) = \prod_{k=1}^K(\pi_k \cdot \mathcal{N}(x_n|\mu_k, \Sigma_k))^{z_{nk}}$

**4e** Consider a generative model $p(x,z)$ where $x$ has been observed and $z$ are latent states. We introduce a posterior distribution $q(z)$ for the latent states and define a Free Energy functional $F[q] = \int q(z)\log\frac{q(z)}{p(x,z)}dz$. Which of the following statements is true?
a) $F[q] = -\log p(x)$ if $q(z) = 0$
b) $F[q] \le -\log p(x)$ for any choice of $q(z)$.
c) $F[q] \ge -\log p(x)$ for any choice of $q(z)$.
d) $F[q] = -\log p(x)$ if $q(z) = p(z)$.

---

## Question 5: Classifier Orange-ness
You have a machine that measures property $x$, the "orangeness" of liquids. You wish to discriminate between $C_1 = \text{'Fanta'}$ and $C_2 = \text{'Orangina'}$. It is known that:
$p(x|C_1) = \begin{cases} 6x(1-x) & 0 \le x \le 1 \\ 0 & \text{otherwise} \end{cases}$
$p(x|C_2) = \begin{cases} 2x & 0 \le x \le 1 \\ 0 & \text{otherwise} \end{cases}$

The probability that $x$ falls outside the interval $[0.0, 1.0]$ is zero. The prior class probabilities $p(C_1) = 0.6$ and $p(C_2) = 0.4$ are also known from experience.

**5a** We want to develop a Bayesian classifier. The discrimination boundary on the interval $x \in [0.0, 1.0]$ is given by:
a) $1 = \frac{p(x|C_1)}{p(x|C_2)} = \frac{6x(1-x)}{2x} \Rightarrow x = 2/3$
b) $\frac{1}{2} = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 8/9$
c) $1 = \frac{p(C_1|x)}{p(C_2|x)} = \frac{p(x|C_1)p(C_1)}{p(x|C_2)p(C_2)} = \frac{6x(1-x)\cdot 0.6}{2x\cdot 0.4} \Rightarrow x = 7/9$

**5b** Compute $p(C_1|x=0.5)$.
a) $p(C_1|x=0.5) = \frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5|C_2)p(C_2)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{1\cdot\frac{4}{10}}$
b) $p(C_1|x=0.5) = \frac{p(x=0.5|C_1)p(C_1)}{p(x=0.5)} = \frac{\frac{6}{4}\cdot\frac{6}{10}}{\frac{6}{4}\cdot\frac{6}{10}+1\cdot\frac{4}{10}}$
c) $p(C_1|x=0.5) = p(x=0.5|C_1)p(C_1) = \frac{6}{4}\cdot\frac{6}{10}$

**5c** Now assume that the prior probabilities $p(C_1)$ and $p(C_2)$ are not known and you have a data set of correctly labeled samples $D=\{(x_1,y_1), (x_2,y_2), \dots, (x_N,y_N)\}$. How would a Bayesian approach proceed to classify a new sample $x_\bullet$?
a) Assume parameterized prior class probabilities, e.g., $p(C_1|\theta)=\theta$ and $p(C_2|\theta)=1-\theta$, with a Gaussian prior on $\theta$. Then absorb the data in the model by Bayes rule to get $p(\theta|D)$ and classify $x_\bullet$ by $p(C_1|x_\bullet,D) \propto \int p(x_\bullet|C_1,\theta)p(\theta|D)d\theta$.
b) Assume $p(C_1)=p(C_2)=0.5$ and use Bayes rule to compute $p(C_1|x_\bullet)$.
c) Assume parameterized prior class probabilities, e.g., $p(C_1|\theta)=\theta$ and $p(C_2|\theta)=1-\theta$, with a Beta prior on $\theta$. Then absorb the data in the model by Bayes rule to get $p(\theta|D)$ and $p(C_1|x_\bullet,D) \propto \int p(x_\bullet|C_1)p(C_1|\theta)p(\theta|D)d\theta$.
