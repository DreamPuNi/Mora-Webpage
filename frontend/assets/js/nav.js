// 夜间模式切换
const themeToggle = document.getElementById('theme-toggle'); // 获取页面中 ID 为 'theme-toggle' 的元素（通常是一个按钮或图标）
if (themeToggle) { // 检查是否成功获取到该元素，防止出现未找到元素的错误
    themeToggle.addEventListener('click', () => { // 如果元素存在，为其添加一个点击事件监听器
        document.body.classList.toggle('dark-mode'); //切换 <body> 元素的 'dark-mode' 类
    });
}

document.addEventListener("DOMContentLoaded", function () {
    // 语言切换
    const languageButton = document.getElementById("language-button");
    const languageOptions = document.getElementById("language-options");

    // 用户登陆
    const userButton = document.getElementById("user-button");
    const userInfo = document.getElementById("user-info");

    // 点击按钮时切换语言列表显示状态
    languageButton.addEventListener("click", function (event) {
        event.stopPropagation(); // 防止点击事件冒泡到 document
        languageOptions.classList.toggle("hidden");
    });

    // 点击按钮时切换用户信息显示状态
    userButton.addEventListener("click", function (event) {
        event.stopPropagation(); // 防止点击事件冒泡到 document
        userInfo.classList.toggle("hidden");
    });

    // 点击页面其他地方关闭语言列表和用户信息
    document.addEventListener("click", function (event) {
        // 关闭语言列表
        if (!languageButton.contains(event.target) && !languageOptions.contains(event.target)) {
            languageOptions.classList.add("hidden");
        }

        // 关闭用户信息
        if (!userButton.contains(event.target) && !userInfo.contains(event.target)) {
            userInfo.classList.add("hidden");
        }
    });
});

// 登陆状态管理
document.addEventListener("DOMContentLoaded",function(){
    fetch("http://127.0.0.1:8000/users/user_info/",{
        method: "GET",
        credentials: "include",//发送请求时包含cookies
    })
        .then((response) => {
            if (response.ok){
                return response.json();
            } else {
                throw new Error("未登录或获取用户信息失败");
            }
        })
        .then((data) => {
            //更新页面内容
            const userInfoDiv = document.getElementById("user-info");

            const adminLink = data.is_superuser
                ? `<a href="http://127.0.0.1:8000/admin" class="user-link">超级管理后台</a>`
                : '';

            const staffLink = data.is_staff
                ? `<a href="http://127.0.0.1:5500/staff" class="user-link">你是员工</a>`
                : '';
            
            userInfoDiv.innerHTML = `
                <img src="assets/icons/user.png">
                <h4>欢迎，${data.username}</h4>
                ${staffLink}
                ${adminLink}
                <a href="#" class="user-link" onclick="logout()">退出登陆</a>
            `;
            userInfoDiv.classList.remove("hidden");
        })
        .catch((error) => {
            console.error(error);
        });
})

function logout(){
    fetch('http://127.0.0.1:8000/users/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // 获取 CSRF Token
        },
        credentials: 'include', // 确保请求携带 Cookie
    })
    .then(response => {
        if (response.ok){
            window.location.href = '/';
        } else {
            alert('登出失败');
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {// 从浏览器Cookie中获取CSRF令牌
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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