# Second Lecture

Q: What is the key distinction between primary and secondary data collection, and which one is typically preferred in engineering systems?
A: Primary data collection involves gathering data directly from the source with control over the collection process, while secondary data collection uses existing data. Engineering systems typically focus on primary data collection because it offers better control over data quality and relevance.

Q: Why is capturing context information considered very relevant in data collection?
A: Context information helps understand the conditions and circumstances under which data was collected, enabling better interpretation, validation, and appropriate use of the data in decision-making and analysis.

Q: Name the four main categories of data mentioned in the lecture and provide a brief description of each.
A: 1) Attribute-value pairs (fields in records, matrix/table representation), 2) Unstructured data (text), 3) Sequence data (time series, event logs), 4) Graph data (non-linear data represented as nodes and vertices).

Q: How does graph data differ from traditional tabular data, and what advantage does it offer?
A: Graph data represents information as nodes, vertices, and attributes on nodes/vertices rather than rows and columns. It captures structural elements better, making it ideal for problems with natural network representations like water distribution systems.

Q: What are the main components of a simplified data acquisition system?
A: The main components include transducers/sensors (to observe the analog world), signal conditioning circuits, ADC (Analog-to-Digital Converter), processing unit, DAC (Digital-to-Analog Converter), and data storage.

Q: What is a transducer and what are its five key properties?
A: A transducer converts a physical quantity into another (usually electrical signal). Key properties are: 1) Sensitivity (response to input changes), 2) Stability (consistent performance over time), 3) Noise (unwanted signal interference), 4) Dynamic range (operating range), 5) Linearity (proportional input-output relationship).

Q: Explain the difference between signal conditioning and data conditioning.
A: Signal conditioning modifies the analog signal before digitization (amplification, filtering, isolation), while data conditioning modifies digitized data for analysis (decomposition, aggregation, smoothing, normalization).

Q: What are the four common filter types used in signal conditioning?
A: Low-pass filter (allows low frequencies), High-pass filter (allows high frequencies), Band-pass filter (allows specific frequency range), Band-stop/Notch filter (blocks specific frequency range).

Q: Why is it important to store raw data rather than only processed or aggregated data?
A: Raw data represents actual measurements and is often atomic/transactional. Storing raw data allows flexibility to derive different features for various analyses later, preserving all original information for future processing needs.

Q: What is the Nyquist rate and why is it important for sampling?
A: The Nyquist rate equals 2 times the signal bandwidth. It's the minimum sampling frequency needed to accurately reconstruct a bandwidth-limited signal without aliasing, ensuring no information loss during digitization.

Q: In system excitation for data collection, what is a pseudo-random binary sequence (PRBS) and why is it useful?
A: PRBS is a signal that contains all frequencies, making it ideal for exciting linear systems during testing. It ensures the system experiences sufficient relevant examples across all frequency ranges for comprehensive characterization.

Q: Name at least four data conditioning techniques and explain what each accomplishes.
A: 1) Decomposition - represents signals as superposition of parts (Fourier transform, wavelets), 2) Aggregation - replaces multiple values with single value (mean, median), 3) Smoothing - reduces noise using filters like moving averages, 4) Interpolation - estimates values between known data points.

Q: What is the exponentially weighted moving average formula and what parameter controls the smoothing?
A: Formula: $y'(t) = a\cdot y(t) + (1-a)\cdot y'(t-1)$, where $0 < a < 1$. Parameter $a$ controls smoothing: smaller $a$ means more smoothing (more weight on history), larger $a$ means less smoothing (more weight on current value).

Q: What is a significant drawback of using moving average filters for smoothing?
A: Moving average filters introduce a phase shift (lag) in the signal, which can be problematic for real-time applications or when timing relationships are important.

Q: Explain the three types of missing data: MCAR, MAR, and MNAR.
A: MCAR (Missing Completely at Random): No systematic differences between missing and non-missing data. MAR (Missing at Random): Differences can be explained by other non-missing features. MNAR (Missing Not at Random): Missing with bias, where the value itself explains why it's missing.

Q: What are the main approaches for handling missing values in datasets?
A: Main approaches include: deletion (removing records with missing values), imputation (filling with estimates like mean, median, or predicted values), and using algorithms that can handle missing data directly.

Q: Describe the CRISP-DM process model and explain why it's considered non-sequential.
A: CRISP-DM (Cross-Industry Standard Process for Data Mining) includes: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. It's non-sequential because it's iterative - you can return to previous phases based on findings, and it's a never-ending circle of improvements.

Q: In CRISP-DM, what guides the Data Preparation phase and when can models be deployed?
A: Data Preparation is guided by the conceptual model developed in earlier phases. Models can only be deployed after receiving positive evaluation, ensuring they meet business requirements and perform adequately.

Q: What are the differences between Essential Tremor and Parkinson's disease tremor in terms of type, frequency, and prevalence?
A: Essential Tremor: postural/kinetic type, $7\text{-}12$ Hz frequency, 95% presence in hands. Parkinson's: resting type, $4\text{-}6$ Hz frequency, >70% presence in hands. Essential Tremor affects 10 million in US vs 1 million for Parkinson's.

Q: Why might computerized tremor analysis be preferred over traditional rating scales like QUEST and ETRS?
A: Computerized analysis provides objective measurements, while rating scales are subjective and biased. Rating scales depend on patient/clinician interpretation, whereas computerized analysis uses sensors for precise, reproducible measurements.

Q: In the TREMOR12 application, what sensors are used and at what sampling rate?
A: TREMOR12 uses accelerometer (measuring acceleration in $\text{g}$) and gyroscope (measuring rotation speed in $\text{rad}/\text{s}$), both sampling at $100$ Hz.

Q: Why were the first and last 50 samples omitted in the TREMOR12 data processing?
A: These samples contained noise from tapping the start and stop buttons, which would interfere with tremor analysis. Removing them ensures only relevant tremor data is analyzed.

Q: What frequency range was used for the FIR filter in TREMOR12 and why?
A: The Equiripple FIR filter used 7-12 Hz range, which corresponds to the typical frequency range of Essential Tremor, helping isolate tremor from voluntary movements and other noise.

Q: What signal features were extracted in the TREMOR12 analysis?
A: Features included: signal strength (root-mean-square), signal period, dominant magnitude (using Welch and Daubechies 8 wavelet methods), and dominant frequency (using same methods).

Q: What is sequential forward feature selection and why is it used?
A: Sequential forward feature selection is an iterative method that starts with no features and adds the most relevant feature at each step. It's used to identify the most informative features while avoiding redundancy and overfitting.

Q: Based on the lecture, why should primary data collection be preferred whenever possible?
A: Primary data collection should be preferred because it provides control over what data is collected, how it's collected, ensures data quality, allows proper experimental design, and enables collection of all necessary context information.

Q: How does a data warehouse differ from operational databases in terms of purpose and structure?
A: Data warehouses are designed for analysis, querying, and reporting with integrated, historical data from multiple sources (ETL process), while operational databases handle day-to-day transactions. Data warehouses support OLAP (analytical processing) vs OLTP (transactional processing).

Q: What role do data marts play in a data warehouse architecture?
A: Data marts are subsets of data warehouses focused on specific business areas or departments. They provide targeted, simplified access to relevant data for specific user groups, improving query performance and usability.

Q: Why is experiment design crucial for both cross-sectional and longitudinal data collection?
A: Experiment design determines which data to collect and how. For cross-sectional data, it involves population sampling and active learning strategies. For longitudinal data, it requires planning system excitation and sampling frequency to capture dynamic behavior properly.

Q: What is the relationship between bandwidth and the Nyquist rate, and why does this matter for data acquisition?
A: Nyquist rate $= 2 \times \text{bandwidth}$. This relationship defines the minimum sampling frequency to avoid aliasing and accurately reconstruct signals. Understanding this prevents information loss and ensures proper digital representation of analog signals.


Overview: Introduction to data collection and processing, covering basic signal analysis and data handling. Features case studies on tremor analysis and data storage systems.

Date: 5 Sep 2025