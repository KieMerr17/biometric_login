// Trigger authentication
async function authenticate() {
    try {
        const credentials = await navigator.credentials.get({
            publicKey: {
                challenge: new Uint8Array([/* Server-sent random bytes */]),
                allowCredentials: [
                    { type: 'public-key', id: new Uint8Array([/* Server-sent credential ID */]) }
                ],
                timeout: 60000
            }
        });

        window.location.href = '/full-content.html';
    } catch (error) {
        alert("Authentication failed: " + error);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const isAuthPage = window.location.pathname.includes('authenticate');

    if (isAuthPage) {
        authenticate();
    }
});