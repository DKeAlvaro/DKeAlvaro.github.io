document.addEventListener('DOMContentLoaded', () => {
    const timeline = document.querySelector('.timeline-line');
    const items = document.querySelectorAll('.timeline-item');
    
    // Initialize timeline height
    timeline.style.scale = '0 1';
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.5
    });
    
    items.forEach(item => observer.observe(item));
    
    // Update timeline progress on scroll
    window.addEventListener('scroll', () => {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        const scrollTop = window.scrollY;
        const progress = Math.min((scrollTop) / (documentHeight - windowHeight), 1);
        
        timeline.style.scale = `1 ${progress}`;
    });
}); 