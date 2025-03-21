window.addEventListener('DOMContentLoaded', (event) => {
    getVistitCount();
});

const functionApi = 'https://getresumecounterjatinadamms.azurewebsites.net/api/increment-counter?';

const getVistitCount = () => {
    let count = 0;
    fetch(functionApi).then(response => {
        return response.json();
    }).then(response => {
        console.log('Website called function API.');
        count = response.count;
        document.getElementById('counter').innerText = count;
    }).catch(err => {
        console.error(err);
    });
    return count;
}