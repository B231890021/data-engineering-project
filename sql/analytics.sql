-- ── 1. NULL УТГУУД ШАЛГАХ ──
SELECT 
    COUNT(*) FILTER (WHERE ner IS NULL)           AS ner_null,
    COUNT(*) FILTER (WHERE ovog IS NULL)          AS ovog_null,
    COUNT(*) FILTER (WHERE email IS NULL)         AS email_null,
    COUNT(*) FILTER (WHERE heltes IS NULL)        AS heltes_null,
    COUNT(*) FILTER (WHERE alban_tushaal IS NULL) AS alban_tushaal_null,
    COUNT(*) FILTER (WHERE tuluv IS NULL)         AS tuluv_null
FROM huviin_medeelel;

-- ── 2. ДАВХАРДСАН МӨРҮҮД ШАЛГАХ ──
SELECT COUNT(*) - COUNT(DISTINCT employee_id) AS davhardsan_too
FROM huviin_medeelel;

-- ── 3. VIEW 1: Хэлтэс тус бүрийн дундаж цалин ──
CREATE OR REPLACE VIEW v_heltes_tsalin AS
SELECT
    h.heltes,
    COUNT(*)                        AS ajiltny_too,
    ROUND(AVG(a.undsen_tsalin))     AS dundaj_undsen_tsalin,
    ROUND(AVG(a.niit_tsalin))       AS dundaj_niit_tsalin,
    ROUND(AVG(a.gart_avah_tsalin))  AS dundaj_gart_avah_tsalin,
    ROUND(SUM(a.niit_tsalin))       AS niit_tsalin_dun
FROM huviin_medeelel h
JOIN ajliin_medeelel a ON h.employee_id = a.employee_id
GROUP BY h.heltes
ORDER BY dundaj_niit_tsalin DESC;

-- ── 4. VIEW 2: Үнэлгээгээр ажилтны тоо ба дундаж bonus ──
CREATE OR REPLACE VIEW v_unelgee_bonus AS
SELECT
    guitsetgeliiin_unelgee          AS unelgee,
    COUNT(*)                        AS ajiltny_too,
    ROUND(AVG(bonus))               AS dundaj_bonus,
    ROUND(AVG(niit_tsalin))         AS dundaj_niit_tsalin
FROM ajliin_medeelel
GROUP BY guitsetgeliiin_unelgee
ORDER BY unelgee;

-- ── 5. VIEW 3: Илүү цаг хамгийн их ажилласан top 10 ──
CREATE OR REPLACE VIEW v_top_iluu_tsag AS
SELECT
    h.employee_id,
    h.ner,
    h.ovog,
    h.heltes,
    h.alban_tushaal,
    a.iluu_tsag,
    a.iluu_tsagiin_tuluv,
    a.niit_tsalin
FROM huviin_medeelel h
JOIN ajliin_medeelel a ON h.employee_id = a.employee_id
ORDER BY a.iluu_tsag DESC
LIMIT 10;

-- ── 6. VIEW 4: Хэлтэс тус бүрийн боловсролын түвшин ──
CREATE OR REPLACE VIEW v_bolovsrol_heltes AS
SELECT
    heltes,
    bolovsrol,
    COUNT(*) AS ajiltny_too
FROM huviin_medeelel
GROUP BY heltes, bolovsrol
ORDER BY heltes, ajiltny_too DESC;