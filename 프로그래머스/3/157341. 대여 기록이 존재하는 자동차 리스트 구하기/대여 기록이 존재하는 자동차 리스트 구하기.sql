-- 코드를 입력하세요
SELECT DISTINCT(A.CAR_ID)
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
JOIN CAR_RENTAL_COMPANY_CAR B
ON A.CAR_ID = B.CAR_ID
WHERE B.CAR_TYPE = '세단'
AND A.START_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY A.CAR_ID DESC