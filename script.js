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
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    
    // Apply saved theme or default based on user preference
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.body.classList.add('dark-theme');
        themeToggle.textContent = 'Light Mode';
    } else {
        themeToggle.textContent = 'Dark Mode';
    }

    // Theme toggle click handler
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        
        if (document.body.classList.contains('dark-theme')) {
            localStorage.setItem('theme', 'dark');
            themeToggle.textContent = 'Light Mode';
        } else {
            localStorage.setItem('theme', 'light');
            themeToggle.textContent = 'Dark Mode';
        }
    });
} 