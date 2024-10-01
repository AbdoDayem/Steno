// let data = {
//     "event": "",
//     "prefs": {
//         // KEYS WE DEFINE OURSELVES
//         "varX": "x",
//         "varY": "y",
//         "varZ": "z"
//     }
// }

chrome.runtime.onMessage.addListener(data => {
    // we need to define what the data object will look like
    // the data object will be sent from the popup.js file and will be handled by this event listener
    if (data.event = 'transcribe') {
        console.log(data.prefs.url);
    }
});