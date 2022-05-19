
function classChange(new_font) {
    var current = document.querySelectorAll(".active")[0];
    let current_font = (current.id).slice(3);

    if (current_font !== new_font) {
        let t_box = document.getElementById("write-space");

        while (t_box.classList.length > 0) {
            t_box.classList.remove(t_box.classList.item(0));
        }

        t_box.classList.add(new_font);
        
        current.classList.remove("active");
        document.querySelector("#rad" + new_font).classList.add("active");
    }
}

document.getElementById("radbold").addEventListener("click", function() {
    classChange("bold")
});
document.getElementById("radold").addEventListener("click", function() {
    classChange("old")
});
document.getElementById("radwild").addEventListener("click", function() {
    classChange("wild")
});