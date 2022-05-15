
const textarea = document.getElementById("write-space");

textarea.addEventListener("keyup", function() {
  var answer = document.getElementById("write-space").value;
  var remaining = 200 - answer.length;
  document.getElementById("characters-left").textContent = remaining;
})