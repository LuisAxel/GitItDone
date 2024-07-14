select patient_id, patient_name, conditions
from Patients
where regexp_like(conditions, ' DIAB1') or
  regexp_like(conditions, '^DIAB1')
