
const codes = document.querySelectorAll("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > div > pre > span");

const sourceCode = []
codes.forEach(ele => {
    sourceCode.push(ele.textContent)
});

// console.log(sourceCode)

window.localStorage.setItem("sourceCode", JSON.stringify(sourceCode))
window.localStorage.setItem("flag", 1)
window.close()