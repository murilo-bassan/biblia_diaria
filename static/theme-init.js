(function() {
          const currentTheme = localStorage.getItem('theme');
          let themeToApply = 'light'; // Padrão
          
          if (currentTheme) {
              themeToApply = currentTheme;
          } 
          
          else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
              themeToApply = 'dark'; // Usa a preferência do sistema se não houver no localStorage
          }

          document.documentElement.setAttribute('data-theme', themeToApply);

          // Tenta encontrar o botão da navbar imediatamente e define seu texto/ícone
          // Isso é importante para evitar o "flash" do texto incorreto
          const themeToggleButton = document.getElementById('themeToggleButton');
          if (themeToggleButton) {
              if (themeToApply === 'dark') {
                  themeToggleButton.innerHTML = '<i class="fas fa-sun"></i> Modo Claro';
              } 
              else {
                  themeToggleButton.innerHTML = '<i class="fas fa-moon"></i> Modo Noturno';
              }
          }
      })();
