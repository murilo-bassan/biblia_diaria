document.addEventListener('DOMContentLoaded', function() {
    const themeToggleButton = document.getElementById('themeToggleButton');

    if (themeToggleButton) {
        // LÊ o tema atual que foi aplicado pelo script no HEAD
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        
        // Define o texto e ícone do botão com base no tema atual
        if (currentTheme === 'dark') {
            themeToggleButton.innerHTML = '<i class="fas fa-sun"></i> Modo Claro';
        } else {
            themeToggleButton.innerHTML = '<i class="fas fa-moon"></i> Modo Noturno';
        }

        themeToggleButton.addEventListener('click', function() {
            let theme = document.documentElement.getAttribute('data-theme');
            if (theme === 'dark') {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
                themeToggleButton.innerHTML = '<i class="fas fa-moon"></i> Modo Noturno';
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                themeToggleButton.innerHTML = '<i class="fas fa-sun"></i> Modo Claro';
            }
        });
    }
});