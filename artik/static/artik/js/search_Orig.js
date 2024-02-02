
document.getElementById('searchButton').addEventListener('click', function () {
    let searchInput = document.getElementById('searchInput');
    let filterOptionsElement = document.getElementById('filterOptions');

    if (searchInput && filterOptionsElement) {
        let searchText = searchInput.value;
        let filterOptionElements = filterOptionsElement.children;
        let filterOptions = Array.from(filterOptionElements).map(element => element.innerText);
        // Other code...

        // code to perform the search
        // For example
    } else {
        console.error('One of the required elements does not exist.');
    }
});