// 夜间模式切换
const themeToggle = document.getElementById('theme-toggle'); // 获取页面中 ID 为 'theme-toggle' 的元素（通常是一个按钮或图标）
if (themeToggle) { // 检查是否成功获取到该元素，防止出现未找到元素的错误
    themeToggle.addEventListener('click', () => { // 如果元素存在，为其添加一个点击事件监听器
        document.body.classList.toggle('dark-mode'); //切换 <body> 元素的 'dark-mode' 类
    });
}

// 语言切换
const languageSelect = document.getElementById('language-select');
if (languageSelect) {
    languageSelect.addEventListener('change', (event) => {
        const selectedLanguage = event.target.value;
        alert(`语言切换到：${selectedLanguage === 'zh' ? '中文' : 'English'}`);
        // 可以根据语言选择动态加载不同的内容，以下为占位逻辑
    });
}

// 内部标签页切换
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const sectionId = link.dataset.section;

        // 隐藏所有页面
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });

        // 显示目标页面
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.add('active');
        }
    });
});