package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Paiement;

import java.util.List;

public interface IPaiementService {
    public Paiement ajouterPaiement(Paiement paiement);
    public Paiement modifierPaiement(Paiement paiement);
    public Paiement getPaiementById(Long id);
    public List<Paiement> getAllPaiement();
    public Paiement supprimerPaiementById(Long id);
}
