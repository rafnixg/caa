// TIKETS


const addButton = document.getElementById('addTicket')
const removeButton = document.getElementById('removeTicket')

const inputTickets = document.getElementById('tickets')

addButton.addEventListener('click', (event) => {
    inputTickets.value = parseInt(inputTickets.value) + 1
})

removeButton.addEventListener('click', (event) => {
    if (inputTickets.value > 1) {
        inputTickets.value -= 1
    }
})


// VIDEO
/*const video = document.getElementById('video')
const playButton = document.getElementById('play')

if (video && playButton) {
    playButton.addEventListener('click', (event) => {
        if (video.paused) {
            video.play()
            playButton.classList.add('fade-out')
        } else {
            video.pause()
        }
        
    })

    playButton.addEventListener('mouseover', (event) => {
        playButton.classList.remove('fade-out')
        playButton.classList.add('fade-in')
    })
    
    video.addEventListener('mouseover', (event) => {
        if (!video.paused) {
            playButton.classList.remove('fade-out')
            playButton.classList.add('fade-in')
        }
    })
    
    video.addEventListener('mouseout', (event) => {
        if (!video.paused) {
            playButton.classList.remove('fade-in')
            playButton.classList.add('fade-out')
        }
    })
}*/
