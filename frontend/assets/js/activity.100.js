// 获取 <li> 元素
const layoutButton = document.getElementById("layout");

// 绑定点击事件
layoutButton.addEventListener("click", function (event) {
    event.preventDefault(); // 阻止默认行为

    // 获取当前模式
    const currentMode = layoutButton.getAttribute("data-mode");

    // 根据当前模式切换
    if (currentMode === "page") {
        layoutButton.setAttribute("data-mode", "scroll"); // 切换为滑动阅读
        console.log("切换到滑动阅读模式");
        // TODO: 在这里加入切换到滑动阅读的逻辑
    } else {
        layoutButton.setAttribute("data-mode", "page"); // 切换为翻页阅读
        console.log("切换到翻页阅读模式");
        // TODO: 在这里加入切换到翻页阅读的逻辑
    }
});
