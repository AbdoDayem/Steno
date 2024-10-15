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
        mode: 'no-cors',
        body: JSON.stringify(data)
    }

    const resp = await fetch('http://localhost:5000/url', OPTIONS)
        // .then(res => res.json())
        // .then(data => data);
        .then(res => res);

    console.log(resp);

    // Example number of transcriptions
    // TODOR: replace this with 'resp' and have the request send back a number
    return 111;
}