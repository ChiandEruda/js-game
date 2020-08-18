var Game = function() {
    var g = {
        score: 0,
        left: false,
        right: false,
        paused: false,
    }

    var canvas = document.querySelector('#id-canvas')
    var context = canvas.getContext('2d')

    g.canvas = canvas
    g.context = context

    // 监听按键 'a' 和 'd' 状态
    window.addEventListener('keydown', function(event) {
        if (event.key == 'a') {
            g.left = true
        }
        if (event.key == 'd') {
            g.right = true
        }
    })

    window.addEventListener('keyup', function(event) {
        if (event.key == 'a') {
            g.left = false
        }
        if (event.key == 'd') {
            g.right = false
        }
    })

    window.addEventListener('keydown', function(event) {
        if (event.key == 'q') {
            g.paused = !g.paused
        }
    })

    g.drawImage = function(image, x, y, w, h) {
        context.drawImage(image, x, y, w, h)
    }

    setInterval(function() {
        g.update()
        context.clearRect(0, 0, 800, 600)
        g.draw()
    }, 1000/30)

    return g
}
