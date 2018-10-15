const snapElement = document.querySelector('#snap');
const charactersElement = document.querySelector('.characters')
const thanosElement = document.querySelector('#thanos')
const theBalance = document.querySelector('#theBalance')
const audioElement = new Audio('static/sound/intro.mp3');


audioElement.play();
snapElement.style.opacity = '0';
theBalance.style.opacity = '0'

thanosElement.addEventListener('click', () => {
    snapElement.style.opacity = '1';

    setTimeout(() => {
        audioElement.pause();
        audioElement.currentTime = 0;
        audioElement.src = 'static/sound/snap.mp3';
        audioElement.play();
        snapElement.style.opacity = '0';

        setTimeout(() => {
            audioElement.pause();
            audioElement.currentTime = 0;
            audioElement.src = 'static/sound/funeral.mp3';
            audioElement.play();
            balanceUniverse();

        }, 2000)

    }, 3000)
})

function balanceUniverse() {
    const characters = [].slice.call(document.querySelectorAll('.character'));
    let leftToDie = Math.floor(characters.length / 2);

    kill(characters, leftToDie)

}

function kill(characters, leftToDie) {
    if (leftToDie > 0) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        const [characterChosen] = characters.splice(randomIndex, 1);
        characterChosen.style.transform = 'scale(0)';
        characterChosen.classList.remove('alive')
        characterChosen.classList.add('dead');


        setTimeout(() => {
            kill(characters, leftToDie - 1)
        }, 1000)
    } else {
        document.querySelectorAll('.dead').forEach(character => {
            charactersElement.removeChild(character);
        });
        theBalance.style.opacity = '1'
    }
}