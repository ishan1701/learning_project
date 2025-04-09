SELECT DeforestationStatus, count(FarmID) as quantity
FROM `{project_id}.{dataset}.{table}`
group by all;
