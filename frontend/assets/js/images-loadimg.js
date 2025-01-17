document.addEventListener("DOMContentLoaded", () => {
    const libraryContainer = document.getElementById("slides");

    async function loadimgs() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/imgs_info/`);
            const result = await response.json(); // 这里获取的是包含 status 和 data 的对象
            const data = result.data; // 访问 data 数组

            libraryContainer.innerHTML = ""; // 清空容器

            data.forEach((img) => {
                const imgUrl = `http://127.0.0.1:8000${img.image_url}`;
                const slide = `
                    <div class="slide">
                        <img src="${imgUrl}" alt="${img.title}">
                        <h2 class="title">${img.title}</h2>
                        <p>${img.introduce}</p>
                    </div>
                `;
                libraryContainer.insertAdjacentHTML("beforeend", slide);
            });

            initializeSlides(); // 确保内容加载完成后初始化
        } catch (error) {
            console.error("Error loading books:", error);
        }
    }

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

    loadimgs();
});
