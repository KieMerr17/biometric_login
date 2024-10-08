// auth.js
async function authenticate() {
    try {
        const challenge = new Uint8Array(32);
        const allowCredentials = [{
            type: 'public-key',
            id: new Uint8Array(32)
        }];

        const credentials = await navigator.credentials.get({
            publicKey: {
                challenge: challenge,
                allowCredentials: allowCredentials,
                timeout: 60000
            }
        });

        if (credentials) {
            window.parent.postMessage('auth-success', '*'); // Notify the parent window
        }
    } catch (error) {
        alert("Authentication failed: " + error);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // Trigger authentication when the QR code is clicked
    document.getElementById('qrCode').addEventListener('click', authenticate);
});
