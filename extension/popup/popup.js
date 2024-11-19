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
    // Poll for transcriptions if the button is clicked
    pollForTranscription()
    // Show the spinner
    document.getElementById('spinner').classList.remove('hidden');
    
});

$transcribeButton.onclick = () => {
    sendURL();
}

const sendURL = async () => {
    // Use the Chrome API to obtain the active tab
    const url = await getURL();

    // Send the URL to the background script
    await chrome.runtime.sendMessage(
        // The JSON we send to the background script
        {
            "event": "transcribe",
            "prefs": {
                "url": url
            }
        },
        // The callback function
        (response) => {
            if (chrome.runtime.lastError) {
                console.error(JSON.stringify(chrome.runtime.lastError));
            }

            // Display a message to the user that the transcription is beginning
            if (response) {
                p = document.createElement('p');
                p.textContent = 'Transcribing audio on: ' + response;

                const launchStatus = document.getElementById('launchStatus');

                // Clear the previous content
                launchStatus.innerHTML = '';

                // Add the <p> to the content area in the HTML page
                launchStatus.appendChild(p);
                
                // Display the transcription response area
                launchStatus.classList.remove('hidden');
                
                // Trigger the next action - the polling function
                pollForTranscription();
            }
        }
    );
};

// Display the number of remaining files to be transcribed using the backend endpoint /status
// const remainingFiles = document.getElementById("files")
// fetch("http://0.0.0.0:5001/status")
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//         remainingFiles.innerText = "Remaining Files = " + data
//     })

// Obtain the user's active tab
// Creates and return a promise so that the URL is resolved prior to sending to the background script
const getURL = async () => {
    return new Promise((resolve, reject) => {
        chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
            resolve(tabs[0].url);
        });
    });
};

const pollForTranscription = async () => {
    await chrome.runtime.sendMessage(
        {
            "event": "poll",
        },
        (response) => {
            const transcriptionResponse = document.getElementById('transcriptionResponse');
            transcriptionResponse.innerHTML = '';

            // Trigger the next action - the transcription retrieval function
            getTranscriptions();
        }
    );
};

const getTranscriptions = async () => {
    await chrome.runtime.sendMessage(
        {
            "event": "transcriptions",
        },
        (response) => {
            // Hide the spinner
            document.getElementById('spinner').classList.add('hidden');

            // response should be an object of key-value pairs, where the values are the text i want to display to the user
            Object.keys(response).forEach(key => {
                p = document.createElement('p');
                p.textContent = response[key];

                transcriptionResponse.appendChild(p);
            });

            transcriptionResponse.classList.remove('hidden');
        }
    );
};
