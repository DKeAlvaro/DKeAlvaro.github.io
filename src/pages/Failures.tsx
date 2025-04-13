import React, { useState, useEffect } from 'react';

interface Failure {
  Company: string;
  Role: string;
  Reason: string;
}

const Failures: React.FC = () => {
  const [failures, setFailures] = useState<Failure[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/src/assets/failures.csv');
        const csvText = await response.text();
        
        const lines = csvText.split('\n').filter(line => line.trim());
        const headers = lines[0].split(',').map(header => header.trim());
        
        const parsedData = lines.slice(1).map(line => {
          let inQuotes = false;
          let currentValue = '';
          let values = [];
          
          for (let char of line) {
            if (char === '"') {
              inQuotes = !inQuotes;
              continue;
            }
            if (char === ',' && !inQuotes) {
              values.push(currentValue.trim());
              currentValue = '';
              continue;
            }
            currentValue += char;
          }
          values.push(currentValue.trim());

          return {
            Company: values[0],
            Role: values[1],
            Reason: values[2]
          };
        });

        setFailures(parsedData);
      } catch (error) {
        console.error('Error loading failures data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="page-container">
      <h1>Unsuccessful applications</h1>
      <div className="intro-container">
        <p>
          Websites like this one tend to show that the person who made them has their 
          life figured out, and that is something I wanted to avoid here.
        </p>
        
        <p>
          At the time of this writing, it has been 4 months since I started searching for a job, 
          with no success, and it is an exasperating process.
        </p>
        
        <p>
          I will leave it there, but I just want to tell you that if you are in a similar situation, 
          I understand what you are going through. Keep fighting.
        </p>
        
        <p>
          Although many of the following are not rejections, below is 
          a (short) list of many of the hiring processes that have not gone as I was 
          hoping for.
        </p>
      </div>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Position</th>
              <th>Reason</th>
            </tr>
          </thead>
          <tbody>
            {failures.map((failure, index) => (
              <tr key={index}>
                <td>
                  <strong>{failure.Company}</strong>
                  {failure.Role && <div className="role">{failure.Role}</div>}
                </td>
                <td>{failure.Reason}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <style>{`
        .intro-container {
          max-width: 800px;
          margin: 2rem auto;
          padding: 0 0.5rem;
          color: var(--secondary-text);
          line-height: 1.6;
        }

        .intro-container p {
          margin-bottom: 1.5rem;
        }

        .table-container {
          max-width: 1000px;
          margin: 0 auto;
          padding: 0 0.5rem;
          height: 500px;
          overflow-y: auto;
        }

        table {
          width: 100%;
          border-collapse: collapse;
        }

        th {
          background: var(--accent-color);
          color: var(--bg-color);
          text-align: left;
          padding: 1rem;
          position: sticky;
          top: 0;
        }

        td {
          padding: 1rem;
          border-bottom: 1px solid var(--nav-border);
        }

        th:first-child, td:first-child {
          width: 40%;
        }

        .role {
          color: var(--secondary-text);
          font-size: 0.9em;
          margin-top: 0.25rem;
        }

        @media (max-width: 767px) {
          .intro-container,
          .table-container {
            padding: 0 0.25rem;
          }
        }
      `}</style>
    </div>
  );
};

export default Failures; 