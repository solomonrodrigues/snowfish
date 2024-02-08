const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]}|;:,<.>/?';

function getRandomCharacter() {
    const randomIndex = Math.floor(Math.random() * characters.length);
    return characters[randomIndex];
}

function updateSnowfishArt() {
    const snowfishArt = document.getElementById('snowfishArt');
    const lines = snowfishArt.innerText.trim().split('\n');

    const updatedLines = lines.map(line => {
        let updatedLine = '';
        for (const char of line) {
            if (char === ' ' || char === '$t') {
                updatedLine += char;
            } else {
                updatedLine += getRandomCharacter();
            }
        }
        return updatedLine;
    });

    snowfishArt.innerText = updatedLines.join('\n');
}

setInterval(updateSnowfishArt, 100);