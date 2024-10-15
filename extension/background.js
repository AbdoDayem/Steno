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

    const resp = await fetch('http://localhost:8080/api/v1/transcribe', OPTIONS)
        .then(res => res.json())
        .then(data => data);

    // Example number of transcriptions
    // TODOR: replace this with 'resp' and have the request send back a number
    return 111;
}