function func(x, yes, no){
    if (x > -2){
        console.log(yes(x));
    }
    else if (x <= -2){
        console.log(no(x));
    }
}
let x = +prompt('Введите х')
func(x, (x) => (2 * Math.pow(x, 2) + 3), (x) => (4 * x))
console.log(func)