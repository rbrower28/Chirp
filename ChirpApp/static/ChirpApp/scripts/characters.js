
const textarea = document.querySelector("textarea");

textarea.addEventListener("keyup", function() {
  var answer = document.querySelector("textarea").value;
  var remaining = 200 - answer.length;
  document.getElementById("characters-left").textContent = remaining;
})