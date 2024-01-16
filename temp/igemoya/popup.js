  // popup.js

document.addEventListener('DOMContentLoaded', function () {
    // 현재 탭의 페이지에서 tbody 내의 데이터를 출력하는 함수 호출
    getCurrentPageData();
  });
  
  function getCurrentPageData() {
    // 현재 탭의 페이지에서 tbody를 선택
    const tbody = document.querySelector('tbody');
  
    if (tbody) {
      // tbody가 존재하는 경우
      const rows = tbody.querySelectorAll('tr');
  
      // 각 행의 데이터를 출력
      rows.forEach((row, index) => {
        const columns = row.querySelectorAll('td');
        const rowData = Array.from(columns).map((column) => column.textContent.trim());
        console.log(`Row ${index + 1} Data: `, rowData);
      });
    } else {
      console.log('Tbody not found on the page.');
    }
  }