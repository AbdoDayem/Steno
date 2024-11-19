const BACKEND_URL = 'http://0.0.0.0:5001'
let status = 0;

chrome.runtime.onMessage.addListener((data, sender, sendResponse) => {
    if (data.event === 'transcribe') {
        const numberOfTranscriptions = startTranscription(data.prefs)
            .then(data => {
                sendResponse(data);
            })
    } else if (data.event === 'poll') {
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

            return res.json();
        });

    return resp;
};

const pollStatus = async () => {
    const OPTIONS = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }

    let newStatus = status;

    while (newStatus == status) {
        const resp = await fetch(BACKEND_URL + '/status', OPTIONS)
            .then(res => {
                return res.json()
            });

        newStatus = parseInt(resp);
        await delay();
    }

    status = newStatus;

    return status;
};

const delay = () => {
    return new Promise(resolve => setTimeout(resolve, 5000));
};

// Query the backend for text
const getText = async () => {
    const OPTIONS = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }

    const resp = await fetch(BACKEND_URL + '/', OPTIONS)
        .then(res => res.json());

    return resp;
};