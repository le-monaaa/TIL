const tr = document.querySelector("#status-table > tbody > tr");

function isStatusWaiting() {
  let resultProcess = document.querySelector(
    "#status-table > tbody > tr :nth-child(4) > span"
    ).textContent;
    console.log(resultProcess)
  return (
      resultProcess === "기다리는 중" ||
      resultProcess === "채점 준비 중" ||
      resultProcess.substring(0, 4) === "채점 중"
      );
    }
    if(isStatusWaiting){
      // 초기 상태가 채점 중일 때만 실행.
      console.log("solved entered, ", resultProcess)
      async function waitForStatusChange() {
        while (isStatusWaiting()) {
          // 1초마다 다시 체크
          let result = document.querySelector(
            "#status-table > tbody > tr :nth-child(4) > span"
            ).textContent;
          await new Promise((resolve) => setTimeout(resolve, 1000));
        }
      }
      // 변경되면,
      waitForStatusChange().then(() => {
        if (
          result === "맞았습니다!!"
          ) {
      console.log("맞았습니다", result)
      const col = tr.children;
      const jsonproblem = window.localStorage.getItem("problemData");
      const problem = JSON.parse(jsonproblem);
      const language = col[6].textContent.replace(/\s+/g, "").split("/")[0];
      const sourceCode = window.localStorage.getItem("sourceCode");
      const data = {
        problem,
        sourceCode,
        result: {
          memory: col[4].textContent.trim(),
          time: col[5].textContent.trim(),
          language: language,
          codeLength: col[7].textContent.trim(),
        },
      };
      // problem: 문제 정보.
      // sourceCode: 소스코드.
      // result : 유저의 제출결과.
      console.log(data.sourceCode);
      console.log(data);
    }
    else if(
      result === "틀렸습니다"
    ){
      console.log(result)
    }
  });

}
