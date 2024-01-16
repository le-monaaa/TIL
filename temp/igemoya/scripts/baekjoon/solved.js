const tr = document.querySelector('#status-table > tbody > tr');

function isStatusWaiting() {
    const resultProcess = document.querySelector('#status-table > tbody > tr :nth-child(4) > span').textContent
    return (resultProcess === "기다리는 중" 
    || resultProcess === "채점 준비 중" 
    || resultProcess.substring(0,4) === "채점 중" );
}
if (tr) {


async function waitForStatusChange() {
    while (isStatusWaiting()) {
        // 1초마다 다시 체크
        await new Promise(resolve => setTimeout(resolve, 1000)); 
    }
}
// 변경되면,
waitForStatusChange()
.then(() => {

    const columns = tr.children;
    const jsonproblem = window.localStorage.getItem("problemData")
    const problem = JSON.parse(jsonproblem)
    const language = columns[6].textContent.replace(/\s+/g, '').split('/')[0];
    console.log(language)
    const data = {
        problem,
        "result" : {
      memory: columns[4].textContent.trim(),
      time: columns[5].textContent.trim(),
      "language" : language,
      code_length: columns[7].textContent.trim(),
        }
    };
    // problem: 문제 정보.
    // result : 유저의 제출결과. 
    console.log(data);
});
    
}