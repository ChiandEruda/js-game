var Doctor = function() {
    var d = {
        image: imageFromPath('img/失智博士.png'),
        x: 300,
        y: 500,
        w: 200,
        h: 100,
    }
    // 左右横跳逻辑
    d.左横 = function() {
        d.x -= 10
        if (d.x < -50) {
            d.x = 0
        }
    }
    d.右跳 = function() {
        d.x += 10
        if (d.x > 650) {
            d.x = 600
        }
    }
    
    return d 
}