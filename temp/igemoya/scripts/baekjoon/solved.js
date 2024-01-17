const tr = document.querySelector('#status-table > tbody > tr');

function getSourceCode() {
    const url = document.querySelector(`#solution-${tr.children[0].textContent} > td:nth-child(7) > a:nth-child(1)`).getAttribute( 'href' );
    console.log(url)
    window.open("https://www.acmicpc.net" + url)
    }

function isStatusWaiting() {
    const resultProcess = document.querySelector('#status-table > tbody > tr :nth-child(4) > span').textContent
    return (resultProcess === "기다리는 중" 
    || resultProcess === "채점 준비 중" 
    || resultProcess.substring(0,4) === "채점 중" );
}
if (tr) {
async function waitForStatusChange() {
    
    if(window.localStorage.getItem("flag")===0){
        getSourceCode()
    }
    while (isStatusWaiting()) {
        // 1초마다 다시 체크
        await new Promise(resolve => setTimeout(resolve, 1000)); 
    }
}
// 변경되면,
waitForStatusChange()
.then(() => {
    if(document.querySelector('#status-table > tbody > tr :nth-child(4) > span').textContent !="틀렸습니다"){
    const col = tr.children;
    const jsonproblem = window.localStorage.getItem("problemData")
    const problem = JSON.parse(jsonproblem)
    const language = col[6].textContent.replace(/\s+/g, '').split('/')[0];
    const sourceCode = window.localStorage.getItem("sourceCode")
    const data = {
        problem,
        sourceCode,
        "result" : {
      memory: col[4].textContent.trim(),
      time: col[5].textContent.trim(),
      "language" : language,
      codeLength: col[7].textContent.trim(),
        }
    };
    // problem: 문제 정보.
    // sourceCode: 소스코드.
    // result : 유저의 제출결과. 
    console.log(data);
}
});  
}