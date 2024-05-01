document.addEventListener("DOMContentLoaded", function () {
    const balloonsContainer = document.getElementById('balloons-container');

    function createBalloon() {
        const balloon = document.createElement('div');
        balloon.className = 'balloon';

        const emojis = ['🏆', '🌏', '⚽️'];

        emojis.forEach(emoji => {
            const emojiSpan = document.createElement('span');
            emojiSpan.innerText = emoji;
            emojiSpan.style.fontSize = '0.5em';  // modifica para cambiar el tamaño de lo emojis

            const positionX = Math.random() * (window.innerWidth - 40);
            const positionY = Math.random() * (window.innerHeight - 40);

            emojiSpan.style.position = 'absolute';
            emojiSpan.style.left = positionX + 'px';
            emojiSpan.style.top = positionY + 'px';

            balloon.appendChild(emojiSpan);
        });

        balloonsContainer.appendChild(balloon);

        setTimeout(() => {
            balloon.remove();
        }, 5000);
    }

    setInterval(createBalloon, 1000);  // cantidad de balones aparecidos durante el intervalo de tiempo de:
});
