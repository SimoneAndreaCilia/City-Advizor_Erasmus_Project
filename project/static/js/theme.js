document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    // Function to set the theme
    const setTheme = (theme) => {
        if (theme === 'dark') {
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            themeToggleBtn.textContent = '☀️ Light Mode';
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            themeToggleBtn.textContent = '🌙 Dark Mode';
        }
    };

    // Check for saved user preference, if any, on load of the website
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        setTheme(currentTheme);
    } else if (prefersDarkScheme.matches) {
        setTheme('dark');
    } else {
        setTheme('light'); // Default to light if no preference
    }

    // Toggle theme on button click
    themeToggleBtn.addEventListener('click', () => {
        if (document.body.classList.contains('dark-mode')) {
            setTheme('light');
        } else {
            setTheme('dark');
        }
    });
});
