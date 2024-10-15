// let data = {
//     "event": "",
//     "prefs": {
//         // KEYS WE DEFINE OURSELVES
//         "varX": "x",
//         "varY": "y",
//         "varZ": "z"
//     }
// }

chrome.runtime.onMessage.addListener((data, sender, sendResponse) => {
    if (data.event = 'transcribe') {
        const numberOfTranscriptions = startTranscription(data.prefs)
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

    const resp = await fetch('http://127.0.0.1:5000/url', OPTIONS)
        .then(res => res);
}