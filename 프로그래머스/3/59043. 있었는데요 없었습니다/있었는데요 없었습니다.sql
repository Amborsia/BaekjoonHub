-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME FROM ANIMAL_INS I JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID WHERE i.DATETIME > o.DATETIME ORDER BY I.DATETIME

# SELECT o.ANIMAL_ID, o.NAME
# FROM ANIMAL_INS i
# JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
# WHERE i.DATETIME > o.DATETIME
# ORDER BY i.DATETIME;
