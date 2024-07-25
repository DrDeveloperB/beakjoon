document.addEventListener('DOMContentLoaded', () => {
    const cameraButton = document.querySelector('.camera');
    const cameraOverlay = document.getElementById('cameraOverlay');
    const closeCameraButton = document.getElementById('closeCameraButton');
    const captureButton = document.getElementById('captureButton');
    const cameraStream = document.getElementById('cameraStream');

    const capturedOverlay = document.getElementById('capturedOverlay');
    const closeCapturedButton = document.getElementById('closeCapturedButton');
    const retakeButton = document.getElementById('retakeButton');
    const usePhotoButton = document.getElementById('usePhotoButton');
    const capturedImagesContainer = document.getElementById('capturedImages');
    let capturedImage = null;

    cameraButton.addEventListener('click', () => {
        cameraOverlay.style.display = 'flex';
        navigator.mediaDevices.getUserMedia({
            video: {
                facingMode: { exact: "environment" }
            },
            audio: false
        })
        .then(stream => {
            cameraStream.srcObject = stream;
        })
        .catch(err => {
            console.error('Error accessing camera:', err);
        });
    });

    closeCameraButton.addEventListener('click', () => {
        cameraOverlay.style.display = 'none';
        let stream = cameraStream.srcObject;
        if (stream) {
            let tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            cameraStream.srcObject = null;
        }
    });

    captureButton.addEventListener('click', () => {
        let canvas = document.createElement('canvas');
        canvas.width = cameraStream.videoWidth;
        canvas.height = cameraStream.videoHeight;
        let context = canvas.getContext('2d');
        context.drawImage(cameraStream, 0, 0, canvas.width, canvas.height);
        let imageData = canvas.toDataURL('image/png');

        capturedImage = imageData;

        capturedImagesContainer.innerHTML = `<img src="${capturedImage}" alt="Captured Image">`;

        cameraOverlay.style.display = 'none';
        capturedOverlay.style.display = 'flex';
    });

    closeCapturedButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        capturedImage = null;
        capturedImagesContainer.innerHTML = '';
    });

    retakeButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        capturedImage = null;
        capturedImagesContainer.innerHTML = '';
        cameraOverlay.style.display = 'flex';
    });

    usePhotoButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        const chatContainer = document.querySelector('.chat-container');
        const newMessage = document.createElement('div');
        newMessage.className = 'message chulsoo';
        newMessage.innerHTML = `<img src="${capturedImage}" alt="Captured Image" style="width: 100%;">`;
        chatContainer.appendChild(newMessage);
        capturedImage = null;
    });
});
