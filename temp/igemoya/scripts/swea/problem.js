console.log("entered!")
// 문제 번호, 제목
const problem = document.querySelector("#problem_right > div.problem_box > h3").textContent.split(". ");
const problemNum = problem[0]
const problemTitle = problem[1]

// 문제 조건
// 시간, 메모리
const Time = document.querySelectorAll("#collapseOne > div > div.box3 > ul > li:nth-child(1) > span")[1].innerHTML;
const Memory = document.querySelectorAll("#collapseOne > div > div.box3 > ul > li:nth-child(2) > span")[1].innerHTML;


// 문제 내용- 본문, 입력, 출력
const problemContent = document.querySelector("#collapseOne > div > div.box4 > p").innerHTML.split("<strong>[입력]</strong>")
const content = problemContent[0].replaceAll("<br>", " ").trim().replace("<strong>※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.</strong>", "")
const input = problemContent[1].split("<strong>[출력]</strong>")[0].replaceAll("<br>", " ")
const output = problemContent[1].split("<strong>[출력]</strong>")[1].replaceAll("<br>", " ").trim()

// 입력

document.querySelector("#collapseOne > div > div.box_type1 > div.left > div > table > tbody > tr > td:nth-child(1)")