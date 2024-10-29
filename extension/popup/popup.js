/**
 * 
 * Function to start transcribing by calling the backend API
 */
async function StartTranscription() {
    
}

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
    // if (document.getElementById('transcriptionResponse').children.length === 0) {
        // p = document.createElement('p');
        // // This is a placeholder API
        // fetch("https://catfact.ninja/fact")
        // .then(response => response.json())
        // .then(data => {
        //     p.textContent = data["fact"]
        // })
        // // Add the <p> to the content area in the HTML page
        // document.getElementById('transcriptionResponse').appendChild(p);
        
        // Display the transcription response area
        document.getElementById('transcriptionResponse').classList.remove('hidden');
    //}
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

// Display the number of remaining files to be transcribed using the backend endpoint /status
const remainingFiles = document.getElementById("files")
fetch("http://localhost:5000/status")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        remainingFiles.innerText = "Remaining Files = " + data
    })

// Obtain the user's active tab
// Creates and return a promise so that the URL is resolved prior to sending to the background script
const getURL = async () => {
    return new Promise((resolve, reject) => {
        chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
            resolve(tabs[0].url);
        });
    });
};
