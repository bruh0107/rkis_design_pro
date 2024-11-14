const sliderWrapper = document.querySelector('.slider-wrapper')
const nextBtn = document.querySelector('.next-btn')
const prevBtn = document.querySelector('.prev-btn')
let currentIndex = 0

function sliderFunc(index){
    const allSlides = document.querySelectorAll('.slider-item').length
    if(index >= allSlides){
        currentIndex = 0
    }
    else if (index < 0){
        currentIndex = allSlides - 1
    }
    else{
        currentIndex = index
    }

    const offset = -currentIndex * 100
    sliderWrapper.style.transform = `translateX(${offset}%)`
}

prevBtn.addEventListener('click', () => {
    sliderFunc(currentIndex - 1)
})

nextBtn.addEventListener('click', () => {
    sliderFunc(currentIndex + 1)
})