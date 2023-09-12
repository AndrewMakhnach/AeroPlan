document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("header-burger").addEventListener("click", function() {
        document.getElementById("header-burger").classList.toggle("active")
        document.getElementById("main-menu").classList.toggle("active")
        document.getElementById("button").classList.toggle("active")
    })
})