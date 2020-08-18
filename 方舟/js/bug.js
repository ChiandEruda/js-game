var Bug = function(position) {
    var p = position
    var b = {
        image: imageFromPath('img/源石虫.png'),
        x: p[0],
        y: p[1],
        w: 200,
        h: 100,
        alive: true,
    }

    b.die = function() {
        b.alive= false
    }
    return b
}

var _bugs = [
    [0, 0],
    [300, 0],
    [600, 0],
    [0, 100],
    [600, 100],
]