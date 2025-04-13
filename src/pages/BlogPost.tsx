import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

const BlogPost: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [content, setContent] = useState<string>('');

  useEffect(() => {
    const loadBlogContent = async () => {
      try {
        const response = await fetch(`/src/content/blogs/${id}/index.html`);
        if (!response.ok) {
          throw new Error('Blog post not found');
        }
        const html = await response.text();
        
        // Extract the content from the main or article tag
        const mainContent = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i)?.[1] ||
                          html.match(/<article[^>]*>([\s\S]*?)<\/article>/i)?.[1];
        
        if (mainContent) {
          setContent(mainContent);
        } else {
          // Fallback to body content if main/article not found
          const bodyContent = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1] || html;
          setContent(bodyContent);
        }
      } catch (error) {
        console.error('Error loading blog post:', error);
        setContent('<h1>Blog post not found</h1>');
      }
    };

    if (id) {
      loadBlogContent();
    }
  }, [id]);

  return (
    <div className="page-container blog-post-container">
      <Link to="/blog" className="back-link">← Back to Blog</Link>
      <article className="blog-content">
        <div 
          id="blog-content-container"
          dangerouslySetInnerHTML={{ __html: content }}
        />
      </article>
      <style>{`
        .blog-post-container {
          max-width: 800px;
          margin: 0rem auto;
          padding: 0 1rem;
        }

        .back-link {
          display: inline-block;
          margin-bottom: 0rem;
          color: var(--accent-color);
          text-decoration: none;
        }

        .back-link:hover {
          text-decoration: underline;
        }

        .blog-content {
          font-size: 1.1rem;
          line-height: 1.6;
        }

        .blog-content h1 {
          font-size: 2.5rem;
          margin-bottom: 0rem;
        }

        .blog-content h2 {
          font-size: 1.8rem;
          margin: 2rem 0 1rem;
        }

        .blog-content p {
          margin: 1rem 0;
        }

        .blog-content img {
          max-width: 100%;
          height: auto;
          border-radius: 8px;
          margin: 2rem 0;
        }

        .blog-content pre {
          background: var(--tag-bg);
          padding: 1rem;
          border-radius: 8px;
          overflow-x: auto;
        }

        .blog-content code {
          font-family: 'Fira Mono', monospace;
          background: var(--tag-bg);
          padding: 0.2rem 0.4rem;
          border-radius: 4px;
        }

        /* Additional styles for blog content */
        .blog-content a {
          color: var(--accent-color);
          text-decoration: none;
        }

        .blog-content a:hover {
          text-decoration: underline;
        }

        .blog-content ul, .blog-content ol {
          margin: 1rem 0;
          padding-left: 2rem;
        }

        .blog-content li {
          margin: 0.5rem 0;
        }

        .blog-content blockquote {
          margin: 1.5rem 0;
          padding-left: 1rem;
          border-left: 4px solid var(--accent-color);
          color: var(--secondary-text);
        }

        .blog-content hr {
          margin: 2rem 0;
          border: none;
          border-top: 1px solid var(--nav-border);
        }

        /* Additional styles for video containers */
        .video-container {
          position: relative;
          padding-bottom: 56.25%; /* 16:9 aspect ratio */
          height: 0;
          overflow: hidden;
          margin: 2rem 0;
        }

        .video-container video {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }

        /* Fix for inline styles */
        [style*="display: flex"] {
          display: flex !important;
        }

        [style*="justify-content: center"] {
          justify-content: center !important;
        }
      `}</style>
    </div>
  );
};

export default BlogPost; 