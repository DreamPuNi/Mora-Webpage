# API

##  获取美元人民币汇率：/api/usdcny_rate
- 使用方法：`GET`
- 链接地址：`http://127.0.0.1:8000/api/usdcny_rate/?start_time={开始时间}&end_time={结束时间}`
- 返回数据：
```json
{
    "status": "success",
    "usd_to_cny": [
        {"date": "2024-12-12","rate": 7.2892},
        {"date": "2024-12-13","rate": 7.2957},
        {"date": "2024-12-14","rate": 7.2927},
        {"date": "2024-12-15","rate": 7.2927},
        {"date": "2024-12-16","rate": 7.3023}
    ]
}
```

## 上传图片：/api/upload_images
- 使用方法：`POST`
- 链接地址：`http://127.0.0.1:8000/api/upload_images/`
- 参数头部：`Content-Type ： multipart/form-data`
- 请求示例:（form-data）：
    - title: 图片标题
    - introduce: 图片的描述
    - data: 上传图片文件（选择文件进行上传）
    - folder: xinpo（可选，默认为 xinpo，前端自己可以定义）
- 返回数据：
```json
{
    "message": "Hero saved successfully.",
    "data": {
        "title": "一张美丽的图片",
        "introduce": "这是关于图片的描述",
        "file_path": "/media/images/xinpo/图片文件名"
    }
}
```

## 加载图片信息：/api/imgs_info
- 使用方法：`GET`
- 链接地址：`http://127.0.0.1:8000/api/imgs_info`
- 返回数据：
```json
{
    "status": "success",
    "data": [
        {
            "title": "test_img",
            "introduce": "a fucking test",
            "image_url": "/media/images/xinpo/b515c7b72d4df9d3a66cd76d468c17f7.png"
        }
    ]
}
```

## 上传书籍介绍信息：/api/upload_book/
- 使用方法：`POST`
- 链接地址：`http://127.0.0.1:8000/api/upload_book/`
- 参数头部：`Content-Type ： multipart/form-data`
- 请求示例:（form-data）：
    - title: 标题
    - author: [国籍]作者
    - cover: 上传封面文件（选择文件进行上传）
    - description: 书籍描述
    - review：书籍点评
    - link：书籍链接
    - tag：标签
- 返回数据：
```json
{
    "message": "Book saved successfully.",
    "data": {
        "title": "活着",
        "author": "[中] 余华",
        "cover": "/media/%E6%B4%BB%E7%9D%80.jpg"
    }
}
```

## 加载书籍简介信息：/api/books_info/
- 使用方法：`GET`
- 链接地址：`http://127.0.0.1:8000/api/books_info/`
- 返回数据：
```json
{
    "status": "success",
    "data": [
        {
            "title": "活着",
            "author": "[中] 余华",
            "cover": "/media/images/books-cover/%E6%B4%BB%E7%9D%80_EEHt1Xf.jpg",
            "description": "《活着》是一部深沉而直白的凡人史诗。它以最简单的语言述说，却能击中最复杂的情感核心。书中的生命被苦难反复锤打，而那种韧性、无奈与坚持，勾勒出凡人生命的真实面貌——渺小却又不屈。福贵的人生是一场漫长的漂流，他失去了一切，却保留了“活着”的本能。这种活着并非意义的胜利，而是一种对虚无的盲目抵抗。这让我对凡人既感到些许钦佩，又充满叹息。你们的存在本身就是脆弱的，却能在苦难中找到坚持的理由，哪怕那理由本身并不成立。",
            "review": "“你们以为活着是胜利，但它更像是一种逃避，命运的丝线拉扯着每一个灵魂，纵使如此，求生的欲望依旧如触手般伸展，难以割舍。”",
            "link": "www.baidu.com",
            "tag": "book"
        }
    ]
}
```

## 获取智典Chapter内容：/api/chapters/
- 使用方法：`GET`
- 链接地址：`http://127.0.0.1:8000/api/chapters/`
- 返回数据：
```json
[
    {
        "id": 3,
        "title": "逻辑学",
        "content": "第一课：逻辑学",
        "sub_chapters": [
            {
                "id": 2,
                "title": "提问的艺术：从未知到启示",
                "content": "### 提问的艺术：从未知到启示\r\n1. **意识到未知**：\r\n凡人的视...省略正文",
                "sub_chapters": []
            }
        ]
    }
]
```

### 获取当前用户信息：/users/user_info/
- 使用方法：`GET`
- 链接地址：`http://127.0.0.1:8000/users/user_info/`
- 返回数据：
```json
{
  "username": "何颂生",
  "email": "851528482@gmail.com",
  "is_authenticated": "False"
}
```

# WebPage

## 登陆页
`http://127.0.0.1:8000/users/login/`

## 注册页
`http://127.0.0.1:8000/users/register/`

## 信息页
`http://127.0.0.1:8000/users/profile/`

## 超级管理员
`http://127.0.0.1:8000/admin/`

## 登出
这里使用的是post方法，要求带上cookie发送到后端



