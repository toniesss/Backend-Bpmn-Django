SELECT nextval('form_header_form_id_seq');
 
--ALTER SEQUENCE draft_form_header_form_id_seq RESTART WITH 9;
--# Form Test
TRUNCATE "form_header";
INSERT INTO "public"."form_header"
  (form_id, form_name, form_key, description, status, discipline_id, inspection_level_id, create_by, create_date, update_by, update_date)
VALUES
  ('1', 'Fit up & dimension inspection', 'fit_up_&_dimension_inspection', '', 'Active', '1', '1', 'dev', default, 'dev', default),
  ('2', 'Welding inspection', 'welding_inspection', '', 'Active', '1', '1', 'dev', default, 'dev', default),
ALTER SEQUENCE form_header_form_id_seq RESTART WITH 15;
  
TRUNCATE "form_detail";
INSERT INTO "public"."form_detail"
  (form_detail_id, form_id, field_type_id, sequence_no, create_by, create_date, update_by, update_date)
VALUES
  ('1', '1', '4', '0', 'dev', default, 'dev', default),
  ('2', '1', '1', '1', 'dev', default, 'dev', default),
ALTER SEQUENCE form_detail_form_detail_id_seq RESTART WITH 62;

TRUNCATE "form_properties";
INSERT INTO "public"."form_properties"
  (form_properties_id, form_detail_id, properties_id, properties_value, create_by, create_date, update_by, update_date)
VALUES
  ('1', '1', '1', 'Title 1', 'dev', default, 'dev', default),
  ('2', '1', '2', 'default title 1', 'dev', default, 'dev', default),
  ('3', '1', '7', '', 'dev', default, 'dev', default),
ALTER SEQUENCE form_properties_form_properties_id_seq RESTART WITH 392;


TRUNCATE "form_properties_list";
INSERT INTO "public"."form_properties_list"
  (list_id, form_properties_id, list_sequence, list_key, list_value, create_by, create_date, update_by, update_date)
VALUES
  ('2', '34', '1', 'multipel_2', 'Multipel 2', 'dev', default, 'dev', default),
ALTER SEQUENCE form_properties_list_list_id_seq RESTART WITH 10;


---Draft
--# Form Test
TRUNCATE "draft_form_header";
INSERT INTO "public"."draft_form_header"
  (form_id, form_name, form_key, description, status, discipline_id, inspection_level_id, create_by, create_date, update_by, update_date)
VALUES
  ('1', 'Fit up & dimension inspection', 'fit_up_&_dimension_inspection', '', 'Active', '1', '1', 'dev', default, 'dev', default),
  ('2', 'Welding inspection', 'welding_inspection', '', 'Active', '1', '1', 'dev', default, 'dev', default),
ALTER SEQUENCE draft_form_detail_form_detail_id_seq RESTART WITH 62; 
 
TRUNCATE "draft_form_properties";
INSERT INTO "public"."draft_form_properties"
  (form_properties_id, form_detail_id, properties_id, properties_value, create_by, create_date, update_by, update_date)
VALUES
  ('1', '1', '1', 'Title 1', 'dev', default, 'dev', default),
  ('2', '1', '2', 'default title 1', 'dev', default, 'dev', default),

ALTER SEQUENCE draft_form_properties_form_properties_id_seq RESTART WITH 392; 

TRUNCATE "draft_form_properties_list";
INSERT INTO "public"."draft_form_properties_list"
  (list_id, form_properties_id, list_sequence, list_key, list_value, create_by, create_date, update_by, update_date)
VALUES
  ('2', '34', '1', 'multipel_2', 'Multipel 2', 'dev', default, 'dev', default),
 ALTER SEQUENCE draft_form_properties_list_list_id_seq RESTART WITH 10; 
 
 