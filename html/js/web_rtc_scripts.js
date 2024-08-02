function fnCameraStream() {
    let cameraOverlay = document.getElementById('cameraOverlay');
    let cameraStream = document.getElementById('cameraStream');

    cameraOverlay.style.display = 'flex';
        
    let stream = cameraStream.srcObject;
    if (stream) {
        let tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        cameraStream.srcObject = null;
    }

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
}

document.addEventListener('DOMContentLoaded', () => {
    let cameraButton = document.querySelector('.camera');
    let cameraOverlay = document.getElementById('cameraOverlay');
    let closeCameraButton = document.getElementById('closeCameraButton');
    let captureButton = document.getElementById('captureButton');
    let cameraStream = document.getElementById('cameraStream');

    let capturedOverlay = document.getElementById('capturedOverlay');
    let closeCapturedButton = document.getElementById('closeCapturedButton');
    let retakeButton = document.getElementById('retakeButton');
    let usePhotoButton = document.getElementById('usePhotoButton');
    let capturedImagesContainer = document.getElementById('capturedImages');
    let capturedImage = null;

    cameraButton.addEventListener('click', () => {
        fnCameraStream();
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
        capturedImage = canvas.toDataURL('image/png');
        capturedImagesContainer.innerHTML = `<img src="${capturedImage}" alt="Captured Image">`;
        cameraOverlay.style.display = 'none';
        capturedOverlay.style.display = 'flex';
        
        let stream = cameraStream.srcObject;
        if (stream) {
            let tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            cameraStream.srcObject = null;
        }
    });

    closeCapturedButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        capturedImage = null;
        capturedImagesContainer.innerHTML = '';
        
        let stream = cameraStream.srcObject;
        if (stream) {
            let tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            cameraStream.srcObject = null;
        }
    });

    retakeButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        capturedImage = null;
        capturedImagesContainer.innerHTML = '';
        fnCameraStream();
    });

    usePhotoButton.addEventListener('click', () => {
        capturedOverlay.style.display = 'none';
        const chatContainer = document.querySelector('.chat-container');
        let newMessage = document.createElement('div');
        newMessage.className = 'message chulsoo';
        newMessage.innerHTML = `<img src="${capturedImage}" alt="Captured Image" style="width: 100%;">`;
        chatContainer.appendChild(newMessage);
        capturedImage = null;
    });
});
