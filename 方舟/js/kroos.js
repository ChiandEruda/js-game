var Kroos = function() {
    var k = {
        image: imageFromPath('img/克洛丝.png'),
        x: 350,
        y: 400,
        w: 100,
        h: 100,
        speedX: 10,
        speedY: 10,
    }

    k.move = function() {
        if (k.x < 0 || k.x > 800 - k.w) {
            k.speedX *= -1
        }
        if (k.y < 0 || k.y > 600 - k.h) {
            k.speedY *= -1
        }
        k.x += k.speedX
        k.y += k.speedY
    }

    k.被扼住了脖颈 = function(x, y) {
        if (x > k.x && x < k.x + k.w) {
            if (y > k.y && y < k.y + k.h) {
                return true
            }
        }
        return false
    }

    // 碰撞检测
    k.collide = function(b) {
        var s1 = k.x > b.x + b.w
        var s2 = k.x + k.w < b.x
        var s3 = k.y > b.y + b.h
        var s4 = k.y + k.h < b.y

        if (s1 || s2 || s3 || s4) {
            return false
        }
        return true
    }

    k.反弹 = function() {
        k.speedY *= -1
    }

    return k
}
