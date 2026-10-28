package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Equipement;

import java.util.List;

public interface IEquipementService {
    public Equipement ajouterEquipement(Equipement equipement);
    public Equipement modifierEquipement(Equipement equipement);
    public Equipement getEquipementById(Long id);
    public List<Equipement> getAllEquipement();
    public Equipement supprimerEquipementById(Long id);
}
