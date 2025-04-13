import React from 'react';

const About: React.FC = () => {
  return (
    <div className="page-container">
      <h1>About Me</h1>
      <div className="content">
        <p>
          Welcome to my personal website. I am a <strong>Young Data Scientist</strong> who wants to make a <em>positive impact</em> on society.
        </p>
        
        <p>
          At 17, I moved from Spain to the Netherlands to successfully complete my Bachelor's in <a href="https://curriculum.maastrichtuniversity.nl/education/bachelor/data-science-and-artificial-intelligence" target="_blank" rel="noopener noreferrer">Data Science and Artificial intelligence</a> (#1 AI programme in The Netherlands).
        </p>
        
        <p>
          Since then, I have demonstrated my ability to deliver software solutions, ranging from applying AI in education (Collaborated with the <a href="https://dke.maastrichtuniversity.nl/JOINclusion/" target="_blank" rel="noopener noreferrer">JOINclusion team</a> to perform a clustering analysis on the results of the JOINclusion game) to developing a full stack web application for the IOT device management company <a href="https://www.sqippa.com/" target="_blank" rel="noopener noreferrer">Sqippa</a>.
        </p>
        
        <p>
          Currently, I would like to focus my career path into applying <strong>Data Science principles</strong> to solve <em>business problems</em>.
        </p>
        
        <p>
          If you are a company who has lots of data to work with, or you are looking to expand your Data Science team, do not hesitate to contact me
        </p>
        <div className="skills">
          <h2>Skills</h2>
          <ul>
            <li>Python</li>
            <li>Machine Learning (pytorch, scikit learn)</li>
            <li>Data science (numpy, pandas, matplotlib)</li>
            <li>Flask, Django</li>
            <li>LLMs</li>
            <li>SQL</li>
            <li>Git</li>
            <li>HTML, CSS, JavaScript</li>
            <li>Vibe Coding (Cursor, Trae)</li>
            <li>LaTeX</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default About;