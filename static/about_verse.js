// Este é o JavaScript que fará a requisição assíncrona
        document.getElementById('fetchNewVerseButton').addEventListener('click', function() {
            fetch('/get_new_verse') // Rota que o Flask irá fornecer
                .then(response => response.json())
                .then(data => {
                    document.querySelector('#newVerseDisplay .new-verse-text').textContent = data.text;
                    document.querySelector('#newVerseDisplay .new-verse-reference').textContent = '- ' + data.reference;
                })
                .catch(error => {
                    console.error('Erro ao buscar novo versículo:', error);
                    document.querySelector('#newVerseDisplay .new-verse-text').textContent = 'Erro ao carregar versículo.';
                    document.querySelector('#newVerseDisplay .new-verse-reference').textContent = '';
                });
        });