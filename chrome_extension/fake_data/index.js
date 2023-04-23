const button = document.querySelector("button");
button.addEventListener("click", () => {
  const result = document.getElementById("result");
  result.innerText = result.innerText.length === 0
    ? 'This is the result!'
    : ''
})
