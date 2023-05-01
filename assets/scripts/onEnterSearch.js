'use strict';


// Event listener to pressing ENTER key in input field
const onEnterSearchPress = (n_clicks, value) => {
    document.addEventListener(
        'keydown', () => {
            if (event.key === 'Enter') {
                document.getElementById('pkmn-search-btn').click();
                // document.getElementById('pkmn-search-input').textContent = '';
            }
        });
    return '';
};


