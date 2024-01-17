// 문제 번호
const problemNumber = document.querySelector("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > ul > li.active > a").textContent;
const len = document.querySelector("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > ul > li.active > a").textContent.length
const problemNum = problemNumber.substring(0, len-1);

// 시간 제한, 메모리 제한
const limits = document.querySelector("#problem-info > tbody > tr");
const child = limits.children
const timeLimits = child[0].textContent
const memoryLimits = child[1].textContent

// 문제 설명
const problemDescription = document.querySelector("#problem_description > p").textContent;

// 입력, 출력
const input = document.querySelector("#problem_input > p").textContent;
const output = document.querySelector("#problem_output > p").textContent;

// 예제 입력 (여러 개)
const sampleInputs = [];
let sampleInputIndex = 1;

while (true) {
  const sampleInputElement = document.querySelector(`#sample-input-${sampleInputIndex}`);
  if (!sampleInputElement) break; // 해당 번호의 예제 입력이 없으면 종료

  sampleInputs.push(sampleInputElement.textContent.trim());
  sampleInputIndex++;
}

// 예제 출력 (여러 개)
const sampleOutputs = [];
let sampleOutputIndex = 1;

while (true) {
  const sampleOutputElement = document.querySelector(`#sample-output-${sampleOutputIndex}`);
  if (!sampleOutputElement) break; // 해당 번호의 예제 출력이 없으면 종료

  sampleOutputs.push(sampleOutputElement.textContent.trim());
  sampleOutputIndex++;
}

// 문제 분류
const categories = []
let arr = document.querySelectorAll("#problem_tags > div.spoiler > ul > li > a ");
if(arr.length==0){
    arr = document.querySelectorAll("#problem_tags > ul > li > a")
}
// console.log(arr)
arr.forEach(ele => {
    categories.push(ele.innerHTML)
});
const problemData = {
    "problemNum" : problemNum,
    "timeLimits" : timeLimits,
    "memoryLimits" : memoryLimits,
    "problemDescription" : problemDescription,
    "input" : input,
    "output" : output,
    "sampleInputs" : sampleInputs,
    "sampleOutputs" : sampleOutputs,
    "categories" : categories
}

console.log(problemData)
window.localStorage.setItem("flag", 0)
window.localStorage.setItem("problemData", JSON.stringify(problemData))
