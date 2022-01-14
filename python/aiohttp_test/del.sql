SELECT happ.user_id, MAX(hcon.valid_from)
FROM hpcdata.application happ
JOIN hpcdata.consent hcon ON happ.user_id = hcon.user_id
-- WHERE hcon.valid_from in (SELECT MAX(valid_from) FROM hcon where happ.user_id = hcon.user_id ???)