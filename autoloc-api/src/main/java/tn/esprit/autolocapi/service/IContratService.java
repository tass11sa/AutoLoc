package tn.esprit.autolocapi.service;

import tn.esprit.autolocapi.domain.Contrat;

import java.util.List;

public interface IContratService {
    public Contrat ajouterContrat(Contrat contrat);
    public Contrat modifierContrat(Contrat contrat);
    public Contrat getContratById(Long id);
    public List<Contrat> getAllContrat();
    public Contrat supprimerContratById(Long id);
}
