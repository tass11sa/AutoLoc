package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Contrat;
import tn.esprit.autolocapi.repository.ContratRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class ContratServiceImp implements IContratService {

    private final ContratRepository contratRepository;

    @Override
    public Contrat ajouterContrat(Contrat contrat) {

        return contratRepository.save(contrat);
    }

    @Override
    public Contrat modifierContrat(Contrat contrat) {

        return contratRepository.save(contrat);
    }

    @Override
    public Contrat getContratById(Long id) {

        return contratRepository.findById(id).orElse(null);
    }

    @Override
    public List<Contrat> getAllContrat() {

        return contratRepository.findAll();
    }

    @Override
    public Contrat supprimerContratById(Long id) {
        Contrat contrat = getContratById(id);
        if (contrat != null) {
            contratRepository.deleteById(id);
        }
        return contrat;
    }
}
