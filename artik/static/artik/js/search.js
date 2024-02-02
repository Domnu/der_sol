document.getElementById('searchButton').addEventListener('click', function () {
    let searchInput = document.getElementById('searchInput');
    let filterOptionsElement = document.getElementById('filterOptions');
    let resultsElement = document.getElementById('searchResults'); // Là où vous afficherez les résultats de la recherche

    if (searchInput && filterOptionsElement && resultsElement) {
        let searchText = searchInput.value;
        let filterOptionElements = filterOptionsElement.children;
        let filterOptions = Array.from(filterOptionElements).map(element => element.innerText);

        // Code pour effectuer la recherche ici
        let searchResults = performSearch(searchText, filterOptions);

        // Affichez les résultats de la recherche dans la page
        displaySearchResults(searchResults, resultsElement);
    } else {
        console.error('Lun des elements requis n\'existe pas.');

    }
});

function performSearch(searchText, filterOptions) {
    // Implémentez votre logique de recherche ici
    // Retournez les résultats de la recherche
}

function displaySearchResults(results, resultsElement) {
    // Affichez les résultats dans l'élément resultsElement
}
