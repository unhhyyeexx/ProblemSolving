-- 코드를 입력하세요
SELECT b.rest_id, b.rest_name, b.food_type, b.favorites, b.address, round(avg(a.review_score), 2) as score
from rest_review a
join rest_info b on a.rest_id = b.rest_id
group by a.rest_id
having b.address like '서울%'
order by score desc, b.favorites desc