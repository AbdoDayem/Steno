// let data = {
//     "event": "",
//     "prefs": {
//         // KEYS WE DEFINE OURSELVES
//         "varX": "x",
//         "varY": "y",
//         "varZ": "z"
//     }
// }

const BACKEND_URL = 'http://127.0.0.1:5000'

chrome.runtime.onMessage.addListener((data, sender, sendResponse) => {
    if (data.event === 'transcribe') {
        const numberOfTranscriptions = startTranscription(data.prefs)
            .then(data => {
                // console.log('data returned from startTranscription');
                // console.log(data);
                sendResponse(data);
            })
    } else if (data.event === 'poll') {
        console.log('polling event triggered on background.js');
        pollStatus()
            .then(data => sendResponse(data));
    } else if (data.event = 'getText') {
        getText()
            .then(data => sendResponse(data));
    }

    return true;
});

const startTranscription = async (data) => {
    const OPTIONS = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }

    const resp = await fetch(BACKEND_URL + '/url', OPTIONS)
        .then(res => {
            if (!res.ok) {
                console.error('Error: Failed to send URL to backend');
            }

            // console.log('res from /url on background.js');
            // console.log(res);

            return res.json();
        });

    return resp;
};

// Poll '/status' on the backend to figure out if the number of texts has changed
    // Define a variable to record how many texts we currently have
    // Set up an long-running poll to query the backend
        // It updates the number. When the number changes, we query for text
    // Once the number we have == the number we are expecting, we end

// FOR FIRST PROTOTYPE:
    // Assume we are expecting 1 text
const pollStatus = async () => {
    const OPTIONS = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }

    let status = 0;

    while (status < 1) {
        const resp = await fetch(BACKEND_URL + '/status', OPTIONS)
            .then(res => {
                // console.log('res in /status fetch on background.js');
                // console.log(res);
                return res.json()
            });
        status = parseInt(resp.status);
    }

    return 'TEMP: done polling'
};

// Query the backend for text
const getText = () => {
    const OPTIONS = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }

    const resp = fetch(BACKEND_URL + '/', OPTIONS)
        .then(res => res.json());

    return resp;
};