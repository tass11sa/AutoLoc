import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://localhost:8081"

def req(method, path, data=None):
    url = f"{BASE_URL}{path}"
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    headers = {"Content-Type": "application/json"} if data is not None else {}
    r = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            content = resp.read().decode("utf-8")
            return resp.status, json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        return e.code, err_body
    except Exception as e:
        return 500, str(e)

def run():
    print("=" * 65)
    print("🚀 DÉMARRAGE DU TEST INTÉGRAL DE TOUTES LES ENTITÉS ET RELATIONS")
    print("=" * 65 + "\n")

    results = []

    # 1. Agence
    print("🔹 1. TEST ENTITÉ : Agence")
    st, ag = req("POST", "/agences/ajouter", {
        "nom": "Agence Tunis Centre",
        "ville": "Tunis",
        "adresse": "Avenue Habib Bourguiba",
        "telephone": "+21671000111"
    })
    print(f"   [POST /agences/ajouter] -> {st} (ID: {ag.get('idAgence')})")
    assert st == 200, f"Failed Agence POST: {ag}"
    id_ag = ag["idAgence"]

    st, get_ag = req("GET", f"/agences/{id_ag}")
    print(f"   [GET /agences/{id_ag}] -> {st} ({get_ag.get('nom')})")
    assert st == 200

    st, mod_ag = req("PUT", "/agences/modifier", {
        "idAgence": id_ag,
        "nom": "Agence Tunis Centre-Ville",
        "ville": "Tunis",
        "adresse": "Avenue Habib Bourguiba, N° 12",
        "telephone": "+21671000222"
    })
    print(f"   [PUT /agences/modifier] -> {st} (Nouveau nom: {mod_ag.get('nom')})")
    assert st == 200
    results.append(("Agence", "CRUD Validé", "200 OK"))

    # 2. Employe (Relation avec Agence)
    print("\n🔹 2. TEST ENTITÉ : Employe (Relation @ManyToOne vers Agence)")
    st, emp = req("POST", "/employes/ajouter", {
        "nom": "Ben Salah",
        "prenom": "Ahmed",
        "role": "AGENT",
        "agence": {"idAgence": id_ag}
    })
    print(f"   [POST /employes/ajouter] -> {st} (ID: {emp.get('idEmploye')})")
    assert st == 200, f"Failed Employe POST: {emp}"
    id_emp = emp["idEmploye"]
    assert emp.get("agence", {}).get("idAgence") == id_ag, "Relation Employe -> Agence manquante !"
    print(f"   ✓ Relation vérifiée : Employe lié à Agence ID {id_ag}")

    st, get_emp = req("GET", f"/employes/{id_emp}")
    print(f"   [GET /employes/{id_emp}] -> {st} ({get_emp.get('prenom')} {get_emp.get('nom')})")
    assert st == 200

    st, mod_emp = req("PUT", "/employes/modifier", {
        "idEmploye": id_emp,
        "nom": "Ben Salah",
        "prenom": "Ahmed",
        "role": "MANAGER",
        "agence": {"idAgence": id_ag}
    })
    print(f"   [PUT /employes/modifier] -> {st} (Nouveau rôle: {mod_emp.get('role')})")
    assert st == 200
    results.append(("Employe", "CRUD & Relation Agence Validés", "200 OK"))

    # 3. Equipement
    print("\n🔹 3. TEST ENTITÉ : Equipement")
    st, eq = req("POST", "/equipements/ajouter", {
        "libelle": "GPS & Système d'aide à la conduite"
    })
    print(f"   [POST /equipements/ajouter] -> {st} (ID: {eq.get('idEquipement')})")
    assert st == 200
    id_eq = eq["idEquipement"]

    st, get_eq = req("GET", f"/equipements/{id_eq}")
    print(f"   [GET /equipements/{id_eq}] -> {st} ({get_eq.get('libelle')})")
    assert st == 200
    results.append(("Equipement", "CRUD Validé", "200 OK"))

    # 4. Vehicule
    print("\n🔹 4. TEST ENTITÉ : Vehicule")
    st, veh = req("POST", "/vehicules/ajouter", {
        "immatriculation": "250-TUNIS-7788",
        "marque": "Volkswagen",
        "modele": "Golf 8",
        "categorie": "BERLINE",
        "tarifJournalier": 160.00,
        "statut": "DISPONIBLE"
    })
    print(f"   [POST /vehicules/ajouter] -> {st} (ID: {veh.get('idVehicule')})")
    assert st == 200
    id_veh = veh["idVehicule"]

    st, get_veh = req("GET", f"/vehicules/{id_veh}")
    print(f"   [GET /vehicules/{id_veh}] -> {st} ({get_veh.get('marque')} {get_veh.get('modele')})")
    assert st == 200
    results.append(("Vehicule", "CRUD Validé", "200 OK"))

    # 5. Client
    print("\n🔹 5. TEST ENTITÉ : Client")
    st, cl = req("POST", "/clients/ajouter", {
        "nom": "Trabelsi",
        "prenom": "Sami",
        "email": "sami.trabelsi@esprit.tn",
        "telephone": "+21698765432",
        "numPermis": "TN-2023-999"
    })
    print(f"   [POST /clients/ajouter] -> {st} (ID: {cl.get('idClient')})")
    assert st == 200
    id_cl = cl["idClient"]

    st, get_cl = req("GET", f"/clients/{id_cl}")
    print(f"   [GET /clients/{id_cl}] -> {st} ({get_cl.get('prenom')} {get_cl.get('nom')})")
    assert st == 200

    st, mod_cl = req("PUT", "/clients/modifier", {
        "idClient": id_cl,
        "nom": "Trabelsi",
        "prenom": "Sami",
        "email": "sami.trabelsi.pro@esprit.tn",
        "telephone": "+21698765432",
        "numPermis": "TN-2023-999"
    })
    print(f"   [PUT /clients/modifier] -> {st} (Nouvel email: {mod_cl.get('email')})")
    assert st == 200
    results.append(("Client", "CRUD Validé", "200 OK"))

    # 6. Maintenance (Relation avec Vehicule)
    print("\n🔹 6. TEST ENTITÉ : Maintenance (Relation @ManyToOne vers Vehicule)")
    st, maint = req("POST", "/maintenances/ajouter", {
        "dateDebut": "2026-11-01",
        "dateFin": "2026-11-03",
        "description": "Contrôle technique et révision 20 000 km",
        "vehicule": {"idVehicule": id_veh}
    })
    print(f"   [POST /maintenances/ajouter] -> {st} (ID: {maint.get('idMaintenance')})")
    assert st == 200
    id_maint = maint["idMaintenance"]
    assert maint.get("vehicule", {}).get("idVehicule") == id_veh, "Relation Maintenance -> Vehicule manquante !"
    print(f"   ✓ Relation vérifiée : Maintenance liée au Véhicule ID {id_veh}")

    st, get_maint = req("GET", f"/maintenances/{id_maint}")
    print(f"   [GET /maintenances/{id_maint}] -> {st} ({get_maint.get('description')})")
    assert st == 200
    results.append(("Maintenance", "CRUD & Relation Vehicule Validés", "200 OK"))

    # 7. Reservation (Relations avec Client et Vehicule)
    print("\n🔹 7. TEST ENTITÉ : Reservation (Relations @ManyToOne vers Client et Vehicule)")
    st, res = req("POST", "/reservations/ajouter", {
        "dateDebut": "2026-11-10",
        "dateFin": "2026-11-15",
        "statut": "CONFIRMEE",
        "client": {"idClient": id_cl},
        "vehicule": {"idVehicule": id_veh}
    })
    print(f"   [POST /reservations/ajouter] -> {st} (ID: {res.get('idReservation')})")
    assert st == 200
    id_res = res["idReservation"]
    assert res.get("client", {}).get("idClient") == id_cl, "Relation Reservation -> Client manquante !"
    assert res.get("vehicule", {}).get("idVehicule") == id_veh, "Relation Reservation -> Vehicule manquante !"
    print(f"   ✓ Relations vérifiées : Reservation liée au Client ID {id_cl} et au Véhicule ID {id_veh}")

    st, get_res = req("GET", f"/reservations/{id_res}")
    print(f"   [GET /reservations/{id_res}] -> {st} (Statut: {get_res.get('statut')})")
    assert st == 200

    st, mod_res = req("PUT", "/reservations/modifier", {
        "idReservation": id_res,
        "dateDebut": "2026-11-10",
        "dateFin": "2026-11-17",
        "statut": "CONFIRMEE",
        "client": {"idClient": id_cl},
        "vehicule": {"idVehicule": id_veh}
    })
    print(f"   [PUT /reservations/modifier] -> {st} (Nouvelle dateFin: {mod_res.get('dateFin')})")
    assert st == 200
    results.append(("Reservation", "CRUD & Relations Client/Vehicule Validés", "200 OK"))

    # 8. Contrat (Relation avec Reservation)
    print("\n🔹 8. TEST ENTITÉ : Contrat (Relation @OneToOne vers Reservation)")
    st, cont = req("POST", "/contrats/ajouter", {
        "dateSignature": "2026-11-10",
        "montantTotal": 1120.00,
        "valide": True,
        "reservation": {"idReservation": id_res}
    })
    print(f"   [POST /contrats/ajouter] -> {st} (ID: {cont.get('idContrat')})")
    assert st == 200
    id_cont = cont["idContrat"]
    assert cont.get("reservation", {}).get("idReservation") == id_res, "Relation Contrat -> Reservation manquante !"
    print(f"   ✓ Relation vérifiée : Contrat lié à la Réservation ID {id_res}")

    st, get_cont = req("GET", f"/contrats/{id_cont}")
    print(f"   [GET /contrats/{id_cont}] -> {st} (Montant: {get_cont.get('montantTotal')} TND)")
    assert st == 200
    results.append(("Contrat", "CRUD & Relation Reservation Validés", "200 OK"))

    # 9. Paiement (Relation avec Contrat)
    print("\n🔹 9. TEST ENTITÉ : Paiement (Relation @ManyToOne vers Contrat)")
    st, pmt = req("POST", "/paiements/ajouter", {
        "montant": 1120.00,
        "datePaiement": "2026-11-10",
        "modePaiement": "CARTE",
        "contrat": {"idContrat": id_cont}
    })
    print(f"   [POST /paiements/ajouter] -> {st} (ID: {pmt.get('idPaiement')})")
    assert st == 200
    id_pmt = pmt["idPaiement"]
    assert pmt.get("contrat", {}).get("idContrat") == id_cont, "Relation Paiement -> Contrat manquante !"
    print(f"   ✓ Relation vérifiée : Paiement lié au Contrat ID {id_cont}")

    st, get_pmt = req("GET", f"/paiements/{id_pmt}")
    print(f"   [GET /paiements/{id_pmt}] -> {st} (Mode: {get_pmt.get('modePaiement')})")
    assert st == 200
    results.append(("Paiement", "CRUD & Relation Contrat Validés", "200 OK"))

    # 10. Test exhaustif de tous les GET /all
    print("\n" + "=" * 65)
    print("📋 VÉRIFICATION GLOBALE DES ENDPOINTS GET /all")
    print("=" * 65)
    endpoints_all = [
        ("Agence", "/agences/all"),
        ("Employe", "/employes/all"),
        ("Equipement", "/equipements/all"),
        ("Vehicule", "/vehicules/all"),
        ("Client", "/clients/all"),
        ("Maintenance", "/maintenances/all"),
        ("Reservation", "/reservations/all"),
        ("Contrat", "/contrats/all"),
        ("Paiement", "/paiements/all")
    ]
    for ent, path in endpoints_all:
        st, data = req("GET", path)
        count = len(data) if isinstance(data, list) else 0
        status_sym = "✓ 200 OK" if st == 200 else f"✗ {st}"
        print(f"   • {ent:<14} : GET {path:<20} -> {status_sym} ({count} élément(s))")
        assert st == 200

    print("\n" + "=" * 65)
    print("🎉 RÉSULTAT FINAL : 100% DES ENTITÉS ET RELATIONS SONT VALIDÉES !")
    print("=" * 65)

if __name__ == "__main__":
    run()
