const img = new Image();

let btn = document.getElementById('dims')

let wd = 0;
let ht = 0;

img.onload = function() {
    console.log(`width : ${this.width}, height : ${this.height}`)
    wd = this.width
    ht = this.height
}


img.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZHo_RMM0cMQFsh3Qf8myGeVppIMZcHg0nJw&usqp=CAU';

btn.addEventListener('click', () => {
    console.log(wd, ht)
})


console.log("Hello World!")

