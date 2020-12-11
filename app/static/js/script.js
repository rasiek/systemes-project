
function addCritere() {
    var x = document.getElementById("new-critere")
    if (x.style.display === "none") {
        x.style.display = "flex";
    } else {
        x.style.display = "none";
    }
}

function sendForms() {
    
    document.getElementById("form-recherche").submit();
    document.getElementById("form-recherche2").submit();
}