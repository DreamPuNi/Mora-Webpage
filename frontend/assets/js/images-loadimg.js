document.addEventListener("DOMContentLoaded", () => {
    const libraryContainer = document.getElementById("slides");

    async function loadimgs() {
        try{
            const response = await fetch(`http://127.0.0.1:8000/api/imgs_info`);
            const data = await response.json();
            libraryContainer.innerHTML = "";
            data.forEach((img) => {
                const slide = `
                    <div class="slide">
                        <img src="${img.data}" alt="${img.title}">
                        <h2 class="title">${img.title}</h2>
                        <p>${img.introduce}</p>
                    </div>
                `;
                libraryContainer.insertAdjacentHTML("beforeend", slide);
            })
        }
        catch (error){
            console.error("Error loading books:", error);
        }
    }

    loadimgs();
})

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelector('.slides');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    let currentIndex = 0;

    function updateSlidePosition() {
        slides.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    function initializeSlides() {
        const slideCount = document.querySelectorAll('.slide').length;
        if (slideCount > 0) {
            prevButton.addEventListener('click', () => {
                currentIndex = (currentIndex - 1 + slideCount) % slideCount;
                updateSlidePosition();
            });

            nextButton.addEventListener('click', () => {
                currentIndex = (currentIndex + 1) % slideCount;
                updateSlidePosition();
            });
            updateSlidePosition();
        } else {
            console.error("No slides found.");
        }
    }

    initializeSlides();

    // 如果动态加载幻灯片，使用 MutationObserver 监听
    const observer = new MutationObserver(() => {
        initializeSlides();
    });
    observer.observe(slides, { childList: true });
});
