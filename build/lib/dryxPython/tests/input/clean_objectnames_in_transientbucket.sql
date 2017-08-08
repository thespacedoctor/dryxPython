CREATE TEMPORARY TABLE tmp AS (SELECT primaryKeyId, masterIDFlag, name, observationMJD, magnitude, filter, concat(name, observationMJD, magnitude, filter) as nameIndex from transientBucket where name like "%-%" and name not like "%:%" order by name);
create TEMPORARY table tmp2 as (select primaryKeyId, masterIDFlag, name, observationMJD, magnitude, filter,concat(replace(name,":","-"), observationMjd, magnitude, filter) as nameIndex from transientBucket where name like "%:%" and masterIDFlag = 0 and dateCreated > DATE_SUB(now(),INTERVAL 14 day));
Create TEMPORARY table tmp3 as (select b.primaryKeyId from transientBucket b, tmp2, tmp where tmp2.nameIndex = tmp.nameIndex and b.primaryKeyId = tmp2.primaryKeyId) ;
delete from transientBucket where primaryKeyId in (select * from tmp3);

update transientBucket set name = replace(name,' ','+') where primaryKeyId in (select primaryKeyId from (SELECT primaryKeyId FROM transientBucket where name REGEXP '[0-9] [0-9]') as x) and primaryKeyId not in (select primaryKeyId from (SELECT primaryKeyId FROM transientBucket where name REGEXP '[a-zA-Z] [a-zA-Z]') as y);
update transientBucket set name = replace(name,' ','') where primaryKeyId not in (select primaryKeyId from (SELECT primaryKeyId FROM transientBucket where name REGEXP '[0-9] [0-9]') as x) and primaryKeyId in (select primaryKeyId from (SELECT primaryKeyId FROM transientBucket where name REGEXP '[a-zA-Z] [a-zA-Z]') as y);
-- select name from transientBucket where name like "%:%";
update transientBucket set name = replace(name,':','-') where name like "%:%";
-- select name from transientBucket where name like "% %";
update transientBucket set name = replace(name,' ','') where name like "% %";
