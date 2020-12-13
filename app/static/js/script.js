var checkbox = document.getElementById('add-critere2')
checkbox.addEventListener('change', function() {
    if (this.checked) {
        var inputCri2 = document.getElementById('input-critere2')
        inputCri2.setAttribute('type', 'text')
    } else {
        var inputCri2 = document.getElementById('input-critere2')
        inputCri2.setAttribute('type', 'hidden')
    }
})



