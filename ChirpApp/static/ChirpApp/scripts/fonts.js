
function classChange(new_font) {
    var current = document.querySelectorAll(".active")[0];

    const fontdict = {
        "bold": "#id_font_0",
        "old": "#id_font_1",
        "wild": "#id_font_2"
    };

    let t_box = document.querySelector("textarea");

    while (t_box.classList.length > 0) {
        t_box.classList.remove(t_box.classList.item(0));
    }
    t_box.classList.add(new_font);
    current.classList.remove("active");
    
    let label = document.querySelector(fontdict[new_font]).parentElement;
    label.parentElement.classList.add("active");

}

const divs = document.getElementById("id_font").childNodes;
divs[0].classList.add("active");

document.getElementById("id_font_0").parentElement.addEventListener("click", function() {
    classChange("bold")
});
document.getElementById("id_font_1").parentElement.addEventListener("click", function() {
    classChange("old")
});
document.getElementById("id_font_2").parentElement.addEventListener("click", function() {
    classChange("wild")
});