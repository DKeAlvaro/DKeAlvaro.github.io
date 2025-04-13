import React from 'react';
import { Link } from 'react-router-dom';

interface BlogPost {
  id: string;
  title: string;
  date: string;
  summary: string;
  path: string;
}

const Blog: React.FC = () => {
  const blogPosts: BlogPost[] = [
    {
      id: 'hack2progress',
      title: 'My first live Hackathon (hack2progress.com)',
      date: 'March 3, 2025',
      summary: 'I will dive into the details of my first live Hackathon',
      path: '/blog/hack2progress'
    },
    {
      id: 'goals',
      title: 'My short and long term goals',
      date: 'February 26, 2025',
      summary: 'A personal post where I open up about me. Please don\'t judge!',
      path: '/blog/goals'
    },
    {
      id: 'ai-agents',
      title: 'AI agents are not quite there yet (but they are close)',
      date: 'February 24, 2025',
      summary: 'I used the new best AI web agent to apply for a LinkedIn job and it didn\'t perform as expected... Spoiler, it couldn\'t complete the task',
      path: '/blog/ai-agents'
    },
    {
      id: 'message-to-employer',
      title: 'A note to my future employer',
      date: 'February 21, 2025',
      summary: 'What I would like my future employer to know about me',
      path: '/blog/message-to-employer'
    },
    {
      id: 'gpt-intro',
      title: 'Humble introduction to GPT models and PyTorch',
      date: 'February 6, 2025',
      summary: 'The beginner-friendly introduction to GPT models and PyTorch I would have liked to have.',
      path: '/blog/gpt-intro'
    }
  ];

  return (
    <div className="page-container">
      <div className="blog-posts">
        {blogPosts.map(post => (
          <div key={post.id} className="blog-post">
            <h2>
              <Link to={post.path}>{post.title}</Link>
            </h2>
            <div className="post-date">{post.date}</div>
            <p>{post.summary}</p>
          </div>
        ))}
      </div>
      <style>{`
        .blog-posts {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .blog-post {
          margin-bottom: 1rem;
        }

        .blog-post h2 {
          margin: 0;
          font-size: 1.5rem;
        }

        .blog-post h2 a {
          color: var(--text-color);
          text-decoration: none;
        }

        .blog-post h2 a:hover {
          color: var(--accent-color);
        }

        .post-date {
          color: var(--secondary-text);
          font-size: 0.9rem;
          margin: 0.5rem 0;
        }

        .blog-post p {
          margin: 0.5rem 0 0;
          color: var(--secondary-text);
        }
      `}</style>
    </div>
  );
};

export default Blog;