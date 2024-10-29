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
        p.textContent = `Lorem ipsum odor amet, consectetuer adipiscing elit. 
        Elementum tortor pretium sapien sodales turpis potenti morbi in placerat.
        Dictum quisque mi est mi lobortis luctus finibus integer dui. Metus nullam tellus, 
        efficitur fermentum nibh sagittis. Nunc nam et volutpat augue at laoreet luctus. 
        Dignissim facilisis est placerat facilisi sem. In aliquet eget nibh elementum phasellus 
        metus donec fusce.`;
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

const pollForTranscription = async () => {
    await chrome.runtime.sendMessage(
        {
            "event": "poll",
        },
        (response) => {
            // console.log('response from pollForTranscription on popup.js');
            // console.log(response);

            // Trigger the next action - the transcription retrieval function
            getTranscriptions();
        }
    );

    // getTranscriptions();
};

const getTranscriptions = async () => {
    await chrome.runtime.sendMessage(
        {
            "event": "transcriptions",
        },
        (response) => {
            const transcriptionResponse = document.getElementById('transcriptionResponse');
            transcriptionResponse.innerHTML = '';

            // console.log('response from getTranscriptions on popup.js');
            // console.log(typeof response);
            // console.log(response);

            // response should be an object of key-value pairs, where the values are the text i want to display to the user
            Object.keys(response).forEach(key => {
                p = document.createElement('p');
                p.textContent = response[key];

                transcriptionResponse.appendChild(p);
            });
            // response.forEach(transcription => {
            //     p = document.createElement('p');
            //     p.textContent = transcription;

            //     transcriptionResponse.appendChild(p);
            // });
        }
    );
};
