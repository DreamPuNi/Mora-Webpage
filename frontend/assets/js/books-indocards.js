// 等待DOM完全加载后执行
document.addEventListener("DOMContentLoaded", () => {
    // 获取书籍展示的容器
    const libraryContainer = document.getElementById("card-library");

    async function loadBooks(tag = "all") {
        try {
            // 发起Fetch请求，向后端获取指定标签的书籍数据
            const response = await fetch(`http://127.0.0.1:8000/api/books_info?tag=${tag}`);
            // 解析返回的JSON数据
            const data = await response.json();

            // 清空书籍容器中的旧内容
            libraryContainer.innerHTML = "";

            // 遍历返回的数据，为每本书创建对应的HTML结构
            data.forEach((book) => {
                // 动态生成书籍卡片HTML
                const card = `
                    <div class="info-card">
                        <!-- 封面图片，链接到书籍详情页 -->
                        <a class="cover" href="${book.link}">
                            <img src="${book.cover}" alt="${book.title}">
                        </a>
                        <!-- 信息展示部分 -->
                        <div class="information">
                            <h2 class="title">
                                <a class="title-container" href="${book.link}" title="${book.title}" itemprop="name">
                                    <span class="title-text">${book.title}</span>
                                </a>
                            </h2>
                            <!-- 作者信息 -->
                            <small class="text-uppercase fw-semibold ls-md">${book.author}</small>
                            <!-- 书籍简介 -->
                            <a href="${book.link}">
                                <span class="description_text">${book.description}</span>
                                <span class="mora_review" style="display: block;">${book.review}</span>
                            </a>
                        </div>
                    </div>
                `;
                // 将生成的卡片HTML插入到容器中
                libraryContainer.insertAdjacentHTML("beforeend", card);
            });
        } catch (error) {
            // 捕获并输出加载过程中的错误
            console.error("Error loading books:", error);
        }
    }

    // 初始化页面时，加载所有书籍信息
    loadBooks();

    // 为每个标签按钮绑定点击事件，用于筛选书籍
    document.querySelectorAll(".tag-button").forEach((button) => {
        button.addEventListener("click", () => {
            // 获取按钮上的data-tag属性值（对应筛选条件）
            const tag = button.getAttribute("data-tag");
            // 根据标签筛选加载书籍
            loadBooks(tag);
        });
    });
});
