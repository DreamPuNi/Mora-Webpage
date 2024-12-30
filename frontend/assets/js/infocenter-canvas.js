// 获取指定日期的字符串格式
// offset: 与当前日期的天数偏移（负数表示过去，正数表示未来）
// 返回值：格式为 "YYYY-MM-DD" 的日期字符串
const getDateString = (offset) => {
    const date = new Date(); // 创建当前日期对象
    date.setDate(date.getDate() + offset); // 调整日期为偏移后的日期
    // 获取本地时间的年、月、日
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0"); // 月份从 0 开始，需要加 1
    const day = String(date.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
};

const startTime = getDateString(-6);
const endTime = getDateString(0);

// 构建 API 请求的 URL
const apiURL = `http://127.0.0.1:8000/api/usdcny_rate?start_time=${startTime}&end_time=${endTime}`;

// 向 API 发送请求并获取数据
fetch(apiURL)
    .then(response => response.json()) // 将响应解析为 JSON 格式
    .then(data => {
        if (data.status === "success") { 
            // 提取汇率数据并转换为浮点数，同时反转数组顺序
            const rates = data.usd_to_cny.map(entry => parseFloat(entry.rate)).reverse(); 
            if (rates.length > 1) { // 确保有足够的数据点绘制折线图
                drawLineChart(rates); // 调用绘图函数
            } else {
                console.error("Not enough data points to draw the chart."); // 数据点不足时输出错误
            }
        } else {
            console.error("Failed to fetch data:", data); // 请求失败时输出错误信息
        }
    })
    .catch(error => console.error("Error fetching data:", error)); // 捕获网络或解析错误

// 绘制折线图函数
// 参数 data: 汇率数据的数组，每个值对应一个数据点
function drawLineChart(data) {
    const canvas = document.getElementById("exchangeRateChart"); // 获取画布元素
    const ctx = canvas.getContext("2d"); // 获取 2D 绘图上下文

    const width = canvas.width; // 画布的宽度
    const height = canvas.height; // 画布的高度

    // 设置画布边距，实际绘图区域会缩小
    const padding = 10; 
    const chartWidth = width - 2 * padding; // 去除左右边距后的绘图宽度
    const chartHeight = height - 2 * padding; // 去除上下边距后的绘图高度

    // 计算每个数据点之间的水平间隔
    const pointSpacing = chartWidth / (data.length - 1); 

    // 计算数据的最大值和最小值，用于归一化处理
    const maxRate = Math.max(...data); 
    const minRate = Math.min(...data); 

    // 调整缩放比例和垂直偏移
    const amplitudeFactor = 0.5; // 缩放比例
    const verticalOffset = (1 - amplitudeFactor) / 2; // 垂直偏移量，确保图线居中

    // 转换数据到坐标系（调整幅度）
    const points = data.map((rate, index) => ({
        x: padding + index * pointSpacing,
        y: padding + chartHeight * (1 - (verticalOffset + amplitudeFactor * (rate - minRate) / (maxRate - minRate))),
    }));

    // 清空画布，防止覆盖已有内容
    ctx.clearRect(0, 0, width, height); 

    // 开始绘制折线
    ctx.beginPath(); 
    ctx.moveTo(points[0].x, points[0].y); // 移动画笔到第一个点
    points.slice(1).forEach(point => { 
        ctx.lineTo(point.x, point.y); // 依次连接后续点
    });
    ctx.strokeStyle = "#009bf5"; // 设置折线颜色（绿色）
    ctx.lineWidth = 2; // 设置折线宽度
    ctx.stroke(); // 绘制折线

    // 绘制数据点
    ctx.fillStyle = "#009bf5"; // 设置点的颜色（橙色）
    points.forEach(point => {
        ctx.beginPath();
        ctx.arc(point.x, point.y, 3, 0, Math.PI * 2); // 绘制一个半径为3的圆
        ctx.fill(); // 填充圆形
    });
}
