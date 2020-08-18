游戏笔记 - 1

######################### 阶段1 #########################
    
    创建画布标签，选取元素 - document.querySelector('#id-canvas')

    搜索 Canvas API - mdn canvas image - ctx.drawImage

    ======================================================
    图像加载不了 - var log = console.log
        JS 里外部资源的加载是在最后的
        动态创建的标签 src 属性发送请求是【异步】的
        canvas 还没渲染，所以 querySelector 选不到
        创建画布放入 img.onload = function() {}
    ******************************************************

    修改坐标 - ctx.drawImage(img, 150 ,200)

    绑定按键事件 - window.addEventListener('keydown', function() {})

    log(event) 查询出 'key' 属性

    编写往左往右的逻辑 - if (k == 'a')

    =======================================================
    编写游戏的套路 - 清空画布，改变坐标，再次清空 - x -= 10
    ******************************************************

    坐标添加变量 - var x - ctx.drawImage(img, x, y)

    搜索清空画布 - mdn canvas clear 
        context.clearRect(0, 0, canvas.width, canvas.height)

    清空后再画 - ctx.drawImage(img, x, y)

    查看按住后的 keydown 事件 - log('keydown') - 秒触发数不够

    用定时器提高秒触发 - setInterval(function() {}, 1000/30)
        将 ctx.clearRect 和 ctx.drawImage 放入

    =======================================================
    新建变量 leftDown rightDown 保存按键状态，并放入事件监听来判断，事件监听里因按键状态而改变的左右状态放入定时器里移动才顺滑
        var leftDown = false
        var rightDown = flase

        if k == 'a' leftDown = true
        if k == 'd' rightDown =true

    为了清除状态，还要监听 'keyup'事件 - 复制 'keydown' 事件
        Window.addEventListener('keyup', function(event) {})
    ******************************************************

    添加 speed 变量 - var speed = 5

    代码不要直接从上写到下流水账，最外层只应有函数不应有变量，只有一个入口 - 封装

######################### 阶段2 #########################
    
    定义入口 - _main() - var _main = function() {}
        直接全部包进去也能运行

    初级拆分 - paddle - 事件监听 - 定时器

    将 paddle 拨出去变成对象 - var Paddle = function() {}
        var o = {} return o

    对象 o 需要一个 image 属性，则在外层创建一个 image 变量，image 变量需要载入图片，则在更外层创建一个载入函数
        var image = imageFromPath(paddle.png)

        var imageFromPath = function(path) {
            var img = new Image()
            img.src = path
            return img
        }

    对象 o 继续封装 x, y, speed

    删除封装后剩下的残渣

    为何这里直接不需要 img.onload 了
        img.onload = function() {
            context.drawImage(img, x, y)
        }

    创建对象实例 - var paddle = Paddle()

    修改程序内 paddle 对象涉及的变量

    记得边改边测试，不要一下子写一大段代码

    定时器里的状态改变用函数来代替，不要纠缠在一起 - 41:56
        o.moveLeft() = function() {}
        o.moveRight() = function() {}

    之前的 Paddle 出了 BUG - var paddle = o 

######################### 阶段3 #########################
    
    将 canvas context addEventListener setInterval 封闭入 game

    先封装 canvas 和 context
        GuaGame() 封装个 g 对象
        再将外层定时器的 can ctx 先改下

        var g = {}
        var canvas = ...
        var context = ...
        g.canvas = canvas
        g.context = context
        return g

    再封装 addEventListener, 不封装的话以后一堆 event 很恶心

    先监听事件储存 key 的状态，之后再遍历状态储存 key 注册的方法

    g 对象添加两个对象，储存的 key 的状态和注册的方法
        var g = {
            keydowns: {}
            actions: {},  
        }

    添加按下事件监听,改变 keydowns 储存的对应状态
        window.addEventListener('keydown', function(event) {
            g.keydowns[event.key] = true
        })

    添加按起事件监听,改变 keydowns 储存的对应状态
        window.addEventListener('keyup', function(event) {
            g.keydowns[event.key] = false
        })

    =======================================================
    在定时器里检查遍历 actions 的全部事件 - 54:28
    即 for in 出 actions 的 key 给 keydowns 用作判断状态

        var actions = Objects.keys(g.actions)
        for (var i = 0; i < actions.length; i++) {
            var key = actions[i]
            if (g.keydowns[key]) {
                g.actions[key]()
            }
        }
    ******************************************************

    添加事件注册调用,外层的注册调用储存在 actions 里面
        g.registerAction = function(key, callback) {
            g.actions[key] = callbacks
        }

    在外层注册左右移动函数
        game.registerAction('a', function() {
            paddle.moveLeft()
        })

######################### 阶段4 #########################

    接着封装外层定时器里的 draw 和 clear

    clear 可以直接封入 game 定时器，但 draw 调用了外层 paddle 的参数，需要在外层暴露 api 接口用来注册
        game.draw = function() {}
        var p = paddle
        game.context.drawImage(p.img, p.x, p.y)

    game 定时器里放入未定义的 g.draw()

    g.draw() 之前要 clear 
        g.context.clearRect(0, 0, g.canvas.width, g.canvas.height)

    game.draw 的调用再进一步封装 game.drawImage(img) 作为接口
        game.draw = function() {
            game.drawImage(paddle)
        }

        g.drawImage = function(img) {
            g.context.drawImage(img.img, img.x, img.y)
        }

######################### 阶段5 #########################

    创建 Ball() 对象 实例化 更新状态 画布

    Game 定时器添加 g.update() 用于更新 ball 状态

    对象添加 fired: false 属性判断启动

    添加 o.move = function() {}

    注册 ball.fire() 按键

    o.move 添加弹框逻辑 - o.speedX o.speedY

    Paddle 添加碰撞逻辑 - o.collide = function(img) {}

    game.update 判断碰撞
        if (paddle.collide(ball)) {}























