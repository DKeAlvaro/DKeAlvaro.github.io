# The Opacity Problem in ML - Lecture 7

Q: What are the three main questions the lecture on "The Opacity Problem in ML" addresses?
A: 1. Why is opacity a problem? 2. What does the opacity problem look like in AI? 3. How to achieve transparency? (Page 2)

Q: What does "XAI" stand for?
A: eXplainable Artificial Intelligence (Page 4).

Q: Why is there an increasing interest in XAI?
A: AI is omnipresent, it is used in high-stakes contexts (like health care), and people have "automation bias" (Page 4, Page 5, Page 6).

Q: What is "automation bias"?
A: People tend to over-rely on automated systems, even when they know it's faulty (Page 6).

Q: What is "opacity" in the context of AI?
A: Humans often don't understand the model's decision logic (Page 7).

Q: What was the Dutch benefits fraud scandal used as an example of opacity?
A: The Dutch tax authorities falsely accused thousands of families of fraud, based on an opaque "risk assessment" tool (Page 8).

Q: What was the issue with Amazon's AI recruiting tool?
A: It taught itself that male candidates were preferable, penalizing resumes with words like "women's" or from all-women's colleges (Page 10).

Q: Why is opacity a problem (i.e., why is interpretability needed)?
A: For Model Validation, Knowledge Discovery, User Acceptance, Justification, Assessing Fairness, and Assessing Trustworthiness (Page 11).

Q: What is the central consequence of opacity?
A: If we don't know how a system works, we cannot trust, challenge, improve, or intervene on its outputs and we have no control / oversight (Page 12).

Q: What are some of the harms opacity can cause in high-stakes contexts?
A: Injustices, lack of recourse/contestability/accountability, and unsafety (Page 12).

Q: In the ML lifecycle diagram, what component is typically considered the "black box"?
A: The "Model" (Page 17).

Q: What is the "technical explainability problem"?
A: The challenge of using XAI methods to understand the "black box" model (Page 18).

Q: What is a saliency map or "heatmap" in XAI?
A: A visualization showing which parts of an input (like an image) are most important for the model's decision-making process (Page 19).

Q: What is a "feature importance ranking"?
A: A method that identifies and ranks the significance of individual input variables in influencing a model's predictions (Page 20).

Q: What is a "counterfactual explanation" in ML?
A: It describes the smallest change to the feature values that changes the prediction to a predefined output (Page 21).

Q: What is an example of a counterfactual explanation for a rejected loan application?
A: "If the applicant's income was €45.000, the loan would be approved." (Page 22).

Q: What are "interpretable models" as a type of XAI?
A: Models where you can directly interpret the model's decision logic (Page 23).

Q: What are "post-hoc explanations" as a type of XAI?
A: Methods that estimate the decision logic of an existing model (Page 23).

Q: What is the difference between "global" and "local" explanations?
A: Global explanations cover the model's overall logic, while local explanations cover a single prediction (Page 23).

Q: What is the difference between "model-specific" and "model-agnostic" explanations?
A: Model-specific methods leverage characteristics of a specific model class, while model-agnostic methods can work on any model (Page 23).

Q: What does Cynthia Rudin argue regarding high-stakes decisions?
A: Stop explaining black box models and use interpretable models instead (Page 23).

Q: Is the opacity problem limited to just the "black box" algorithm?
A: No, the lecture states it is much larger and is a sociotechnical problem that occurs in the entire AI ecosystem (Page 25, Page 43).

Q: What are the different stakeholders in the "real-world context of application" for an ML model?
A: Creators, Data subjects, Operators, Executors, Decision subjects / users, and Auditors (Page 28).

Q: In the credit scoring example, who is the "Operator"?
A: The front-office bank teller who enters the data (Page 29, Page 30).

Q: In the credit scoring example, who is the "Executor"?
A: The back-office analyst who uses the score to make a decision (Page 29, Page 30).

Q: In the generative AI (e.g., DALLE) example, who are the "data subjects"?
A: Artists, photographers, and designers whose images and designs are in the datasets (Page 31).

Q: According to Burrell (2016), what are the three sources of opacity?
A: Technical illiteracy, Intentional secrecy, and System complexity (Page 32).

Q: What is opacity from "technical illiteracy"?
A: A system is opaque because the stakeholder does not have enough technical skills to understand it (Page 33).

Q: What is opacity from "intentional secrecy"?
A: A system is opaque because a third party (like a developer) deliberately holds back information (Page 34).

Q: What is opacity from "system complexity"?
A: A system is opaque to all stakeholders simply because of its characteristics (size, complexity) (Page 35).

Q: How can data collection methods be opaque due to "intentional secrecy"?
A: Through the "non-disclosure of data collection methods" (Page 36).

Q: What did the lawyer who used ChatGPT for a court filing discover?
A: That ChatGPT had invented everything (the cases were false), and it even falsely claimed the cases were real when asked to verify (Page 40, Page 41).

Q: What is the "algorithmic divide"?
A: Inequalities in AI knowledge and understanding that exacerbate existing social inequalities (Page 42).

Q: Are XAI methods a "silver bullet" for opacity?
A: No, the lecture states they are not (yet?) a silver bullet (Page 45).

Q: What is the "fidelity" problem with post-hoc XAI methods?
A: They might not perfectly represent the model's true decision process, leading to misleading explanations (Page 46).

Q: What is the "robustness" problem with XAI methods?
A: Many XAI methods are unreliable and prone to adversarial attacks (Page 46).

Q: What is the "interpretability gap" with heatmaps?
A: The "hottest" parts of the map contain both useful and non-useful information, so it doesn't reveal *exactly* what the model used (Page 47).

Q: What is the "feasibility" problem with counterfactual explanations?
A: Not all counterfactuals are actionable or realistic (e.g., suggesting a person change their age to get a loan) (Page 48).

Q: What right does Recital 71 of the GDPR provide regarding automated decisions?
A: The right to obtain an explanation of the decision and to challenge the decision (Page 49).

Q: What right does the AI Act (Art. 86) provide to an affected person?
A: The right to obtain "clear and meaningful explanations of the role of the AI system in the decision-making procedure" (Page 49).

Q: Is transparency a goal in itself?
A: No, it is a means to an end; it's necessary to achieve other goals we value, like justice, safety, and accountability (Page 51).

Q: What three solutions are needed to increase transparency?
A: More robust XAI, strong regulation, and public education (Page 52).


Overview: Seventh lecture
Date: 21 Sep 2025