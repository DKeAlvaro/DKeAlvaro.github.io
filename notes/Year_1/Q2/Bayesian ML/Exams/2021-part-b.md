### Question 1

**1a** The Free Energy Principle (FEP) is a theory about biological self-organization, in particular about how brains develop through interactions with their environment. Which of the following statements is most consistent with FEP:
* **a.** Our actions aim to reduce the complexity of our model of the environment.
* **b.** Learning maximizes variational free energy
* **c.** Perception aims to reduce the complexity of our model of the environment.
* **d.** We act to fullfil our predictions about future sensory inputs.

**1b** Given is a data set $D=\{(x_{n},y_{n})\}_{n=1}^{N}$ where $x_{n}$ holds a set of features and $y_{n}$ is the class label for the n-th item. The discriminative approach to classification is based on a model proposal $p(y_{n}|x_{n},\theta)$ with prior $p(\theta)$. After training this model on data D, the Bayesian class prediction $y_{\bullet}$ for a new input $x_{\bullet}$ is based on:
* **a.** $p(y_{\bullet}|x_{\bullet},D)=\int p(y_{\bullet}|x_{\bullet},\theta,D)dt$
* **b.** $p(y_{\bullet}|x_{\bullet})=\int p(y_{\bullet}|x_{\bullet},\theta)p(\theta)d\theta$
* **c.** $p(y_{\bullet}|x_{\bullet},D)=\int p(y_{\bullet}|x_{\bullet},\theta)p(\theta|D)d\theta$
* **d.** $p(y_{\bullet}|x_{\bullet})=\int p(y_{\bullet}|x_{\bullet},\theta)d\theta$

**1c** In the Bayesian approach to model comparison, we rate the performance of model $m_{k}$ for a given data set $D=\{x_{n}\}_{n=1}^{N}$ by its posterior probability $p(m_{k}|D)$, which can be evaluated by the following formula:
* **a.** $p(m_{k}|D)=p(m_{k})\int p(\theta|D,m_{k})p(D|m_{k})d\theta$
* **b.** $p(m_{k}|D)=p(m_{k})\int p(D|\theta,m_{k})p(\theta|m_{k})d\theta$
* **c.** $p(m_{k}|D)=\Sigma_{n}p(m_{k})p(D|m_{k})$
* **d.** $p(m_{k}|D)=\int p(D|\theta,m_{k})p(\theta|m_{k})d\theta$

**1d** A dark bag contains five red balls and seven green ones. Balls are not returned to the bag after each draw. If you know that on the third draw the ball was a green one, what is now the probability of drawing a red ball on the first draw?
* **a.** $4/12$
* **b.** $5/11$
* **c.** $5/12$
* **d.** $4/11$

**1e** Which of the following expressions is a correct generative Gaussian Mixture Model for observations $x_{n}$ and hidden one-hot coded cluster selection variables $z_{n}$?
* **a.** $p(x_{n},z_{n})=\prod_{k=1}^{K}(\pi_{k}\cdot\mathcal{N}(x_{n}|\mu_{k},\Sigma_{k}))^{z_{n}}$
* **b.** $p(x_{n},z_{n})=\prod_{k=1}^{K}\pi_{k}\cdot\mathcal{N}(x_{n}|\mu_{k},\Sigma_{k})^{z_{nk}}$
* **c.** $p(x_{n},z_{n})=\Sigma_{k=1}^{K}\pi_{k}\cdot\mathcal{N}(x_{n}|\mu_{k},\Sigma_{k})$
* **d.** $p(x_{n},z_{n})=\prod_{k=1}^{K}(\pi_{k}\cdot\mathcal{N}(x_{n}|\mu_{k},\Sigma_{k}))^{z_{nk}}$

---

### Question 2

A model $m_{1}$ is described by a single parameter, with $0\le\theta\le1$. The system can produce data $x\in\{0,1,...\}$. The sampling distribution $p(x|\theta,m_{1})$ and prior $p(\theta|m_{1})$ are given by:

$$p(x|\theta,m_{1})=(1-\theta)\theta^{x}$$
$$p(\theta|m_{1})=6\theta(1-\theta)$$

**2a** Determine the posterior $p(\theta|x=4,m_{1})$
* **a.** $6\theta^{4}(1-\theta)^{2}$
* **b.** $\frac{\int_{0}^{1}\theta^{5}(1-\theta)^{2}d\theta}{\theta^{5}(1-\theta)^{2}}$
* **c.** $\frac{\theta^{5}(1-\theta)^{2}}{\int_{0}^{1}\theta^{5}(1-\theta)^{2}d\theta}$

**2b** Determine the probability $p(x=4|m_{1})$.
* **a.** $\int_{0}^{1}\frac{(1-\theta)\theta^{4}}{6\theta(1-\theta)}d\theta$
* **b.** $\int_{0}^{1}(1-\theta)\theta^{4}d\theta$
* **c.** $\int_{0}^{1}6\theta^{5}(1-\theta)^{2}d\theta$
* **d.** $\int_{0}^{1}\frac{6\theta(1-\theta)}{(1-\theta)\theta^{4}}d\theta$

Consider a second model $m_{2}$ with the following sampling distribution and prior on $0\le\theta\le1$:

$$p(x|\theta,m_{2})=(1-\theta)\theta^{x}$$
$$p(\theta|m_{2})=2\theta$$

The model priors are given by $p(m_{1})=2/3$ and $p(m_{2})=1/3$.

**2c** Determine the probability $p(x=4|m_{2})$.
* **a.** $\int_{0}^{1}2(1-\theta)\theta^{5}d\theta$
* **b.** $\frac{1}{\int_{0}^{1}2(1-\theta)\theta^{5}}d\theta$
* **c/d.** $\int_{0}^{1}\frac{(1-\theta)\theta^{4}}{2\theta}d\theta$

**2d** Which of the two models has the largest Bayesian evidence after observing $x=4?$
* **a.** $m_{1}$
* **b.** $m_{2}$
* **c.** same evidence for both models

**2e** Which of the two models has the largest posterior probability after observing $x=4?$
* **a.** $m_{1}$
* **b.** $m_{2}$
* **c.** both models have the same posterior probability.

