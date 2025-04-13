import React, { useState } from 'react';

const Journey: React.FC = () => {
  const [showContent, setShowContent] = useState(false);
  const [firstConfirmation, setFirstConfirmation] = useState(false);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const [isFinalTransition, setIsFinalTransition] = useState(false);

  const handleFirstConfirm = () => {
    setIsTransitioning(true);
    setTimeout(() => {
      setFirstConfirmation(true);
      setTimeout(() => {
        setIsTransitioning(false);
      }, 300);
    }, 500);
  };

  const handleFinalReveal = () => {
    setIsFinalTransition(true);
    setTimeout(() => {
      setShowContent(true);
    }, 1000);
  };

  const timelineEvents = [
    {
      year: "2025 - now",
      title: "Hackathons and Personal Projects",
      description: "While actively looking for a meaningful job where I can grow professionally, I am participating in various hackathons and working on personal projects to improve my skills and show my abilities.",
      images: [
        {
          src: "/src/assets/images/hack2progress.jpg",
          alt: "Hack2Progress Hackathon",
          caption: "Hack2Progress: Applying AI agents to improve urban movility with my team 'Los Cachosos'. Saw the Hackhaton online and organized a weekend trip to participate with my friends. We didn't win but had a great time so it was worth it."
        },
        {
          src: "/src/assets/images/hackathon-axa.jpg",
          alt: "AXA Hackathon",
          caption: "AXA Hackathon: Developed a RAG chatbot to answer insurance specific questions with my team 'Axalyticos'. I was contacted and invited by Santiago Ampudia via Linkedin and I am super thankful about it! I met amazing people there"
        }
      ]
    },
    {
      year: "2024",
      title: "End of BSc & Multiple Jobs",
      description: "Completed my Bachelor's degree while working 4 jobs: that was intense and didn't last long, but I really enjoyed and learned from it. This was the end of an era in my life in which I grew a lot as a person.",
      images: [
        {
          src: "/src/assets/images/holanda-final-tesis.jpg",
          alt: "Final thesis in Holland",
          caption: "During my Bachelor's defense. My thesis work was about clustering explainability in educational games data. To be honest, I think I could have done a better job, but I am satisfied with it."
        },
        {
          src: "/src/assets/images/cocinero.jpg",
          alt: "Working as a cook",
          caption: "Working as a cook assistant to support my studies. Somehow made my way through to work as a kitchen assistant in the second best restaurant in the city, even though I had no real previous experience. It was an enriching experience for me to work in such a different enviroment"
        },
        {
          src: "/src/assets/images/repartidor-flink.jpg",
          alt: "Working as a delivery person",
          caption: "Delivering with Flink between classes. This is the job I spent more time during my degree, I really liked it. I would do 3 to 8h shifts and wouldn't get tired. Partly because Maastricht is a cozy city and its very bike friendly. I used to listen to many books and podcasts while biking, such as 'Atomic Habits' and 'The picture of Dorian Gray'"
        },
        {
          src: "/src/assets/images/teacher.jpg",
          alt: "Working as a teacher",
          caption: "Selfie before starting my Scratch class! An afterschool academy were looking for teachers so I got in contact with Rishat, the man behind all of it. There is a lot to learn about him, but I would highlight his attitude of believing 'everything is possible'. He created the academy and got it up and running with many schools in less than 7 months. Really inspiring. I would also highlight that during my time there, I noticed I really enjoy teaching and it is definitely a thing I will do in the future"
        },
        {
          src: "/src/assets/images/mattress.jpg",
          alt: "Living minimally",
          caption: "I lived in a mattress for 3 weeks. I had to organize everything about my flat in the Netherlands while being in Spain. It ended up working out smoothly but I arrived to an empty flat, so I lived in a mattress I borrowed from Joana for a while, lol"
        },
        {
          src: "/src/assets/images/naples-thesis.jpg",
          alt: "Presenting thesis in Naples",
          caption: "Presenting my research in Naples. Im very thankful to Enrique, my supervisor, for giving me this opportunity. He invited me to Naples to present my results to the JOINclusion team and met I my teachers from a different point of view. Just imagine having a teacher for three years, then going on a trip with them! It was surprising"
        }
      ]
    },
    {
      year: "2021 - 2023",
      title: "University Life & Adventures",
      description: "Having the best university life with the best people.",
      images: [
        {
          src: "/src/assets/images/malta_trip.jpeg",
          alt: "Trip to Malta",
          caption: "Week trip to Malta with my class friends: Boris, Asha, Ratix Alex, Rubén and Eden. We all had fun."
        },
        {
          src: "/src/assets/images/granada.jpg",
          alt: "Visit to Granada",
          caption: "Visiting Granada with my friends from Madrid: Pejes, Frodo and Mikelo"
        },
        {
          src: "/src/assets/images/italy-federica-alessio.jpg",
          alt: "Italy with friends",
          caption: "Ohh, Alessio and Federica! They treated Joana and I so well inviting us to Italy. They were super nice hosts"
        }
      ]
    },
    {
      year: "Before 2021",
      title: "Teenage years",
      description: "Before university, I though all forms of life were related to the neighborhood I was born.",
      images: [
        {
          src: "/src/assets/images/arbitro-2.jpg",
          alt: "Referee experience",
          caption: "Working as a Handball referee. When I was just 15 y/o I worked for a few months as a referee, and I should have stayed longer. Being a referee is completely different than being a player. When you play, you just follow rules, but when you are a referee, you are the one who decides how the game goes. And that teaches you a lot about life"
        },
        {
          src: "/src/assets/images/holanda-llegar.jpg",
          alt: "Arriving in Holland",
          caption: "First steps in The Netherlands. This actually belongs to 2021, but I feel this belongs to my teenage years. I was just 17 y/o when I arrived to study there!"
        },
        {
          src: "/src/assets/images/bici_luis_santiago.jpg",
          alt: "Camino de Santiago by bike",
          caption: "Cycling the Camino de Santiago with Luis. This was a 7 day bike trip from Madrid to Santiago that really marked me"
        }
      ]
    }
  ];

  if (!showContent) {
    return (
      <div className={`journey-container reveal-question ${isFinalTransition ? 'fade-out-scale' : ''}`}>
        <div className={`question-container ${isTransitioning ? 'fade-out' : ''}`}>
          <h2 className="question-text">
            {!firstConfirmation ? 'Do you really want to know about my life?' : 'Are you sure?'}
          </h2>
          {!firstConfirmation && (
            <button onClick={handleFirstConfirm} className="reveal-button">Yes</button>
          )}
        </div>
        {firstConfirmation && !isTransitioning && (
          <button onClick={handleFinalReveal} className="reveal-button fade-in">Yes, I'm sure</button>
        )}
        <style>{`
          .reveal-question {
            transition: all 1s ease;
            transform-origin: center;
          }
          .reveal-question.fade-out-scale {
            opacity: 0;
            transform: scale(0.95);
          }
          .question-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: opacity 0.5s ease;
            opacity: 1;
          }
          .question-container.fade-out {
            opacity: 0;
          }
          .reveal-button {
            margin-top: 1rem;
            transition: opacity 1s ease;
          }
          .reveal-button.fade-in {
            animation: fadeIn 0.5s ease 1s forwards;
            opacity: 0;
          }
          @keyframes fadeIn {
            from {
              opacity: 0;
            }
            to {
              opacity: 1;
            }
          }
          .fade-out-scale .reveal-button {
            opacity: 0;
          }
        `}</style>
      </div>
    );
  }

  return (
    <div className="journey-container fade-in">
      <div className="timeline">
        {timelineEvents.map((event, index) => (
          <div key={index} className="timeline-item">
            <div className="timeline-content">
              <div className="timeline-year">{event.year}</div>
              <h3>{event.title}</h3>
              <p>{event.description}</p>
              <div className="timeline-images">
                {event.images.map((image, imgIndex) => (
                  <figure key={imgIndex} className="image-container">
                    <img 
                      src={image.src} 
                      alt={image.alt} 
                      className="timeline-image"
                    />
                    <figcaption>{image.caption}</figcaption>
                  </figure>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
      <style>{`
        .fade-in {
          animation: fadeIn 1s ease;
        }
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .timeline {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 1rem;
        }

        .timeline-item {
          margin-bottom: 4rem;
          position: relative;
        }

        .timeline-item:first-child {
          margin-top: 1rem;
        }

        .timeline-content {
          padding: 1rem 0;
        }

        .timeline-content:first-child {
          padding-top: 0;
        }

        .timeline-year {
          font-size: 2rem;
          font-weight: bold;
          color: var(--accent-color);
          margin-bottom: 0.5rem;
        }

        .timeline-images {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          gap: 2rem;
          margin-top: 2rem;
        }

        .image-container {
          margin: 0;
          display: flex;
          flex-direction: column;
          align-items: center;
        }

        .timeline-image {
          width: 100%;
          height: auto;
          border-radius: 8px;
        }

        .image-container figcaption {
          margin-top: 0.5rem;
          text-align: center;
          color: var(--secondary-text);
          font-size: 0.9rem;
          padding: 0.5rem;
        }

        h3 {
          font-size: 1.5rem;
          margin: 1rem 0;
          color: var(--text-color);
        }

        p {
          color: var(--secondary-text);
          line-height: 1.6;
        }

        @media (min-width: 768px) {
          .timeline-item:nth-child(even) .timeline-content {
            margin-left: auto;
          }

          .timeline-content {
            width: 90%;
          }
        }

        @media (max-width: 767px) {
          .timeline-content {
            margin: 0;
            padding: 1rem 0;
          }

          .timeline-year {
            font-size: 1.5rem;
          }

          .timeline-images {
            grid-template-columns: 1fr;
            gap: 1.5rem;
          }

          h3 {
            font-size: 1.2rem;
          }

          .image-container figcaption {
            font-size: 0.85rem;
          }
        }
      `}</style>
    </div>
  );
};

export default Journey;