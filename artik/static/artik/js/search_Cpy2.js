
document.getElementById('searchButton').addEventListener('click', function () {
    let searchInput = document.getElementById('searchInput');
    let filterOptionsElement = document.getElementById('filterOptions');
    let resultsElement = document.getElementById('searchResults');

    if (searchInput && filterOptionsElement && resultsElement) {
        let searchText = searchInput.value;
        let filterOptionElements = filterOptionsElement.children;
        let filterOptions = Array.from(filterOptionElements).map(element => element.innerText);

        if(searchText.trim() !== '' && filterOptions.length > 0){
            try{
                let searchResults = performSearch(searchText, filterOptions);
                displaySearchResults(searchResults, resultsElement);
            } catch(e) {
                console.error('Error performing search:', e);
            }
        } else {
            console.error('Search text or filter options are empty. Please check');
        }
    } else {
        console.error('Required HTML elements missing.');
    }
});


function performSearch(searchText, filterOptions) {
     // Implémentez votre logique de recherche ici
    // Retournez les résultats de la recherche
    const data = ["apple", "courage", "orange", "banana"];
    let searchResult = data.filter(item => {
        if(!filterOptions) {
            return item.includes(searchText);
        }
        // Insert more specific search logic based on filterOptions here
    });
    return searchResult;
}


function displaySearchResults(results, resultsElement) {
    // Affichez les résultats dans l'élément resultsElement
    resultsElement.innerHTML = '';  // Clear previous results
    results.forEach(result => {
        let li = document.createElement('li');
        li.innerHTML = result;
        resultsElement.appendChild(li);
    });
}
