document.addEventListener('DOMContentLoaded', () => {
    alert('DOM content loaded');

    const form = document.getElementById('form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        // alert('Form submitted');
        try {
            const response = await fetch('http://localhost:3000', {
                method: 'GET', // or 'POST', 'PUT', etc.
                headers: {
                    'Content-Type': 'application/json'
                },
                // mode: 'no-cors'
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // const data = await response.json();
            // console.log('Response from localhost:', data);
            // alert(response.body);
            console.log(response);
        } catch (error) {
            console.error('Error making request:', error);
        }
    });
});

const createAlert = () => {
    alert('Alert created');
};
