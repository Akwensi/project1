
SHOW search_path;

SET search_path TO stackoverflow_filtered;

SELECT * FROM results;

--Create a btree index on the reputation column within the results table
create index reputation_idx on results using btree(reputation desc, nulls, last);

--Create a hash index on the display_name column within the results table.
create index display_name_idx on results using hash(display_name) desc, nulls, last);

--From the results table, create a view with the column names display_name, city, questions_id where the accepted_answer_id is not null.
CREATE VIEW results_view as SELECT display_name, city, questions_id, 
where accepted_answer_id is not null
FROM results;

--Create a materialized view with column names display_name, city, questions_id where the accepted_answer_id is not null.
CREATE MATERIALIZED VIEW results_materialized_view as select display_name, city, questions_id, where accepted_answer_id is not null
FROM results;

--How many cities appeared more than twice in your results table?
SELECT city, count(*)
FROM results
GROUP BY city
HAVING count(*)>2
ORDER BY count(*) desc;

--How many unique created_at dates(not datetime) are in the result table?
SELECT created_at, count(*), array_agg(DISTINCT (extract(date_part FROM created_at)))
FROM results
GROUP BY count(*)
ORDER BY count(*) desc;


--If you were to give an award to one user, who will it be? And why?
--the User with the highest accepted_answer_id 
select users_id, display_name, accepted_answer_id, score, answers_score
from results
where answers_score is max;