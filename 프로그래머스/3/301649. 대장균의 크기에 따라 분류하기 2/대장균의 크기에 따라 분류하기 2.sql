-- 코드를 작성해주세요
SELECT ED.ID, CASE WHEN ED.R <= 0.25 THEN "LOW"
WHEN ED.R <= 0.5 THEN "MEDIUM"
WHEN ED.R <= 0.75 THEN "HIGH"
ELSE "CRITICAL"
END AS COLONY_NAME
FROM (SELECT ID, PERCENT_RANK() 
      OVER (ORDER BY SIZE_OF_COLONY) AS R 
     FROM ECOLI_DATA) AS ED
ORDER BY ID