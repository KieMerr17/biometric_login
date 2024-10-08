document.getElementById('qr-code').addEventListener('click', async function () {
    const code = prompt("Please enter the access code:");

    if (code) {
        const response = await fetch('/verify_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        });

        if (response.ok) {
            document.getElementById('full-content').style.display = 'block'; // Show content if authenticated
            document.getElementById('qr-code').style.display = 'none'; // Hide QR code
        } else {
            alert("Authentication failed: Invalid code");
        }
    } else {
        alert("No code entered");
    }
});