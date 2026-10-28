import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_report():
    doc = Document()

    # Define color palette
    COLOR_PRIMARY = RGBColor(27, 54, 93)     # Navy #1B365D
    COLOR_SECONDARY = RGBColor(0, 122, 204)  # Blue #007ACC
    COLOR_SUCCESS = RGBColor(40, 167, 69)    # Green #28A745
    COLOR_DARK = RGBColor(33, 37, 41)        # #212529
    COLOR_MUTED = RGBColor(108, 117, 125)    # Gray #6C757D

    HEX_PRIMARY = "1B365D"
    HEX_LIGHT_BG = "F4F6F9"
    HEX_BORDER = "D1D5DB"
    HEX_SUCCESS_BG = "E8F5E9"
    HEX_SUCCESS_TXT = "1E7E34"

    # Set margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    def set_cell_background(cell, hex_color):
        shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        cell._tc.get_or_add_tcPr().append(shading_elm)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
        tblPr = table._tbl.tblPr
        tblBorders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(tblBorders)

    # ==================== HEADER / COVER BLOCK ====================
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_table.cell(0, 0)
    set_cell_background(cell, "1B365D")
    set_cell_margins(cell, top=260, bottom=260, left=260, right=260)
    cell.width = Inches(6.9)

    p_badge = cell.paragraphs[0]
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_badge = p_badge.add_run("ESPRIT  |  MODULE SPRING BOOT & SPRING DATA JPA")
    run_badge.font.name = "Arial"
    run_badge.font.size = Pt(10)
    run_badge.font.bold = True
    run_badge.font.color.rgb = RGBColor(220, 230, 245)

    p_title = cell.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("Rapport de Validation des Endpoints REST")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(255, 255, 255)

    p_sub = cell.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    run_sub = p_sub.add_run("Tests Postman & Validation Statut 200 OK — VehiculeController")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(13)
    run_sub.font.color.rgb = RGBColor(176, 212, 255)

    p_meta = cell.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_meta = p_meta.add_run("Projet : AutoLoc (Gestion de Location de Véhicules)  •  Port Serveur : 8081  •  Résultat : 5/5 Validés (200 OK)")
    run_meta.font.name = "Arial"
    run_meta.font.size = Pt(9.5)
    run_meta.font.italic = True
    run_meta.font.color.rgb = RGBColor(200, 215, 235)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ==================== SECTION 1: CONTEXTE ====================
    h1 = doc.add_heading(level=1)
    run_h1 = h1.add_run("1. Contexte & Architecture du Contrôleur")
    run_h1.font.name = "Arial"
    run_h1.font.size = Pt(14)
    run_h1.font.bold = True
    run_h1.font.color.rgb = COLOR_PRIMARY
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(4)

    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.line_spacing = 1.15
    p_desc.paragraph_format.space_after = Pt(6)
    r1 = p_desc.add_run("Dans le cadre du projet ")
    r1.font.name = "Calibri"
    r2 = p_desc.add_run("AutoLoc")
    r2.font.bold = True
    r3 = p_desc.add_run(", nous avons mis en place une architecture logicielle 3-tiers conforme aux standards Spring Boot. Le contrôleur REST ")
    r4 = p_desc.add_run("VehiculeController")
    r4.font.bold = True
    r4.font.color.rgb = COLOR_SECONDARY
    r5 = p_desc.add_run(" expose l'ensemble des opérations CRUD nécessaires à la gestion des véhicules. Ce document présente les preuves d'exécution et les captures d'écran des tests réalisés via Postman, confirmant le bon fonctionnement et le retour systématique du statut ")
    r6 = p_desc.add_run("HTTP 200 OK")
    r6.font.bold = True
    r6.font.color.rgb = COLOR_SUCCESS
    r7 = p_desc.add_run(".")

    # Info Callout Box
    arch_table = doc.add_table(rows=1, cols=1)
    arch_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_arch = arch_table.cell(0, 0)
    set_cell_background(c_arch, HEX_LIGHT_BG)
    set_cell_margins(c_arch, top=120, bottom=120, left=150, right=150)
    c_arch.width = Inches(6.9)
    p_arch = c_arch.paragraphs[0]
    p_arch.paragraph_format.space_before = Pt(0)
    p_arch.paragraph_format.space_after = Pt(0)
    r_arch = p_arch.add_run("Composants Clés de la Chaîne Applicative :\n")
    r_arch.font.name = "Arial"
    r_arch.font.bold = True
    r_arch.font.size = Pt(10)
    r_arch.font.color.rgb = COLOR_PRIMARY
    r_arch_body = p_arch.add_run(
        "• Contrôleur REST : tn.esprit.autolocapi.controller.VehiculeController (Préfixe : /vehicules)\n"
        "• Couche Service : IVehiculeService (Interface) & VehiculeServiceImp (Implémentation métier)\n"
        "• Couche Données : VehiculeRepository (Spring Data JPA JpaRepository)\n"
        "• Modèle de Données : Entité JPA Vehicule avec énumérations CategorieVehicule et StatutVehicule"
    )
    r_arch_body.font.name = "Calibri"
    r_arch_body.font.size = Pt(9.5)
    r_arch_body.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ==================== SECTION 2: TABLEAU RECAPITULATIF ====================
    h2 = doc.add_heading(level=1)
    run_h2 = h2.add_run("2. Tableau Récapitulatif des Endpoints et Résultats")
    run_h2.font.name = "Arial"
    run_h2.font.size = Pt(14)
    run_h2.font.bold = True
    run_h2.font.color.rgb = COLOR_PRIMARY
    h2.paragraph_format.space_before = Pt(12)
    h2.paragraph_format.space_after = Pt(6)

    summary_table = doc.add_table(rows=6, cols=5)
    summary_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(summary_table, color="D1D5DB", sz="4")

    headers = ["N°", "Méthode", "Endpoint URL", "Description Métier", "Statut Obtenu"]
    widths = [Inches(0.5), Inches(1.1), Inches(2.2), Inches(2.0), Inches(1.1)]

    # Header Row
    for i, title in enumerate(headers):
        cell = summary_table.cell(0, i)
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        cell.width = widths[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 1, 4] else WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(title)
        run.font.name = "Arial"
        run.font.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ("1", "POST", "/vehicules/ajouter", "Création et persistance d'un nouveau véhicule", "200 OK"),
        ("2", "GET", "/vehicules/{id}", "Recherche d'un véhicule spécifique par son identifiant", "200 OK"),
        ("3", "PUT", "/vehicules/modifier", "Mise à jour des informations d'un véhicule existant", "200 OK"),
        ("4", "DELETE", "/vehicules/supprimer/{id}", "Suppression d'un véhicule par ID & retour de l'objet", "200 OK"),
        ("5", "GET", "/vehicules/all", "Consultation de la liste complète des véhicules", "200 OK")
    ]

    for row_idx, row_data in enumerate(data, start=1):
        bg = "FFFFFF" if row_idx % 2 == 1 else "F8F9FA"
        for col_idx, text in enumerate(row_data):
            cell = summary_table.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=90, bottom=90, left=80, right=80)
            cell.width = widths[col_idx]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 1, 4] else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = "Calibri"
            run.font.size = Pt(9.5)
            if col_idx == 1:
                run.font.bold = True
                if text == "GET":
                    run.font.color.rgb = RGBColor(12, 187, 82)
                elif text == "POST":
                    run.font.color.rgb = RGBColor(255, 108, 55)
                elif text == "PUT":
                    run.font.color.rgb = RGBColor(9, 123, 237)
                elif text == "DELETE":
                    run.font.color.rgb = RGBColor(235, 32, 19)
            elif col_idx == 2:
                run.font.name = "Consolas"
                run.font.size = Pt(8.5)
                run.font.bold = True
            elif col_idx == 4:
                run.font.bold = True
                run.font.color.rgb = COLOR_SUCCESS

    doc.add_page_break()

    # ==================== SECTION 3: DETAIL DES TESTS ====================
    h3_main = doc.add_heading(level=1)
    run_h3_main = h3_main.add_run("3. Détail des Tests Postman & Captures d'Écran")
    run_h3_main.font.name = "Arial"
    run_h3_main.font.size = Pt(14)
    run_h3_main.font.bold = True
    run_h3_main.font.color.rgb = COLOR_PRIMARY
    h3_main.paragraph_format.space_before = Pt(6)
    h3_main.paragraph_format.space_after = Pt(10)

    tests = [
        {
            "num": "Test 1",
            "title": "Ajout d'un Nouveau Véhicule",
            "method": "POST",
            "method_color": RGBColor(255, 108, 55),
            "url": "http://localhost:8081/vehicules/ajouter",
            "desc": "Cet endpoint permet la création d'un véhicule en base de données. Le corps de la requête contient les attributs du véhicule (immatriculation, marque, modèle, catégorie, tarif journalier, statut). Le serveur génère automatiquement la clé primaire idVehicule et retourne l'objet persisté.",
            "req_body": '{\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 120.00,\n  "statut": "DISPONIBLE"\n}',
            "resp_body": '{\n  "idVehicule": 4,\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 120.0,\n  "statut": "DISPONIBLE"\n}',
            "status": "200 OK",
            "image": r"C:\Users\lenovo\.gemini\antigravity-ide\brain\c2171398-c0ee-4385-b636-641646420628\.user_uploaded\media_1792238515384.png"
        },
        {
            "num": "Test 2",
            "title": "Consultation d'un Véhicule par ID",
            "method": "GET",
            "method_color": RGBColor(12, 187, 82),
            "url": "http://localhost:8081/vehicules/4",
            "desc": "Cet endpoint recherche et retourne les détails d'un véhicule à partir de son identifiant numérique unique (idVehicule).",
            "req_body": None,
            "resp_body": '{\n  "idVehicule": 4,\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 140.0,\n  "statut": "LOUE"\n}',
            "status": "200 OK (35 ms, 306 B)",
            "image": r"C:\Users\lenovo\.gemini\antigravity-ide\brain\c2171398-c0ee-4385-b636-641646420628\.user_uploaded\media_1792238703028.png"
        },
        {
            "num": "Test 3",
            "title": "Modification d'un Véhicule Existant",
            "method": "PUT",
            "method_color": RGBColor(9, 123, 237),
            "url": "http://localhost:8081/vehicules/modifier",
            "desc": "Cet endpoint permet de mettre à jour un enregistrement existant. Ici, le tarif journalier du véhicule ID 4 passe de 120.00 à 140.00 et son statut passe de DISPONIBLE à LOUE.",
            "req_body": '{\n  "idVehicule": 4,\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 140.00,\n  "statut": "LOUE"\n}',
            "resp_body": '{\n  "idVehicule": 4,\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 140.0,\n  "statut": "LOUE"\n}',
            "status": "200 OK (19 ms, 306 B)",
            "image": r"C:\Users\lenovo\.gemini\antigravity-ide\brain\c2171398-c0ee-4385-b636-641646420628\.user_uploaded\media_1792238705181.png"
        },
        {
            "num": "Test 4",
            "title": "Suppression d'un Véhicule par ID",
            "method": "DELETE",
            "method_color": RGBColor(235, 32, 19),
            "url": "http://localhost:8081/vehicules/supprimer/4",
            "desc": "Cet endpoint supprime le véhicule portant l'ID 4 de la base de données relationnelle et retourne l'entité supprimée en confirmation.",
            "req_body": None,
            "resp_body": '{\n  "idVehicule": 4,\n  "immatriculation": "240-TUNIS-1234",\n  "marque": "Peugeot",\n  "modele": "208",\n  "categorie": "CITADINE",\n  "tarifJournalier": 140.0,\n  "statut": "LOUE"\n}',
            "status": "200 OK (18 ms, 306 B)",
            "image": r"C:\Users\lenovo\.gemini\antigravity-ide\brain\c2171398-c0ee-4385-b636-641646420628\.user_uploaded\media_1792238765377.png"
        },
        {
            "num": "Test 5",
            "title": "Récupération de la Liste Complète des Véhicules",
            "method": "GET",
            "method_color": RGBColor(12, 187, 82),
            "url": "http://localhost:8081/vehicules/all",
            "desc": "Cet endpoint interroge la table vehicule via vehiculeRepository.findAll() et retourne un tableau JSON de tous les véhicules enregistrés.",
            "req_body": None,
            "resp_body": '[\n  {\n    "idVehicule": 1,\n    "immatriculation": "240-TUNIS-1234",\n    "marque": "Peugeot",\n    "modele": "208",\n    "categorie": "CITADINE",\n    "tarifJournalier": 120.0,\n    "statut": "DISPONIBLE"\n  }\n]',
            "status": "200 OK (10 ms, 314 B)",
            "image": r"C:\Users\lenovo\.gemini\antigravity-ide\brain\c2171398-c0ee-4385-b636-641646420628\.user_uploaded\media_1792238766732.png"
        }
    ]

    for t in tests:
        # Heading 2
        h_t = doc.add_heading(level=2)
        h_t.paragraph_format.space_before = Pt(14)
        h_t.paragraph_format.space_after = Pt(4)
        
        r_num = h_t.add_run(f"3.{t['num'].split()[-1]}. {t['title']} — ")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(12)
        r_num.font.bold = True
        r_num.font.color.rgb = COLOR_PRIMARY

        r_m = h_t.add_run(f"[{t['method']}]")
        r_m.font.name = "Arial"
        r_m.font.size = Pt(12)
        r_m.font.bold = True
        r_m.font.color.rgb = t["method_color"]

        # Detail block
        d_table = doc.add_table(rows=1, cols=1)
        d_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        d_cell = d_table.cell(0, 0)
        set_cell_background(d_cell, "F8F9FA")
        set_cell_margins(d_cell, top=100, bottom=100, left=120, right=120)
        d_cell.width = Inches(6.9)

        p_info = d_cell.paragraphs[0]
        p_info.paragraph_format.space_before = Pt(0)
        p_info.paragraph_format.space_after = Pt(2)
        
        r_u_lbl = p_info.add_run("URL : ")
        r_u_lbl.font.bold = True
        r_u_lbl.font.size = Pt(9.5)
        r_u_val = p_info.add_run(t['url'] + "  |  ")
        r_u_val.font.name = "Consolas"
        r_u_val.font.size = Pt(9)
        
        r_s_lbl = p_info.add_run("Statut HTTP : ")
        r_s_lbl.font.bold = True
        r_s_lbl.font.size = Pt(9.5)
        r_s_val = p_info.add_run(t['status'] + "\n")
        r_s_val.font.bold = True
        r_s_val.font.size = Pt(9.5)
        r_s_val.font.color.rgb = COLOR_SUCCESS

        r_desc = p_info.add_run(t['desc'])
        r_desc.font.name = "Calibri"
        r_desc.font.size = Pt(9.5)
        r_desc.font.color.rgb = COLOR_DARK

        # Embed Image
        if os.path.exists(t["image"]):
            p_img = doc.add_paragraph()
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(2)
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_img = p_img.add_run()
            run_img.add_picture(t["image"], width=Inches(6.8))

            p_caption = doc.add_paragraph()
            p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_caption.paragraph_format.space_before = Pt(1)
            p_caption.paragraph_format.space_after = Pt(12)
            r_cap = p_caption.add_run(f"Figure {t['num'].split()[-1]} : Capture Postman — {t['method']} {t['url']} (Status: 200 OK)")
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(8.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = COLOR_MUTED

    # ==================== SECTION 4: CONCLUSION ====================
    h4 = doc.add_heading(level=1)
    run_h4 = h4.add_run("4. Conclusion & Conformité Technique")
    run_h4.font.name = "Arial"
    run_h4.font.size = Pt(14)
    run_h4.font.bold = True
    run_h4.font.color.rgb = COLOR_PRIMARY
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(6)

    p_concl = doc.add_paragraph()
    p_concl.paragraph_format.line_spacing = 1.15
    p_concl.paragraph_format.space_after = Pt(8)
    r_c1 = p_concl.add_run(
        "Les tests réalisés avec l'outil Postman confirment le parfait fonctionnement de la couche REST "
        "de l'application AutoLoc. Les 5 endpoints implémentés dans "
    )
    r_c1.font.name = "Calibri"
    r_c2 = p_concl.add_run("VehiculeController")
    r_c2.font.bold = True
    r_c3 = p_concl.add_run(" répondent fidèlement aux exigences fonctionnelles du cahier des charges :\n")
    r_c3.font.name = "Calibri"

    bullets = [
        "Persistance et auto-incrémentation de l'identifiant primaire lors de l'ajout (POST).",
        "Extraction ciblée et gestion unitaire des données par identifiant (GET /{id}).",
        "Mise à jour transactionnelle des champs de tarification et de disponibilité (PUT /modifier).",
        "Suppression cohérente de l'enregistrement en base tout en renvoyant l'état final (DELETE /supprimer/{id}).",
        "Sérialisation JSON exhaustive de l'ensemble de la flotte de véhicules (GET /all)."
    ]
    for b in bullets:
        p_b = doc.add_paragraph(style='List Bullet')
        p_b.paragraph_format.space_before = Pt(0)
        p_b.paragraph_format.space_after = Pt(2)
        r_b = p_b.add_run(b)
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9.5)

    # Final Success Badge
    concl_table = doc.add_table(rows=1, cols=1)
    concl_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_concl = concl_table.cell(0, 0)
    set_cell_background(c_concl, HEX_SUCCESS_BG)
    set_cell_margins(c_concl, top=100, bottom=100, left=150, right=150)
    c_concl.width = Inches(6.9)
    p_badge_final = c_concl.paragraphs[0]
    p_badge_final.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_bf = p_badge_final.add_run("✓ Statut Global des Tests : 100% Succès (5/5 endpoints validés avec HTTP Status 200 OK)")
    r_bf.font.name = "Arial"
    r_bf.font.bold = True
    r_bf.font.size = Pt(10)
    r_bf.font.color.rgb = RGBColor(30, 126, 52)

    # Save Document
    output_path = r"c:\Users\lenovo\Documents\AutoLoc-repo\Test_Endpoints_VehiculeController.docx"
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    create_report()
