<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>地图展示</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <style>
    body,
    html,
    #container {
        overflow: hidden;
        width: 100%;
        height: 100%;
        margin: 0;
        font-family: "微软雅黑";
    }
    .info {
        z-index: 999;
        width: auto;
        min-width: 22rem;
        padding: .75rem 1.25rem;
        margin-left: 1.25rem;
        position: fixed;
        top: 1rem;
        background-color: #fff;
        border-radius: .25rem;
        font-size: 14px;
        color: #666;
        box-shadow: 0 2px 6px 0 rgba(27, 142, 236, 0.5);
    }
    </style>
    <script src="//api.map.baidu.com/api?type=webgl&v=1.0&ak=您的密钥"></script>
</head>
<body>
    <div class = "info">最新版GL地图命名空间为BMapGL, 可按住鼠标右键控制地图旋转、修改倾斜角度。</div>
    <div id="container"></div>
</body>
</html>
<script>
var map = new BMapGL.Map('container'); // 创建Map实例
map.centerAndZoom(new BMapGL.Point(116.404, 39.915), 12); // 初始化地图,设置中心点坐标和地图级别
map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放
</script>
