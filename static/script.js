document.addEventListener('DOMContentLoaded', function() {
    console.log('Application chargée');
    
    document.getElementById('predictionForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const movieSelect = document.getElementById('movieSelect');
        const selectedOption = movieSelect.options[movieSelect.selectedIndex];
        
        if (!movieSelect.value) {
            alert('Veuillez sélectionner un film');
            return;
        }
        
        const movieId = parseInt(movieSelect.value);
        const movieName = selectedOption.getAttribute('data-name');
        
        // Les autres valeurs seront générées automatiquement côté serveur
        const data = {
            movie_id: movieId,
            movie_name: movieName
        };
    
        try {
            // Afficher un indicateur de chargement
            document.getElementById('predictionValue').textContent = 'Chargement...';
            document.getElementById('result').classList.remove('hidden');
            
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
    
            const result = await response.json();
            
            if (result.user_id !== undefined) {
                // Formater les valeurs pour l'affichage (limiter à 6 décimales)
                const formatValue = (value) => {
                    return typeof value === 'number' ? value.toFixed(6) : value;
                };
                
                // Afficher la prédiction
                document.getElementById('predictionValue').textContent = 
                    `Prédiction réussie pour ${movieName}`;
                
                // Afficher les détails
                document.getElementById('detailMovieId').textContent = movieId;
                document.getElementById('detailMovieName').textContent = movieName;
                document.getElementById('detailUserId').textContent = formatValue(result.user_id);
                document.getElementById('detailMovieId2').textContent = formatValue(result.movie_id);
                document.getElementById('detailRating').textContent = formatValue(result.rating);
                document.getElementById('detailTimestamp').textContent = formatValue(result.timestamp);
            } else {
                document.getElementById('predictionValue').textContent = 'Erreur lors de la prédiction';
                alert('Erreur lors de la prédiction');
            }
        } catch (error) {
            console.error('Erreur:', error);
            document.getElementById('predictionValue').textContent = 'Erreur lors de la requête';
            alert('Erreur lors de la requête');
        }
    });
});