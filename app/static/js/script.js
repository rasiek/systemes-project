document.addEventListener("DOMContentLoaded", () => {
    const formRecherche = document.getElementById("form-recherche")
    formRecherche.addEventListener("submit", (evt) => {
        const jsonData = evt.target.responseText
        console.log(jsonData)
    })
})