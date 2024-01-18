function getSourceCode() {
  
  const codes = document.querySelectorAll(
    "#submit_form > div:nth-child(5) > div > div > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > div > pre > span"
    );
  if(codes){
      const sourceCode = [];
      codes.forEach((ele) => {
      sourceCode.push(ele.textContent);
      });
    
      window.localStorage.setItem("sourceCode", sourceCode)
      console.log(sourceCode)
    }
    else{
      console.log("empty")
    }
    
}

setInterval(getSourceCode, 1000);