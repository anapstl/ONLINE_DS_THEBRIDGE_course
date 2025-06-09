SELECT *
from crime_scene_report
where type='murder' and date='20180115'

-- Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". 
-- The second witness, named Annabel, lives somewhere on "Franklin Ave".

-- 1. 
-- 14887	Morty Schapiro	118009	4919	Northwestern Dr	111564949

--2.
--16371	Annabel Miller	490173	103	Franklin Ave	318771143

SELECT * FROM interview
where person_id in (14887, 16371)

-- 14887 Morty	"I heard a gunshot and then saw a man run out. He had a ""Get Fit Now Gym"" bag. 
        -- The membership number on the bag started with ""48Z"". Only gold members have those bags. 
        -- The man got into a car with a plate that included ""H42W""."

            SELECT * FROM get_fit_now_member
            where id like '48Z%' and membership_status = 'gold'

            -- 48Z7A	28819	Joe Germuska	20160305	gold
            -- 48Z55	67318	Jeremy Bowers	20160101	gold

            select *
            from drivers_license
            where plate_number like '%H42W%'

            -- "183779"	"21"	"65"	"blue"	"blonde"	"female"	"H42W0X"	"Toyota"	"Prius"
            -- "423327"	"30"	"70"	"brown"	"brown"	"male"	"0H42W2"	"Chevrolet"	"Spark LS"
            -- "664760"	"21"	"71"	"black"	"black"	"male"	"4H42WR"	"Nissan"	"Altima"
						
            SELECT drivers_license.id, person.name
            FROM drivers_license
            join person on person.license_id = drivers_license.id
            where person.license_id in (423327, 664760)

            -- "423327"	"Jeremy Bowers" < ----------------------------------- Guilty
            -- "664760"	"Tushar Chandra"


            -- segun Annabel, lo vio en el gym ¿lo estuvo?
            SELECT * 
            FROM get_fit_now_check_in
            WHERE membership_id = '48Z55';

            -- 48Z55	20180109	1530	1700

-- 16371 Annabel "I saw the murder happen, and I recognized the killer from my gym when I was working 
        -- out last week on January the 9th.

            select *
            from get_fit_now_member
            where person_id= '16371'

            -- 90081	16371	Annabel Miller	20160208	gold

            select *
            from get_fit_now_check_in
            where membership_id= '90081'

            -- 90081	20180109	1600	1700   la hora de Annabel en el gym


            select *
            from get_fit_now_check_in
            where check_in_time between '1600' and '1700' 

            -- "48Z7A"	"20180109"	"1600"	"1730"
            -- "48Z55"	"20180109"	"1530"	"1700"
            -- "90081"	"20180109"	"1600"	"1700"

            select person_id, name
            from get_fit_now_member
            WHERE id = '48Z7A'
                -- "67318"	"Jeremy Bowers"
                -- "28819"	"Joe Germuska"

            SELECT person.name, plate_number FROM drivers_license
            join person on drivers_license.id = person.license_id
            where person.id in (67318, 28819)

            -- Jeremy Bowers	0H42W2  <------------- Guilty


-- ¿pero qué pasó?

            SELECT * 
            FROM person
            WHERE name = 'Jeremy Bowers';
            -- 67318	Jeremy Bowers	423327	530	Washington Pl, Apt 3A	871539279


            SELECT * FROM interview
            where person_id=67318

            -- "67318"	"I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5"" (65"") or 5'7"" (67""). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.


            SELECT drivers_license.id, person.name FROM drivers_license
            join person on person.license_id = drivers_license.id

            where car_make like 'Tesla%' and car_model='Model S' and hair_color='red' and (height between 65 and 67)

            -- "918773"	"Red Korb"
            -- "291182"	"Regina George"
            -- "202298"	"Miranda Priestly"

            SELECT drivers_license.id, person.name, facebook_event_checkin.date
            FROM drivers_license
            JOIN person ON person.license_id = drivers_license.id
            JOIN facebook_event_checkin ON person.id = facebook_event_checkin.person_id
            WHERE car_make LIKE 'Tesla%' 
            AND car_model = 'Model S' 
            AND hair_color = 'red' 
            AND height BETWEEN 65 AND 67 
            AND facebook_event_checkin.event_name = 'SQL Symphony Concert'

            -- "202298"	"Miranda Priestly"	"20171206"
            -- "202298"	"Miranda Priestly"	"20171212"
            -- "202298"	"Miranda Priestly"	"20171229"

            SELECT drivers_license.id, person.name, COUNT(facebook_event_checkin.date) AS event_count
            FROM drivers_license
            JOIN person ON person.license_id = drivers_license.id
            JOIN facebook_event_checkin ON person.id = facebook_event_checkin.person_id
            WHERE car_make LIKE 'Tesla%' 
            AND car_model = 'Model S' 
            AND hair_color = 'red' 
            AND height BETWEEN 65 AND 67 
            AND facebook_event_checkin.event_name = 'SQL Symphony Concert'
            GROUP BY drivers_license.id, person.name;

            -- 202298	Miranda Priestly	3




"

        

