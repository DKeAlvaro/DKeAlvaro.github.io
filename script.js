// Get DOM elements
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const themeToggle = document.getElementById('themeToggle');
const footerYear = document.getElementById('footerYear');
const firstConfirmButton = document.getElementById('firstConfirmButton');
const secondConfirmButton = document.getElementById('secondConfirmButton');
const firstConfirmation = document.getElementById('firstConfirmation');
const secondConfirmation = document.getElementById('secondConfirmation');
const journeyContent = document.getElementById('journeyContent');
const menuOverlay = document.querySelector('.menu-overlay');

// Set current year in footer
if (footerYear) {
    footerYear.textContent = `Alvaro Menendez - alvaro.mrgr2@gmail.com`;
}

// Mobile menu toggle
if (hamburger && navLinks) {
    let scrollPosition = 0;

    hamburger.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent event from bubbling up
        
        const isMenuOpen = navLinks.classList.contains('active');
        
        if (!isMenuOpen) {
            // Save current scroll position before locking scroll
            scrollPosition = window.pageYOffset;
            document.body.style.top = `-${scrollPosition}px`;
        }
        
        navLinks.classList.toggle('active');
        document.body.classList.toggle('menu-open');
        
        if (isMenuOpen) {
            // Restore scroll position when closing menu
            document.body.style.top = '';
            window.scrollTo(0, scrollPosition);
        }
    });

    // Close mobile menu when clicking on menu links
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            document.body.classList.remove('menu-open');
            
            // Restore scroll position
            document.body.style.top = '';
            window.scrollTo(0, scrollPosition);
        });
    });

    // Close mobile menu when clicking on overlay
    if (menuOverlay) {
        menuOverlay.addEventListener('click', () => {
            navLinks.classList.remove('active');
            document.body.classList.remove('menu-open');
            
            // Restore scroll position
            document.body.style.top = '';
            window.scrollTo(0, scrollPosition);
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                document.body.classList.remove('menu-open');
                
                // Restore scroll position
                document.body.style.top = '';
                window.scrollTo(0, scrollPosition);
            }
        }
    });
}

// Journey confirmation buttons
if (firstConfirmButton && secondConfirmButton && journeyContent) {
    // First confirmation
    firstConfirmButton.addEventListener('click', () => {
        firstConfirmation.style.display = 'none';
        secondConfirmation.style.display = 'block';
        
        // Delay the appearance of the second button
        setTimeout(() => {
            secondConfirmButton.classList.remove('button-delayed');
            secondConfirmButton.style.opacity = '1';
            secondConfirmButton.style.transform = 'translateY(0)';
            secondConfirmButton.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        }, 1500); // 1.5 second delay
    });

    // Second confirmation
    secondConfirmButton.addEventListener('click', () => {
        secondConfirmation.style.display = 'none';
        journeyContent.style.display = 'block';
        
        // Add a subtle fade-in effect to the journey content
        journeyContent.style.opacity = '0';
        journeyContent.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            journeyContent.style.opacity = '1';
            journeyContent.style.transform = 'translateY(0)';
            journeyContent.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        }, 100);
    });
}

// Theme toggle
if (themeToggle) {
    const themeIcon = themeToggle.querySelector('.theme-icon');
    
    // Determine the correct assets path based on current location
    const currentPath = window.location.pathname;
    let assetsPath = 'assets/svg/';
    
    // Count the depth of the current path to calculate correct relative path
    if (currentPath.includes('/notes/') || currentPath.includes('/blog/')) {
        // For notes: /notes/Year_1/Q1/Mentor_meeting/file.html needs ../../../../
        // For blog: /blog/folder/file.html needs ../../
        const pathSegments = currentPath.split('/').filter(part => part !== '');
        
        // Remove the HTML filename if present
        if (pathSegments[pathSegments.length - 1].endsWith('.html')) {
            pathSegments.pop();
        }
        
        // Calculate depth: number of directory levels from root
        const depth = pathSegments.length;
        assetsPath = '../'.repeat(depth) + 'assets/svg/';
    }
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    
    // Apply saved theme or default based on user preference
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.body.classList.add('dark-theme');
        themeIcon.src = assetsPath + 'sun.svg'; // Show sun icon in dark mode
    } else {
        themeIcon.src = assetsPath + 'moon.svg'; // Show moon icon in light mode
    }

    // Theme toggle click handler
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        
        if (document.body.classList.contains('dark-theme')) {
            localStorage.setItem('theme', 'dark');
            themeIcon.src = assetsPath + 'sun.svg'; // Show sun icon in dark mode
        } else {
            localStorage.setItem('theme', 'light');
            themeIcon.src = assetsPath + 'moon.svg'; // Show moon icon in light mode
        }
    });
}
// Example JavaScript for a simple carousel
document.addEventListener('DOMContentLoaded', () => {
  const carouselItems = document.querySelectorAll('.carousel-item');
  let currentIndex = 0;

  function showCarouselItem(index) {
    carouselItems.forEach((item, i) => {
      if (i === index) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }

  // Show the first item initially
  if (carouselItems.length > 0) {
    showCarouselItem(currentIndex);
  }

  // Example: Add navigation buttons (you'd need to add these buttons in your HTML)
  // const nextButton = document.getElementById('next-button');
  // const prevButton = document.getElementById('prev-button');

  // if (nextButton) {
  //   nextButton.addEventListener('click', () => {
  //     currentIndex = (currentIndex + 1) % carouselItems.length;
  //     showCarouselItem(currentIndex);
  //   });
  // }

  // if (prevButton) {
  //   prevButton.addEventListener('click', () => {
  //     currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
  //     showCarouselItem(currentIndex);
  //   });
  // }

  // Example: Auto-play (optional)
  // setInterval(() => {
  //   currentIndex = (currentIndex + 1) % carouselItems.length;
  //   showCarouselItem(currentIndex);
  // }, 5000); // Change image every 5 seconds
});
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded - checking for acknowledgments list');
    const acknowledgmentsList = document.getElementById('acknowledgments-list');
    console.log('Acknowledgments list element:', acknowledgmentsList);

    if (acknowledgmentsList) {
        console.log('Starting to fetch acknowledgments.csv');
        fetch('./acknowledgments.csv')
            .then(response => {
                console.log('Fetch response:', response);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(data => {
                console.log('CSV data received:', data);
                const rows = data.trim().split('\n');
                console.log('Rows after split:', rows);
                const headers = rows.shift().split(';').map(header => header.trim().replace(/"/g, ''));
                console.log('Headers:', headers);
                
                const personIndex = headers.indexOf('person');
                const whyIndex = headers.indexOf('why');
                console.log('Person index:', personIndex, 'Why index:', whyIndex);

                if (personIndex === -1 || whyIndex === -1) {
                    acknowledgmentsList.innerHTML = '<p>Error: CSV file must have "person" and "why" columns.</p>';
                    return;
                }
                
                // Parse all rows into objects
                const acknowledgments = [];
                rows.forEach((row, index) => {
                    console.log(`Processing row ${index}:`, row);
                    const columns = row.split(';').map(col => col.trim().replace(/"/g, ''));
                    const person = columns[personIndex];
                    const why = columns[whyIndex];
                    console.log(`Person: ${person}, Why: ${why}`);

                    if (person && why) {
                        acknowledgments.push({ person, why });
                    }
                });
                
                // Keep first 2 entries fixed, randomize the rest
                const fixedEntries = acknowledgments.slice(0, 2);
                const randomEntries = acknowledgments.slice(2);
                
                // Shuffle the remaining entries using Fisher-Yates algorithm
                for (let i = randomEntries.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [randomEntries[i], randomEntries[j]] = [randomEntries[j], randomEntries[i]];
                }
                
                // Combine fixed and randomized entries
                const finalOrder = [...fixedEntries, ...randomEntries];
                
                // Create and append DOM elements
                finalOrder.forEach((acknowledgment) => {
                    const acknowledgmentItem = document.createElement('div');
                    acknowledgmentItem.classList.add('acknowledgment-item');

                    const personElement = document.createElement('h3');
                    personElement.textContent = acknowledgment.person;

                    const whyElement = document.createElement('p');
                    whyElement.textContent = acknowledgment.why;

                    acknowledgmentItem.appendChild(personElement);
                    acknowledgmentItem.appendChild(whyElement);

                    acknowledgmentsList.appendChild(acknowledgmentItem);
                    console.log('Added acknowledgment item for:', acknowledgment.person);
                });
                console.log('Finished processing all acknowledgments');
            })
            .catch(error => {
                console.error('Error fetching acknowledgments:', error);
                acknowledgmentsList.innerHTML = '<p>Could not load acknowledgments. Error: ' + error.message + '</p>';
            });
    } else {
        console.log('Acknowledgments list element not found!');
    }
});
document.addEventListener('DOMContentLoaded', () => {
    const folderElements = document.querySelectorAll('.tree-folder');

    folderElements.forEach(folder => {
        // // Initially collapse all folders
        // const nestedUl = folder.querySelector('ul');
        // if (nestedUl) {
        //     folder.classList.add('collapsed');
        //     nestedUl.classList.add('collapsed');
        // }

        folder.addEventListener('click', (e) => {
            // Prevent toggling if a link inside the folder is clicked
            if (e.target.tagName === 'A') {
                return;
            }

            // Stop the event from bubbling up to parent folders
            e.stopPropagation();

            const nestedUl = folder.querySelector('ul');
            if (nestedUl) {
                folder.classList.toggle('collapsed');
                nestedUl.classList.toggle('collapsed');
            }
        });
    });
});

// Q&A Toggle Function
function toggleQA(qaId) {
    const answer = document.getElementById(qaId);
    const question = answer.previousElementSibling;
    
    if (answer.classList.contains('active')) {
        answer.classList.remove('active');
        question.classList.remove('active');
    } else {
        answer.classList.add('active');
        question.classList.add('active');
    }
}