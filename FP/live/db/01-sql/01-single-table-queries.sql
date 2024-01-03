-- 01. Querying data
SELECT LastName
FROM employees;

SELECT LastName, FirstName
From employees;

SELECT *
FROM employees;

SELECT FirstName as 이름
FROM employees;

SELECT Name, Milliseconds/60000 as "재생시간(분)"FROM tracks;
-- 02. Sorting data
SELECT FirstName
FROM employees
ORDER BY FirstName;

SELECT FirstName
FROM employees
ORDER BY FirstName ASC;

SELECT FirstName
FROM employees
ORDER BY FirstName DESC;

SELECT Country, City
FROM customers
ORDER BY Country DESC,
City ASC;

SELECT Name, Milliseconds/60000 as "재생시간(분)"
FROM tracks
ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
-- NULL값이 존재할 경우 오름차순(ASC) 정렬 시 결과에 NULL이 먼저 출력
SELECT ReportsTo
FROM employees
ORDER BY ReportsTo;


-- 03. Filtering data
-- DISTINCT : 조회 결과에서 중복된 레코드 제거. SELECT바로 뒤 작성. 하나 이상의 필드 지정
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

-- WHERE : 조회 시 특정 검색 조건을 지정: FROM 뒤에 위치.
-- search_condition은 비교연산자와 논리연산자(AND, OR, NOT)을 사용하는 구문이 사용됨

SELECT LastName, FirstName, City
FROM customers
WHERE City = "Prague";

SELECT LastName, FirstName, City
FROM customers
WHERE City != "Prague";

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NUll
AND Country = "USA";

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NUll
OR Country = "USA";

SELECT Name, Bytes
FROM tracks
Where bytes
BETWEEN 10000 AND 50000;

-- WHERE  Bytes>=10000
-- AND Bytes <= 50000

SELECT Name, Bytes
FROM tracks
Where byte BETWEEN 10000 AND 50000
ORDER BY bytes;

SELECT LastName, FirstName, Country
FROM customers
WHERE Country = "Canada" or Country = "Germany";

SELECT LastName, FirstName, Country
FROM customers
WHERE Country IN ("Canada","Germany", "France");

SELECT LastName, FirstName, Country
FROM customers
WHERE Country NOT IN ("Canada","Germany","France");

SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE "%son";

SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE "___a";

-- wild characters
-- % 0개 이상의 문자열과 일치하는지 확인
-- _ 단일문자와 일치하는지 확인

-- LIMIT clause 조회하는 레코드의 수를 제한
-- SELECT FROM 이후에 등장. 하나 또는 두 개의 인자 사용(0 또는 양의 정수). 조회하는 최대 레코드 수 지정

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 3, 4;

--  04. Grouping data
-- GROUP BY -> FROM, WHERE 절 뒤 배치. 뒤에 그룹화 할 필드 목록 작성

SELECT Country
FROM customers
GROUP BY Country;

SELECT Country, COUNT(*)
FROM customers
GROUP BY Country;

SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
WHERE avgOfMinute < 10
GROUP BY Composer;
--> 집계항목에 대한 조건은 WHERE 절로 x, HAVING 으로.Address
-- 에러


-- 에러 해결
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
GROUP BY Composer
HAVING avgOfMinute < 10;