import React, { useEffect, useState } from 'react';

interface Repository {
  id: number;
  name: string;
  description: string;
  html_url: string;
  language: string;
  stargazers_count: number;
  topics: string[];
  created_at: string;
}

const StarIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="16"
    height="16"
    viewBox="0 0 24 24"
    fill="currentColor"
    className="star-icon"
  >
    <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/>
  </svg>
);

const Projects: React.FC = () => {
  const [repositories, setRepositories] = useState<Repository[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRepositories = async () => {
      try {
        const response = await fetch('https://api.github.com/users/DKeAlvaro/repos');
        if (!response.ok) {
          throw new Error('Failed to fetch repositories');
        }
        const data = await response.json();
        // Sort repositories by creation date (most recent first)
        const sortedData = data.sort((a: Repository, b: Repository) => 
          new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
        );
        setRepositories(sortedData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setIsLoading(false);
      }
    };

    fetchRepositories();
  }, []);

  if (isLoading) {
    return (
      <div className="page-container">
        <div className="loading">Loading repositories...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-container">
        <div className="error">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="page-container">
      <div className="projects-grid">
        {repositories.map(repo => (
          <a 
            key={repo.id} 
            href={repo.html_url}
            target="_blank"
            rel="noopener noreferrer"
            className="project-card"
          >
            <h2>{repo.name}</h2>
            <p>{repo.description || 'No description available'}</p>
            <div className="project-meta">
              {repo.language && (
                <span className="tech-tag">{repo.language}</span>
              )}
              {repo.stargazers_count > 0 && (
                <span className="stars">
                  <StarIcon />
                  {repo.stargazers_count}
                </span>
              )}
            </div>
            {repo.topics && repo.topics.length > 0 && (
              <div className="topics">
                {repo.topics.map((topic, index) => (
                  <span key={index} className="topic-tag">{topic}</span>
                ))}
              </div>
            )}
          </a>
        ))}
      </div>
    </div>
  );
};

export default Projects;