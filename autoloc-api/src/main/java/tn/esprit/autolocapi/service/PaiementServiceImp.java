package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Paiement;
import tn.esprit.autolocapi.repository.PaiementRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class PaiementServiceImp implements IPaiementService {

    private final PaiementRepository paiementRepository;

    @Override
    public Paiement ajouterPaiement(Paiement paiement) {

        return paiementRepository.save(paiement);
    }

    @Override
    public Paiement modifierPaiement(Paiement paiement) {

        return paiementRepository.save(paiement);
    }

    @Override
    public Paiement getPaiementById(Long id) {

        return paiementRepository.findById(id).orElse(null);
    }

    @Override
    public List<Paiement> getAllPaiement() {

        return paiementRepository.findAll();
    }

    @Override
    public Paiement supprimerPaiementById(Long id) {
        Paiement paiement = getPaiementById(id);
        if (paiement != null) {
            paiementRepository.deleteById(id);
        }
        return paiement;
    }
}
