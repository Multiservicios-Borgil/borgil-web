// Selecciones del DOM
const navbar = document.querySelector('.navbar');
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');
const allLinks = document.querySelectorAll('.nav-links a');

// Cambiar el estilo del Navbar al hacer scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Toggle del menú móvil
mobileMenuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    
    // Animación simple del botón hamburguesa
    const spans = mobileMenuBtn.querySelectorAll('span');
    if (navLinks.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
    }
});

// Cerrar menú al hacer click en un enlace (móvil)
allLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            const spans = mobileMenuBtn.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
});

// Animación suave (reveal) al hacer scroll
const animateOnScroll = () => {
    const sections = document.querySelectorAll('section');
    const triggerBottom = window.innerHeight / 5 * 4;

    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;

        if(sectionTop < triggerBottom) {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }
    });
};

// Inicializar estilos de secciones para la animación
document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.6s ease-out';
});

// Escuchar evento de scroll para la animación
window.addEventListener('scroll', animateOnScroll);

// Ejecutar una vez por si el usuario ya está en medio de la página al cargar
animateOnScroll();
