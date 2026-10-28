package tn.esprit.autolocapi.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import tn.esprit.autolocapi.domain.Agence;
import tn.esprit.autolocapi.repository.AgenceRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class AgenceServiceImp implements IAgenceService {

    private final AgenceRepository agenceRepository;

    @Override
    public Agence ajouterAgence(Agence agence) {

        return agenceRepository.save(agence);
    }

    @Override
    public Agence modifierAgence(Agence agence) {

        return agenceRepository.save(agence);
    }

    @Override
    public Agence getAgenceById(Long id) {

        return agenceRepository.findById(id).orElse(null);
    }

    @Override
    public List<Agence> getAllAgence() {

        return agenceRepository.findAll();
    }

    @Override
    public Agence supprimerAgenceById(Long id) {
        Agence agence = getAgenceById(id);
        if (agence != null) {
            agenceRepository.deleteById(id);
        }
        return agence;
    }
}
