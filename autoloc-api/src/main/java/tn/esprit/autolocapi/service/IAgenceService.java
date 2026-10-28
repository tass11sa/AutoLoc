package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Agence;

import java.util.List;

public interface IAgenceService {
    public Agence ajouterAgence(Agence agence);
    public Agence modifierAgence(Agence agence);
    public Agence getAgenceById(Long id);
    public List<Agence> getAllAgence();
    public Agence supprimerAgenceById(Long id);
}
