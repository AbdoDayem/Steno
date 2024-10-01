const $helpButton = document.getElementById('helpButton');
$helpButton.onclick = (e) => {
    // const isHidden = document.getElementById('helpText').style.display === 'none';
    e.preventDefault();
    document.getElementById('helpArea').classList.toggle('hidden');
};

// Grab the button element from the html
const $transcribeButton = document.getElementById("transcribe")

// Listen to any clicking that happen to the button and if so, transcribe
$transcribeButton.addEventListener("click", () => {
    if (document.getElementById('transcriptionResponse').children.length === 0) {
        p = document.createElement('p');
        p.textContent = `This will display what the API call returns.`;
        // Add the <p> to the content area in the HTML page
        document.getElementById('transcriptionResponse').appendChild(p);
        
        // Display the transcription response area
        document.getElementById('transcriptionResponse').classList.remove('hidden');
    }
});

$transcribeButton.onclick = () => {
    sendURL();
}

const sendURL = async () => {
    // Use the Chrome API to obtain the active tab
    const url = await getURL();

    // Send the URL to the background script
    chrome.runtime.sendMessage({
        "event": "transcribe",
        "prefs": {
            "url": url
        }
    });
};

// Obtain the user's active tab
// Creates and return a promise so that the URL is resolved prior to sending to the background script
const getURL = async () => {
    return new Promise((resolve, reject) => {
        chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
            resolve(tabs[0].url);
        });
    });
};
