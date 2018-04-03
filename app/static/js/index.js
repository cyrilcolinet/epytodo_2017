var buttons = document.querySelectorAll('button')

for (var i = 0; i < buttons.lenght; i++) {
        var x = buttons[i]
        x.addEventListener('click', function() {
        this.classList.add('red')
        })
}
